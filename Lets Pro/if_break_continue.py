#encoding:utf-8

for val in [3, "ab", 7]:
    if isinstance(val, int):
        continue #continueにより繰り返されるのはfor文。インデントに注目。if文が真の時のみ、5行目が実行される
    print("val = " + str(val))

print("End")

#  1) 変数 val にリストから要素を1つ代入 (val は 3)
#  2) if の条件式で val のデータ型が文字列型か調べる --> 偽。continueは実行されず、6行が行われる。
#  3) 変数 val の値を出力。6行目が実行。
#  4) 変数 val にリストから要素を1つ代入 (val は "ab")
#  5) if の条件式で val のデータ型が文字列型か調べる --> 真
#  6) ブロック内の残りの文はスキップ
#  7) 変数 val にリストから要素を1つ代入 (val は 7)
#  8) if の条件式で val のデータ型が文字列型か調べる --> 偽
#  9) 変数 val の値を出力
# 10) "End" を出力