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
    A_M1_Ver1.Exam3_Result()

    # librosa = mel > stft >>>>>>>> rms
    # A_M1_Ver1.Music.music_find_start_timing()
    # A_M1_Ver1.Music._find_onset_num_mel()
    # A_M1_Ver1.Music._find_onset_num_rms()
    # A_M1_Ver1.Music._find_onset_num_stft()

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

    print('A_M1_Ver2: ')
    A_M1_Ver2.Exam3_Result()
    print('A_M1_Ver3: ')
    A_M1_Ver3.Exam3_Result()
    print('A_M2_Ver1: ')
    A_M2_Ver1.Exam3_Result()
    print('A_M3_Ver1: ')
    A_M3_Ver1.Exam3_Result()
    print('B_M1_Ver1: ')
    B_M1_Ver1.Exam3_Result()
    print('C_M2_Ver1: ')
    C_M2_Ver1.Exam3_Result()
    print('D_M2_Ver1: ')
    D_M2_Ver1.Exam3_Result()
    
    # print(A_M1_Ver1.Music.onset_num)
    # print(A_M2_Ver1.Music.onset_num)
    # print(A_M3_Ver1.Music.onset_num)
    Subject_List = [A_M1_Ver1, A_M1_Ver2, A_M1_Ver3, A_M2_Ver1, A_M3_Ver1, B_M1_Ver1, C_M2_Ver1, D_M2_Ver1]
    sensor2dupT_accList = [[subject.Estimate.vo_num, subject.Estimate.me_num, subject.Estimate.dr_num] for subject in Subject_List]
    sensor2dupT_accList_f = [[subject.Estimate.vo_num_f, subject.Estimate.me_num_f, subject.Estimate.dr_num_f] for subject in Subject_List]
    vo_accList = [accL[0] for accL in sensor2dupT_accList]
    me_accList = [accL[1] for accL in sensor2dupT_accList]
    dr_accList = [accL[2] for accL in sensor2dupT_accList]
    vo_accList_f = [accL[0] for accL in sensor2dupT_accList_f]
    me_accList_f = [accL[1] for accL in sensor2dupT_accList_f]
    dr_accList_f = [accL[2] for accL in sensor2dupT_accList_f]
    rulebase_accList = [subject.Estimate.RuleBase_accuracy for subject in Subject_List]
    tfIdf_accList = [subject.Estimate.TfIdf_accuracy for subject in Subject_List]
    print('exma2_result: ', sensor2dupT_accList)
    print('vo_acc_f: ', vo_accList_f)
    print('me_acc_f: ', me_accList_f)
    print('dr_acc_f: ', dr_accList_f)
    print('RuleBase: ', rulebase_accList)
    print('tf/idf: ', tfIdf_accList)
    
    rulebase_confusion_matrix = [[0, 0, 0] for _ in range(3)]
    tfidf_confusion_matrix = [[0, 0, 0] for _ in range(3)]
    for subject in Subject_List:
        rulebase_confusion_matrix = [[elm_a + elm_b for elm_a, elm_b in zip(row_a,row_b)] for row_a,row_b in zip(rulebase_confusion_matrix,subject.Estimate.rulebase_confusion_matrix)]
    print('rulebase_confusion_matrix: ', rulebase_confusion_matrix)
    for subject in Subject_List:
        tfidf_confusion_matrix = [[elm_a + elm_b for elm_a, elm_b in zip(row_a,row_b)] for row_a,row_b in zip(tfidf_confusion_matrix,subject.Estimate.tfidf_confusion_matrix)]
        print('tfidf_confusion_matrix: ', tfidf_confusion_matrix)