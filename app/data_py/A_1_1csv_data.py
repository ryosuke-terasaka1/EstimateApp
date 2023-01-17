import pandas as pd

HRBase_HM_df = pd.read_csv('csv_wav_data/HRBASE_5.csv', usecols=[i for i in range(2,22)], header=1, encoding="utf-8")
# print(HRBase_HM_df)
similarly_vocal = HRBase_HM_df['ボーカル']
similarly_melody = HRBase_HM_df['メロディ']
similarly_drum = HRBase_HM_df['ドラム']
body = HRBase_HM_df['全身']
vocal = HRBase_HM_df['ボーカル.1']
melody = HRBase_HM_df['メロディ.1']
drum = HRBase_HM_df['ドラム.1']
rightHand = HRBase_HM_df['右手']
rightFoot = HRBase_HM_df['右足']
rightElbow = HRBase_HM_df['右肘']
rightKnee = HRBase_HM_df['右膝']
leftHand = HRBase_HM_df['左手']
leftFoot = HRBase_HM_df['左足']
leftElbow = HRBase_HM_df['左肘']
leftKnee = HRBase_HM_df['左膝']
leftCoxa = HRBase_HM_df['左股関節']
rightCoxa = HRBase_HM_df['右股関節']

partsNameList = ['右手', '右足', '左手', '左足', '右肘', '右膝', '左肘', '左膝', '右股関節', '左股関節']

partsList = [rightHand, rightFoot, leftHand, leftFoot, rightElbow, rightKnee, leftElbow, leftKnee, rightCoxa, leftCoxa]
musicList = [vocal, melody, drum]
musicNameList = ['vocal', 'melody', 'drum']