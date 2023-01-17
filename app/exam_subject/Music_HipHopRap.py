from music import Music
from data_py.input_data import HR_file_name_list, HR_half_count

Music_1 = Music(HR_file_name_list, tempo=89.10290948, offset=10.828208616780046 - (HR_half_count*2), duration=65, music_count_length=96)
Music_1.find_onset()