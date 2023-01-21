from exam_subject.A_1_1 import A_M1_Ver1
from exam_subject.A_1_2 import A_M1_Ver2
from exam_subject.A_1_3 import A_M1_Ver3
from exam_subject.A_2_1 import A_M2_Ver1
from exam_subject.A_3_1 import A_M3_Ver1
from exam_subject.B_1_1 import B_M1_Ver1
from exam_subject.C_2_1 import C_M2_Ver1
from exam_subject.D_2_1 import D_M2_Ver1

if __name__ == '__main__':

    # print('A_M1_Ver1: ')
    # A_M1_Ver1.Result()

    # librosa = mel > stft >>>>>>>> rms
    A_M1_Ver1.Music.music_find_start_timing()
    A_M1_Ver1.Music._find_onset_num_mel()
    A_M1_Ver1.Music._find_onset_num_rms()
    A_M1_Ver1.Music._find_onset_num_stft()

    # # stft >= librosa > mel >>> rms
    # A_M2_Ver1.Music.music_find_start_timing()
    # A_M2_Ver1.Music._find_onset_num_mel()
    # A_M2_Ver1.Music._find_onset_num_rms()
    # A_M2_Ver1.Music._find_onset_num_stft()

    # # 一番意図してるのはrms? > librosa = mel >>>>stft
    # A_M3_Ver1.Music.music_find_start_timing()
    # A_M3_Ver1.Music._find_onset_num_mel()
    # A_M3_Ver1.Music._find_onset_num_rms()
    # A_M1_Ver1.Music._find_onset_num_stft()

    # print('A_M1_Ver2: ')
    # A_M1_Ver2.Result()
    # print('A_M1_Ver3: ')
    # A_M1_Ver3.Result()
    # print('A_M2_Ver1: ')
    # A_M2_Ver1.Result()
    # print('A_M3_Ver1: ')
    # A_M3_Ver1.Result()
    # print('B_M1_Ver1: ')
    # B_M1_Ver1.Result()
    # print('C_M2_Ver1: ')
    # C_M2_Ver1.Result()
    # print('D_M2_Ver1: ')
    # D_M2_Ver1.Result()
    
    # print(A_M1_Ver1.Music.onset_num)
    # print(A_M2_Ver1.Music.onset_num)
    # print(A_M3_Ver1.Music.onset_num)
    # Subject_List = [A_M1_Ver1, A_M1_Ver2, A_M1_Ver3, A_M2_Ver1, A_M3_Ver1, B_M1_Ver1, C_M2_Ver1, D_M2_Ver1]
    # sensor2dupT_accList = [[subject.Estimate.vo_num, subject.Estimate.me_num, subject.Estimate.dr_num] for subject in Subject_List]
    # vo_accList = [accL[0] for accL in sensor2dupT_accList]
    # me_accList = [accL[1] for accL in sensor2dupT_accList]
    # dr_accList = [accL[2] for accL in sensor2dupT_accList]
    # rulebase_accList = [subject.Estimate.RuleBase_accuracy for subject in Subject_List]
    # tfIdf_accList = [subject.Estimate.TfIdf_accuracy for subject in Subject_List]
    # print('exma2_result: ', sensor2dupT_accList)
    # print('vo_acc: ', vo_accList)
    # print('me_acc: ', me_accList)
    # print('dr_acc: ', dr_accList)
    # print('RuleBase: ', rulebase_accList)
    # print('tf/idf: ', tfIdf_accList)