import japanize_matplotlib
import matplotlib.pyplot as plt
import matplotlib as mpl

def CompareSimilarlyListWithHandmade(similaryList, handmadeList):
        result = []
        ok_sum = 0
        miss_num = 0
        for similarly, handmade in zip(similaryList, handmadeList):
            if similarly == handmade:
                ok_sum += 1
                if similarly == 1:
                    result.append(3)
                else: result.append(2)
            else:
                miss_num += 1
                if handmade == 1:
                    result.append(1)
                else: result.append(0)
        return result, (ok_sum/(ok_sum + miss_num))*100



def enlarge_sentence(sentence: list, length: int) -> list:
        return [num for num in sentence for _ in range(length)]



def to_figure(figure_time_list, rulebase_estimated_part,tfidf_estimated_part, concious_part):
    data_length = len(rulebase_estimated_part)
    # figure_time_list = []
    # for i in range(data_length):
        # figure_time_list.append(i * 16 * Music.quarter_count / 100)
#         figure_time_list.append(i * 16 * quarter_count / 100)
#     print(time_list)
#     df1 = df1.astype(float)
    x1 = figure_time_list
    y1 = rulebase_estimated_part
    y2 = tfidf_estimated_part
    y3 = concious_part


    # Figureの初期化
    fig = plt.figure(figsize=(12, 5)) #...1

    #図の形式定義
    # plt.rcParams['font.family'] ='Yu Gothic'#使用するフォント
    # plt.rcParams['xtick.direction'] = 'in'#x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    # plt.rcParams['ytick.direction'] = 'in'#y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    # plt.rcParams['xtick.major.width'] = 1.0#x軸主目盛り線の線幅
    # plt.rcParams['ytick.major.width'] = 1.0#y軸主目盛り線の線幅
    # plt.rcParams['font.size'] = 19 #フォントの大きさ
    # plt.rcParams['axes.linewidth'] = 1.0# 軸の線幅edge linewidth。囲みの太さ
    
#     label_l = ['','drum', 'melody', 'vocal']
    label_l = ['None', 'drum', 'melody', 'vocal']
    # label_l = ['', 'None', 'drum', 'melody', 'vocal']
#     label_l = ['', 'melody', 'drum', 'vocal']

    ax = fig.add_subplot(2, 1, 1)#(行，列，領域番号)
    ax.plot(x1, y1,c="blue",label='Estimated Part',linewidth=0.8)
    ax.plot(x1, y3,c="red",label='Conscious Part',linewidth=0.8)
    ax.set_xlabel('Time[s]',fontsize=22)
#     ax.set_ylabel('acc')
#     ax.set_xlim((0,14000))
    ax.set_ylim((0, 4.2))
    ax.set_title("rule-base method",fontsize=26)
    # ax.set_title("tf-idf method",fontsize=26)
    ax.yaxis.set_major_locator(mpl.ticker.IndexLocator(1, -1))
    ax.set_yticklabels(label_l, ha='right',fontsize=22)
    ax.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left', fontsize=19)
#     ax.show()

    ax = fig.add_subplot(2, 1, 2)
    ax.plot(x1, y2,c="green",label='Estimated Part',linewidth=0.8)
    ax.plot(x1, y3,c="red",label='Conscious Part',linewidth=0.8)
    ax.set_xlabel('Time[s]',fontsize=22)
#     ax.set_ylabel('ang')
#     ax.set_xlim((0,14000))
    ax.set_title("tf/idf method",fontsize=26)
    ax.set_ylim((0, 4.2))
    ax.yaxis.set_major_locator(mpl.ticker.IndexLocator(1, -1))
    ax.set_yticklabels(label_l, ha='right',fontsize=22)
    ax.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left',fontsize=19)

    figname = 'uww2021_dataA_3.pdf'
    plt.tight_layout()#グラフが重ならず，設定した図のサイズ内に収まる。
    plt.savefig(figname)