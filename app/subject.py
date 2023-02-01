from music import Music
from move import Move
from accel import Accel
from kinect import Kinect
from estimate import EstimatePart
from typing import List


class Subject():
    def __init__(self):
        self.RuleList: List[int]
        self.LengthList: List[int]
        self.Accuracy: List[int]
        self.Music: Music
        self.Move: Move
        self.RuleList: List[str]
        self.Accel: Accel
        self.Kinect = Kinect
        self.Estimate = EstimatePart


    def Exam3_Result(self):
        self.Move.find_pose_timimng()
        
        self.Estimate = EstimatePart(Music=self.Music, Move=self.Move, rule_list=self.RuleList, rule_length_list=self.LengthList, accuracy_list=self.Accuracy)
        self.Estimate.evaluate()