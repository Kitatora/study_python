# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

teams = int(input())
games = int(teams*(teams - 1)/2)
li1 = []
for i in range(games):
    li1.append(list(map(int, input().split())))
    
for i in range(teams):
    for j in range(teams):
        if i == j:
            print("-", end=" ")
        elif [i+1, j+1] in li1:
            print("W", end=" ")
        else:
            print("L", end=" ")
    print()

"""
11行目以降について
1. i=0とj=0を比較。同じ数字なので"-"を返す
2. 12行目をループ
3. li1中の[i+1(つまり1), j+1(つまり2)]を比較。li1に存在するので、Wを返す
4. 12行目をループ
5. li1中の[i+1(つまり1), j+1(つまり3)]を比較。li1に存在するので、Wを返す
6. 次は11行目をループ
以下、1〜6をくりかえす

入力値
3
1 3
2 1
2 3

出力
- L W
W - W
L L -
"""