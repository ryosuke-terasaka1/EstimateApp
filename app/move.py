from accel import Accel
from kinect import Kinect
from sklearn.metrics import f1_score
import util
from data_py.A_1_1csv_data import body


class Move():
    def __init__(self, Accel: Accel, Kinect: Kinect):
        self.Accel = Accel
        self.Kinect = Kinect

    def partToBody(self, diff_threshold):
        result = []
        for i in range(len(self.partsList[0])):
            sum_part_timing = 0
            for j in range(len(self.partsList)):
                sum_part_timing += self.partsList[j][i]
            if sum_part_timing >= diff_threshold:
                result.append(1)
            else: result.append(0)
        return result

    def partToBody_minMax(self, min, max):
        result = []
        for i in range(len(self.partsList[0])):
            sum_part_timing = 0
            for j in range(len(self.partsList)):
                sum_part_timing += self.partsList[j][i]
            if max > sum_part_timing >= min:
                result.append(1)
            else: result.append(0)
        return result
    

    def find_pose_timimng(self):
        self.Accel.accel_find_pose_timing()
        self.Kinect.kinect_find_pose_timing()

        # self.partsList = [self.Accel.RH, self.Accel.RF, self.Accel.LH, self.Accel.LF, self.Kinect.RE, self.Kinect.RK, self.Kinect.LE, self.Kinect.LK]
        self.partsList = [self.Accel.RH, self.Accel.RF, self.Accel.LH, self.Accel.LF, self.Kinect.RE, self.Kinect.RK, self.Kinect.LE, self.Kinect.LK, self.Kinect.RP, self.Kinect.LP]
        # self.RE = self.kinect_timing_move()
        # for i in range(7):
        #     for j in range(i+1, 8):
        #         self.pose_timing = self.partToBody(4)

        # for i in range(1, 9):
        #     similarlyBody = self.partToBody(i)
        #     body_accuracy_graph, body_accuracy_num = self.CompareSimilarlyListWithHandmade(similarlyBody, body)
        #     # print(body_accuracy_graph)

        #     print('精度: ', body_accuracy_num, 'threshold: ', i)
        #     single_to_figure(body_accuracy_graph)

        sort_list = []
        f_sort_list = []
        for i in range(len(self.partsList)+1):
            for j in range(i+1, len(self.partsList)+2):
                similarlyBody = self.partToBody_minMax(i, j)
                body_accuracy_graph, body_accuracy_num = util.CompareSimilarlyListWithHandmade(similarlyBody, body)
                f = f1_score(similarlyBody, body)*100
                # print(body_accuracy_graph)
                sort_list.append([body_accuracy_num, i, j])
                f_sort_list.append([f, i, j])
                # print('精度: ', body_accuracy_num, 'min: ', i, 'max: ', j)
                # single_to_figure(body_accuracy_graph)
        sort_list.sort(reverse=True)
        f_sort_list.sort(reverse=True)
        print('sort_list: ', sort_list)
        print('f_sort_list', f_sort_list)
        
        self.pose_timing = self.partToBody_minMax(3, 11)
