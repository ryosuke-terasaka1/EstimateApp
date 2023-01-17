import pandas as pd
import math
from music import Music
from scipy.signal import find_peaks
import numpy as np


class Accel():
    
    def __init__(self, Music: Music, accel_file_list, accel_start_timing):
        self.Music = Music
        self.accel_file_list = accel_file_list
        self.accel_start_timing = accel_start_timing
        self.diff_threshold: int

    def accel_composite(self, file_path):
        df = pd.read_csv(file_path, header = None, usecols=[3, 4, 5])
        df.columns = ["x", "y", "z"]
        composite = []
        for i in range(len(df)):
            x_value = float(df["x"][i] ** 2)
            y_value = float(df["y"][i] ** 2)
            z_value = float(df["z"][i] ** 2)
            composite_value = math.sqrt(x_value + y_value + z_value)
            composite.append(composite_value)
        return composite[self.accel_start_timing:]  # 開始タイミング

    def find_pose_timing_from_accel(self, accel_data, differ):
        peaks, _ = find_peaks(accel_data)
        pose_timing = []
        for i in range(1, len(peaks)):
            if abs(accel_data[peaks[i]-1] - accel_data[peaks[i]]) >= differ:
                pose_timing.append(peaks[i])
        return pose_timing

    def accel_timing_move(self, file_path, differ, threshold_level=0, small_or_large='large'):
        composite = self.accel_composite(file_path)
        accel_data = np.array(composite)
        accel_data = np.ndarray.flatten(accel_data)
        
        peaks = self.find_pose_timing_from_accel(accel_data, differ)
        
        count = 0
        half_timing = []
        quarter_timing = []
        for _ in range(self.Music.music_half_count_length):
            half_timing.append(0)
        for _ in range(self.Music.music_quarter_count_length):
            quarter_timing.append(0)

        peak_time = []
        for i in peaks:
            time = float(i/50)
            peak_time.append(time)
        for i in peak_time:
            for j in range(1, len(self.Music.half_count_list)-1):
                if self.Music.half_count_list[j] <= i < self.Music.half_count_list[j+1]:
                    half_timing[j] = 1
        return half_timing
    

    def accel_find_pose_timing(self):
        self.RH = self.accel_timing_move(self.accel_file_list[0], 100)
        self.RF = self.accel_timing_move(self.accel_file_list[1], 400)
        self.LH = self.accel_timing_move(self.accel_file_list[2], 100)
        self.LF = self.accel_timing_move(self.accel_file_list[3], 400)
