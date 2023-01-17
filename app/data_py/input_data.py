faded_file_name_list = ['csv_wav_data/faded_accompaniment.wav', 'csv_wav_data/faded_vocals.wav', 'csv_wav_data/faded_drums.wav']
HR_file_name_list = ['csv_wav_data/uww2021_accompaniment.wav', 'csv_wav_data/uww2021_vocals.wav', 'csv_wav_data/uww2021_drums.wav']
faded_music_info = [faded_file_name_list]
HR_music_info = [HR_file_name_list]

HR_tempo = 89.10290948
HR_half_count = float(30/HR_tempo)
HR_quarter_count = float(15/HR_tempo)

# offset=10.828208616780046 - half_count # UWW: 10  toshi: 140
HR_offset=10.828208616780046 - (HR_half_count*2) # UWW: 10  toshi: 140
HR_duration=65  # UWW: 65  toshi: 60


toshi_accuracy_data = [2, 2, 2, 2, 2, 1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1]
uww2021_accuracy_data = [2,2,2,2,2,2,2, 1,1,1,1,1,1,1, 3,3,3,3,3,3,3]
uww2021_breakTime_nonBreak_accuracy_data = [1,1,1,1,1,1,3,3,3,3,3,3,2,2,2,2,2,2]
uww2021_mix_accuracy_data = [2,1,2,1,1,2,1,3, 2,3,2,3,3,2,3,3, 3,1,3,1,1,3,3,3]
KEY_accuracy_data = [3,3,3,3,3,3,3,3, 1,1,1,1,1,1,1,1, 2,2,2,2,2,2,2,2]
vana_faded_accuracy_data = [1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2]
tsuchida_accuracy_data = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2]
zulu_accuracy_data = [1, 1, 1, 1, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]

faded_rule_length_list = [(0, 32, 8), (32, 4, 4), (36, 128, 8)]
uww2021_rule_length_list = [(0, 168, 8)]
uww2021_real_rule_length_list = [(0, 56, 8), (64, 56, 8), (128, 56, 8)]
uww2021_breakTime_nonBreak_rule_length_list = [(0, 144, 8)]
uww2021_mix_rule_length_list = [(0, 192, 8)]
tsuchida_rule_length_list = [(0, 192, 8)]
KEY_rule_length_list = [(0, 192, 8)]

list_name = ['faded_pop', 'uww_normal', 'uww_breakTime', 'uww_mix','KEY', 'faded_break', 'tsuchida', 'zulu']
rule_length_lists = [faded_rule_length_list, uww2021_rule_length_list, uww2021_breakTime_nonBreak_rule_length_list, uww2021_mix_rule_length_list, KEY_rule_length_list, faded_rule_length_list, tsuchida_rule_length_list, faded_rule_length_list]
accuracy_lists = [toshi_accuracy_data, uww2021_accuracy_data, uww2021_breakTime_nonBreak_accuracy_data, uww2021_mix_accuracy_data, KEY_accuracy_data, vana_faded_accuracy_data, tsuchida_accuracy_data, zulu_accuracy_data]