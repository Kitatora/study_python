# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

# m=1~12の値。d=1〜31の値　例（11　1の組み合わせ。5 12の組み合わせ）

m, d = input().split()
num = list(m+d)　#option-1なら["1", "1", "1"]
if (all(num[0] == x for x in num)): 
# for x in numでxに1をlistの要素数分代入する。 
#num=[0]つまり1に一致し続けるか確認する。
    print("Yes")
else:
    print("No")