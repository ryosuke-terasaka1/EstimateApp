from subject import Subject
from .Music_HipHopRap import Music_1
from kinect import Kinect
from accel import Accel


A_M1_Ver1 = Subject()
A_M1_Ver1.Music = Music_1
A_M1_Ver1.Accel = Accel(Music_1, ['csv_wav_data/righthand02.csv', 'csv_wav_data/rightfoot02.csv', 'csv_wav_data/lefthand02.csv', 'csv_wav_data/leftfoot02.csv'], 642)
A_M1_Ver1.Kinect = Kinect(Music_1, 'csv_wav_data/kinect_uww2021.csv', 280)
A_M1_Ver1.LengthList = [(0, 56, 8), (64, 56, 8), (128, 56, 8)]
A_M1_Ver1.RuleList = ['ドラム', 'ドラム', 'メロディ', 'ドラム', 'ボーカル', 'ボーカル', 'メロディ', 'メロディ', 'ボーカル', 'None', 'ドラム', 'メロディ']
A_M1_Ver1.Accuracy = [2,2,2,2,2,2,2, 1,1,1,1,1,1,1, 3,3,3,3,3,3,3]
