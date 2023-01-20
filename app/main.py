from exam_subject.A_1_1 import A_M1_Ver1
from exam_subject.A_1_2 import A_M1_Ver2
from exam_subject.A_1_3 import A_M1_Ver3
from exam_subject.A_2_1 import A_M2_Ver1
from exam_subject.A_3_1 import A_M3_Ver1
from exam_subject.B_1_1 import B_M1_Ver1
from exam_subject.C_2_1 import C_M2_Ver1
from exam_subject.D_2_1 import D_M2_Ver1

if __name__ == '__main__':

    print('A_M1_Ver1: ')
    A_M1_Ver1.Result()
    print('A_M1_Ver2: ')
    A_M1_Ver2.Result()
    print('A_M1_Ver3: ')
    A_M1_Ver3.Result()
    print('A_M2_Ver1: ')
    A_M2_Ver1.Result()
    print('A_M3_Ver1: ')
    A_M3_Ver1.Result()
    print('B_M1_Ver1: ')
    B_M1_Ver1.Result()
    print('C_M2_Ver1: ')
    C_M2_Ver1.Result()
    print('D_M2_Ver1: ')
    D_M2_Ver1.Result()
    
    Subject_List = [A_M1_Ver1, A_M1_Ver2, A_M1_Ver3, A_M2_Ver1, A_M3_Ver1, B_M1_Ver1, C_M2_Ver1, D_M2_Ver1]
    sensor2dupT_accList = [[subject.Estimate.vo_num, subject.Estimate.me_num, subject.Estimate.dr_num] for subject in Subject_List]
    rulebase_accList = [subject.Estimate.RuleBase_accuracy for subject in Subject_List]
    tfIdf_accList = [subject.Estimate.TfIdf_accuracy for subject in Subject_List]
    print('exma2_result: ', sensor2dupT_accList)
    print('RuleBase: ', rulebase_accList)
    print('tf/idf: ', tfIdf_accList)