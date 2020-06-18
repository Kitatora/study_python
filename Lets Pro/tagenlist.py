#encoding:utf-8
stafflist=[["A", 25], ["B", 30], ["C", 40]]
for name in [0, 1, 2]: #listのインデックス番号1
    for old in [0, 1]: #listのインデックス番号2
        print(stafflist[name][old])


#以下、多次元リストの仕組み
#ありがちなNG例
# stafflist=[["A", 25], ["B", 30], ["C", 40]]
# for i in stafflist[0, 1, 2]: #エラー。list indices must be integers or slices. Not tuple.(リストは整数およびスライスでないとだめ)
#     print(i)

#正解
stafflist=[["A", 25], ["B", 30], ["C", 40]]
for i in [0,1,2]: #iに0から2の数字を入れる。range(0,3)でもOK!
    #print(stafflist[i]) #stafflistにi(0〜2)をそれぞれ入れる。["A", 25], ["B", 30], ["C", 40]がそれぞれ返る
    for j in [0,1]:
        print(stafflist[i][j]) #リスト名[リストのインデックス][要素として代入されていたリストのインデックス]

