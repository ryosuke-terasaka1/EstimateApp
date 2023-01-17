import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from music import Music

class Kinect():
    
    names_list=["PELVIS","SPINE_NAVAL","SPINE_CHEST","NECK","CLAVICLE_LEFT","SHOULDER_LEFT","ELBOW_LEFT","WRIST_LEFT",
    "HAND_LEFT","HANDTIP_LEFT","THUMB_LEFT","CLAVICLE_RIGHT","SHOULDER_RIGHT","ELBOW_RIGHT","WRIST_RIGHT","HAND_RIGHT",
    "HANDTIP_RIGHT","THUMB_RIGHT","HIP_LEFT","KNEE_LEFT","ANKLE_LEFT","FOOT_LEFT","HIP_RIGHT","KNEE_RIGHT",
    "ANKLE_RIGHT","FOOT_RIGHT","HEAD","NOSE","EYE_LEFT","EAR_LEFT","EYE_RIGHT","EAR_RIGHT"]

    kinect_names = ["Time"]
    for name in names_list:
        kinect_names.append(name + "_X")
        kinect_names.append(name + "_Y")
        kinect_names.append(name + "_Z")
    kinect_names.append("")

    def __init__(self, Music, kinect_file, kinect_start_timing):
        self.kinect_file: str = kinect_file
        self.Music = Music
        self.kinect_start_timing = kinect_start_timing

    def numpy_data(self, df: pd.DataFrame, body_part: str):
        numX=df[body_part + '_X'].to_numpy()
        numY=df[body_part + '_Y'].to_numpy()
        numZ=df[body_part + '_Z'].to_numpy()

        numX = np.ndarray.flatten(numX)
        numY = np.ndarray.flatten(numY)
        numZ = np.ndarray.flatten(numZ)

        num = np.stack([numX, numY, numZ], 1)
        return num


    def find_cos(self, start, point, end):
        cos_list = []
        for i in range(len(start)):
            vec_a = start[i] - point[i]
            vec_c = end[i] - point[i]

            # コサインの計算
            length_vec_a = np.linalg.norm(vec_a)
            length_vec_c = np.linalg.norm(vec_c)
            inner_product = np.inner(vec_a, vec_c)
            cos = inner_product / (length_vec_a * length_vec_c)

            # 角度（ラジアン）の計算
            rad = np.arccos(cos)

            # 弧度法から度数法（rad ➔ 度）への変換
            degree = np.rad2deg(rad)
            
            cos_list.append(degree)
        return cos_list


    def degree(self):
        df = pd.read_csv(self.kinect_file, header=None, names = self.kinect_names)
        WRIST_RIGHT_data = self.numpy_data(df, "WRIST_RIGHT")
        SHOULDER_RIGHT_data = self.numpy_data(df, "SHOULDER_RIGHT")
        ELBOW_RIGHT_data = self.numpy_data(df, "ELBOW_RIGHT")
        ANKLE_RIGHT_data = self.numpy_data(df, "ANKLE_RIGHT")
        HIP_RIGHT_data = self.numpy_data(df, "HIP_RIGHT")
        KNEE_RIGHT_data = self.numpy_data(df, "KNEE_RIGHT")
        WRIST_LEFT_data = self.numpy_data(df, "WRIST_LEFT")
        SHOULDER_LEFT_data = self.numpy_data(df, "SHOULDER_LEFT")
        ELBOW_LEFT_data = self.numpy_data(df, "ELBOW_LEFT")
        ANKLE_LEFT_data = self.numpy_data(df, "ANKLE_LEFT")
        HIP_LEFT_data = self.numpy_data(df, "HIP_LEFT")
        KNEE_LEFT_data = self.numpy_data(df, "KNEE_LEFT")
        PELVIS_data = self.numpy_data(df, "PELVIS")
        HIP_LEFT_data = self.numpy_data(df, "HIP_LEFT")
        ELBOW_RIGHT_degree = self.find_cos(WRIST_RIGHT_data, ELBOW_RIGHT_data, SHOULDER_RIGHT_data)
        KNEE_RIGHT_degree = self.find_cos(ANKLE_RIGHT_data, KNEE_RIGHT_data, HIP_RIGHT_data)
        ELBOW_LEFT_degree = self.find_cos(WRIST_LEFT_data, ELBOW_LEFT_data, SHOULDER_LEFT_data)
        KNEE_LEFT_degree = self.find_cos(ANKLE_LEFT_data, KNEE_LEFT_data, HIP_LEFT_data)

        PELVIS_data = self.numpy_data(df, "PELVIS")
        HIP_RIGHT_data = self.numpy_data(df, "HIP_RIGHT")
        HIP_LEFT_data = self.numpy_data(df, "HIP_LEFT")

        PEL_LEFT_degree = self.find_cos(PELVIS_data, HIP_LEFT_data, KNEE_LEFT_data)
        PEL_RIGHT_degree = self.find_cos(PELVIS_data, HIP_RIGHT_data, KNEE_RIGHT_data)
    
        return ELBOW_RIGHT_degree, KNEE_RIGHT_degree, ELBOW_LEFT_degree, KNEE_LEFT_degree, PEL_RIGHT_degree, PEL_LEFT_degree


    def kinect_timing_move(self, kinect_data, start_timing, small_threshold, large_threshold):
        kinect_data = kinect_data[start_timing:]   # 開始タイミング
        small_data_kind = [180 - data for data in kinect_data]
        
        large_data_kind = kinect_data
        large_peaks, _ = find_peaks(large_data_kind, height=large_threshold)
        small_peaks, _ = find_peaks(small_data_kind, height=(180-small_threshold))
        
        half_timing = [0 for _ in range(self.Music.music_half_count_length)]
        
        peak_time = []
        for i in large_peaks:
            time = float(i/30)
            peak_time.append(time)
        for i in small_peaks:
            time = float(i/30)
            peak_time.append(time)
        for i in peak_time:
            for j in range(1, len(self.Music.half_count_list)-1):
                if self.Music.half_count_list[j] <= i < self.Music.half_count_list[j+1]:
                    half_timing[j] = 1

        return half_timing

    
    def find_pose_timing_from_kinect(self, kinect_data, differ):
        peaks, _ = find_peaks(kinect_data)
        small_peaks, _ = find_peaks([180-data for data in kinect_data])
        pose_timing = []
        for i in range(1, len(peaks)):
            if abs(kinect_data[peaks[i]-1] - kinect_data[peaks[i]]) >= differ:
                pose_timing.append(peaks[i])

        for i in range(1, len(small_peaks)):
            if abs(kinect_data[small_peaks[i]-1] - kinect_data[small_peaks[i]]) >= differ:
                pose_timing.append(small_peaks[i])
        return pose_timing

    def kinect_timing_move_diff(self, kinect_data, differ):
        kinect_data = kinect_data[self.kinect_start_timing:]   # 開始タイミング
        peaks = self.find_pose_timing_from_kinect(kinect_data, differ)
        half_timing = [0 for _ in range(self.Music.music_half_count_length)]

        peak_time = []
        for i in peaks:
            time = float(i/50)
            peak_time.append(time)
        for i in peak_time:
            for j in range(1, len(self.Music.half_count_list)-1):
                if self.Music.half_count_list[j] <= i < self.Music.half_count_list[j+1]:
                    half_timing[j] = 1

        return half_timing
    
    def kinect_find_pose_timing(self):
        RE, RK, LE, LK, RP, LP = self.degree()
        self.RE = self.kinect_timing_move_diff(RE, 3)
        self.RK = self.kinect_timing_move_diff(RK, 3)
        self.LE = self.kinect_timing_move_diff(LE, 3)
        self.LK = self.kinect_timing_move_diff(LK, 3)
        self.RP = self.kinect_timing_move_diff(RP, 3)
        self.LP = self.kinect_timing_move_diff(LP, 3)