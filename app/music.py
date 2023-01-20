from typing import List
import librosa
import librosa.display
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


class Music():
    file_name: List[str]
    def __init__(self, file_list, tempo, offset, duration, music_count_length):
        # self.file_name: List[str]
        self.file_name_list = file_list
        self.tempo = tempo
        self.half_count = float(30/self.tempo)
        self.quarter_count = float(30/self.tempo)
        self.offset = offset
        self.duration = duration
        self.music_count_length = music_count_length
        self.music_half_count_length = music_count_length * 2
        self.music_quarter_count_length = music_count_length * 4
        self.half_count_list = [i * self.half_count for i in range(self.music_half_count_length)]
        

    def _find_onset_RMS(self, file_name):
        y, sr = librosa.load(file_name, offset=self.offset, duration=self.duration)

        frame_length = 2048
        hop_length = frame_length // 4
        rms = librosa.feature.rms(y, frame_length=frame_length, hop_length=hop_length, center=True)

        # print(f'rms.shape: {rms.shape}')
        # print(f'rms.shape[1] = y.shape[0] // hop_length + 1 = {y.shape[0]} // {hop_length} + 1 = {y.shape[0] // hop_length + 1}')

        onset_envelope = rms[0, 1:] - rms[0, :-1]
        onset_envelope = np.maximum(0.0, onset_envelope)
        onset_envelope = onset_envelope / onset_envelope.max()

        pre_max = 30 / 1000 * sr // hop_length
        post_max = 0 / 1000 * sr // hop_length + 1
        pre_avg = 100 / 1000 * sr // hop_length
        post_avg = 100 / 1000 * sr // hop_length + 1
        wait = 30 / 1000 * sr // hop_length
        delta = 0.07
        onset_frames = librosa.util.peak_pick(onset_envelope, pre_max, post_max, pre_avg, post_avg, delta, wait)

        times = librosa.times_like(onset_envelope, sr=sr)
        # print(times)

        half_timing = [0 for _ in range(self.music_half_count_length)]

        index = 0
        for i in range(len(self.half_count_list)-1):
            if index < len(onset_frames) and self.half_count_list[i] <= times[onset_frames[index]] < self.half_count_list[i+1]:
                half_timing[i] = 1
                while index < len(onset_frames) and times[onset_frames[index]] < self.half_count_list[i+1]:
                    index += 1

        return half_timing
    
        

    def _find_onset_mel(self, file_name):
        y, sr = librosa.load(file_name, offset=self.offset, duration=self.duration)

        win_length = 2048
        hop_length = win_length // 4
        n_fft = win_length
        window = 'hann'
        n_mels = 128
        mel_power = librosa.feature.melspectrogram(y, sr=sr, n_fft=n_fft, hop_length=hop_length, win_length=win_length,
                                                   window=window, center=True, n_mels=n_mels)
        log_power = librosa.power_to_db(mel_power, ref=np.max)
        onset_envelope = log_power[:, 1:] - log_power[:, :-1]
        onset_envelope = np.mean(onset_envelope, axis=0)
        onset_envelope = np.maximum(0.0, onset_envelope)
        onset_envelope = onset_envelope / onset_envelope.max()

        pre_max = 30 / 1000 * sr // hop_length
        post_max = 0 / 1000 * sr // hop_length + 1
        pre_avg = 100 / 1000 * sr // hop_length
        post_avg = 100 / 1000 * sr // hop_length + 1
        wait = 30 / 1000 * sr // hop_length
        delta = 0.07
        onset_frames = librosa.util.peak_pick(onset_envelope, pre_max, post_max, pre_avg, post_avg, delta, wait)

        times = librosa.times_like(onset_envelope, sr=sr)
        # print(f'times: {times}, length: {len(times)}')
        # for frame in onset_frames:
        #     print(times[frame])
        # print('onset_frames: ', times[onset_frames])
        # print(f'length: {len(onset_frames)}')
        half_timing = [0 for _ in range(self.music_half_count_length)]

        index = 0
        for i in range(len(self.half_count_list)-1):
            if index < len(onset_frames) and self.half_count_list[i] <= times[onset_frames[index]] < self.half_count_list[i+1]:
                half_timing[i] = 1
                while index < len(onset_frames) and times[onset_frames[index]] < self.half_count_list[i+1]:
                    index += 1
        return half_timing


    def _find_onset_librosa(self, file_name):
        y, sr = librosa.load(file_name, offset=self.offset, duration=10)

        frame_length = 2048
        hop_length = frame_length // 4
        onset_frames = librosa.onset.onset_detect(y, sr=sr, hop_length=hop_length)
        times = librosa.frames_to_time(onset_frames, sr=sr, hop_length=hop_length)
        print(times[:50])
        fig = plt.figure(figsize=(6.4, 4.8/2))
        ax = fig.add_subplot()
        librosa.display.waveshow(y, sr=sr)
        ax.vlines(times, -1, 1, color='r', linestyle='--', label='onsets')
        ax.legend(frameon=True, framealpha=0.75)
        ax.set_title('sound wave')
        plt.tight_layout()
        plt.show()



    def find_onset(self):
        self.melody_onset = self._find_onset_RMS(self.file_name_list[0])
        self.vocal_onset = self._find_onset_RMS(self.file_name_list[1])
        self.drum_onset = self._find_onset_RMS(self.file_name_list[2])
        

    def music_find_start_timing(self):
        print('メロディ')
        self._find_onset_librosa(self.file_name_list[0])
        print('ボーカル')
        self._find_onset_librosa(self.file_name_list[1])
        print('ドラム')
        self._find_onset_librosa(self.file_name_list[2])