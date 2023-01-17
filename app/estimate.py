from music import Music
from move import Move
import util
from typing import List
from data_py.A_1_1csv_data import similarly_vocal, similarly_melody, similarly_drum

class EstimatePart():
    def __init__(self, Music: Music, Move: Move, rule_list: List[str], rule_length_list, accuracy_list):
        self.Music = Music
        self.Move = Move
        self.rule_list = rule_list
        self.rule_length_list = rule_length_list
        self.accuracy_list = accuracy_list


    def createRuleInput(self, ruleNameList):
        rule_dic = {}
        rule_dic[(0, 0, 0)] = ruleNameList[0]
        rule_dic[(0, 0, 1)] = ruleNameList[1]
        rule_dic[(0, 1, 0)] = ruleNameList[2]
        rule_dic[(0, 1, 1)] = ruleNameList[3]
        rule_dic[(1, 0, 0)] = ruleNameList[4]
        rule_dic[(1, 0, 1)] = ruleNameList[5]
        rule_dic[(1, 1, 0)] = ruleNameList[6]
        rule_dic[(1, 1, 1)] = ruleNameList[7]
        priority_rank = [ruleNameList[i] for i in range(8, 12)]
        return [rule_dic, priority_rank]

    def CreateSimilarlyList(self, moveList, musicPartList):
        result = []
        for move, part in zip(moveList, musicPartList):
            if move == part == 1:
                result.append(1)
            else: result.append(0)
        return result

    def find_dupTiming(self):
        self.vocal_dupTiming = self.CreateSimilarlyList(self.Move.pose_timing, self.Music.vocal_onset)
        self.melody_dupTiming = self.CreateSimilarlyList(self.Move.pose_timing, self.Music.melody_onset)
        self.drum_dupTiming = self.CreateSimilarlyList(self.Move.pose_timing, self.Music.drum_onset)
        
        vo_re, vo_num = util.CompareSimilarlyListWithHandmade(self.vocal_dupTiming, similarly_vocal)
        me_re, me_num = util.CompareSimilarlyListWithHandmade(self.melody_dupTiming, similarly_melody)
        dr_re, dr_num = util.CompareSimilarlyListWithHandmade(self.drum_dupTiming, similarly_drum)
        print('v-m-d', vo_num, me_num, dr_num)
        figure_time_list = [i * 16 * self.Music.quarter_count / 100 for i in range(len(vo_re))]

        util.single_to_figure(vo_re, figure_time_list)
        util.single_to_figure(me_re, figure_time_list)
        util.single_to_figure(dr_re, figure_time_list)

    def evaluate_RuleBase(self):
        to_int_dic = {'ボーカル': 3, 'メロディ': 2, 'ドラム': 1, 'None': 0}
        accuracy = 0
        result = []
        self.rule_dic = self.createRuleInput(self.rule_list)
        
        part_result = []
        score = 0
        combination_rule, priority_rank = self.rule_dic[0], self.rule_dic[1]
        for vo, me, dr in zip(self.vocal_dupTiming, self.melody_dupTiming, self.drum_dupTiming):
            part_result.append(combination_rule[(vo, me, dr)])
            
        for start, length, interval in self.rule_length_list:
            end = start + length
            for i in range(start, end, interval):
                v_measure = part_result[i:i+interval].count('ボーカル')
                m_measure = part_result[i:i+interval].count('メロディ')
                d_measure = part_result[i:i+interval].count('ドラム')
                n_measure = part_result[i:i+interval].count('None')
                max_num = max(v_measure, m_measure, d_measure, n_measure)

                rule_base_list = []
                if m_measure == max_num:
                    rule_base_list.append('メロディ')
                if v_measure == max_num:
                    rule_base_list.append('ボーカル')
                if d_measure == max_num:
                    rule_base_list.append('ドラム')
                if n_measure == max_num:
                    rule_base_list.append('None')

                # rule_base_listが空になることはない
                if len(rule_base_list) >= 2:
                    if priority_rank[0] in rule_base_list:
                        rule_base_list = [priority_rank[0]]
                    elif priority_rank[1] in rule_base_list:
                        rule_base_list = [priority_rank[1]]
                    elif priority_rank[2] in rule_base_list:
                        rule_base_list = [priority_rank[2]]
                    elif priority_rank[3] in rule_base_list:
                        rule_base_list = [priority_rank[3]]

                result.append(to_int_dic[rule_base_list[0]])
        for tmp, acc in zip(result, self.accuracy_list):
            if tmp == acc: score += 1

        accuracy = (score / len(result)) * 100
        self.RuleBase_accuracy = accuracy
        self.RuleBase_result = result

    def _one_dimension_tfidf(self, vocal, melody, drum, start, length, interval):
    # idfの決定
        v_sum = sum(vocal)
        m_sum = sum(melody)
        d_sum = sum(drum)

        tf_idf_result = [] 
        end = start + length

        for i in range(start, end, interval):
            v_measure = sum(vocal[i:i+interval])
            v_tfidf = v_measure / v_sum
            
            m_measure = sum(melody[i:i+interval])
            m_tfidf = m_measure / m_sum
            
            d_measure = sum(drum[i:i+interval])
            d_tfidf = d_measure / d_sum
            
            max_num = max(v_tfidf, m_tfidf, d_tfidf)
            
            tf_idf_list = []
            
            if max_num == 0:
                tf_idf_list.append('None')
            
            else:
                if m_tfidf == max_num:
                    tf_idf_list.append('メロディ')
                if v_tfidf == max_num:
                    tf_idf_list.append('ボーカル')
                if d_tfidf == max_num:
                    tf_idf_list.append('ドラム')

            tf_idf_result.append(tf_idf_list)
    #         print(tf_idf_result)
        
        return tf_idf_result

    def _DoubleListToIntList(self, doubleList):
        ans = []
        for singleList in doubleList:
            if singleList == ['ボーカル']: ans.append(3)
            elif singleList == ['メロディ']: ans.append(2)
            elif singleList == ['ドラム']: ans.append(1)
            elif singleList == ['None']: ans.append(0)
        return ans
        

    def _one_dimension_part_to_value(self):
        ans=[]
        for start, length, interval in self.rule_length_list:
            ans += self._one_dimension_tfidf(self.vocal_dupTiming, self.melody_dupTiming, self.drum_dupTiming, start, length, interval)
        # print(ans, len(ans))
        return self._DoubleListToIntList(ans)

    def _Score(self, exam, accuracy):
        plus = 0
        if len(exam) != len(accuracy):
            return print('wrong length')
        for i, j in zip(exam, accuracy):
            if i == j:
                plus += 1
        return plus / len(exam)

    def evaluate_tfIdf(self):
        self.TfIdf_result = self._one_dimension_part_to_value()
        # print(len(self.TfIdf_result))
        accu = self.accuracy_list
        # print(len(accu), len(self.TfIdf_result))
        self.TfIdf_accuracy = self._Score(self.TfIdf_result, accu) * 100


    def pickUpData(self):
        print(f'RuleBaseAccuracy: {self.RuleBase_accuracy}, TfIdfAccuracy: {self.TfIdf_accuracy}')
        enl_rulebase_estimate = util.enlarge_sentence(self.RuleBase_result, 100)
        enl_tfIdf_estimate = util.enlarge_sentence(self.TfIdf_result, 100)
        enl_accuracy_data = util.enlarge_sentence(self.accuracy_list, 100)
        
        figure_time_list = [i * 16 * self.Music.quarter_count / 100 for i in range(len(enl_accuracy_data))]

        util.to_figure(
            figure_time_list,
            enl_rulebase_estimate,
            enl_tfIdf_estimate,
            enl_accuracy_data
            )

    def evaluate(self):
        self.find_dupTiming()
        # print(self.melody_dupTiming)
        self.evaluate_RuleBase()
        # print(self.RuleBase_result)
        self.evaluate_tfIdf()
        self.pickUpData()
