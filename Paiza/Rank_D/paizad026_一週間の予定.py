#encoding:utf-8

d_1 = input()
d_2 = input()
d_3 = input()
d_4 = input()
d_5 = input()
d_6 = input()
d_7 = input() #変数を一つ一つ代入してるのがブサイクだと思う
l = [d_1, d_2, d_3, d_4, d_5, d_6, d_7] #リスト化をforを使ってもっとスムーズに作成できないか？
Nos = l.count("no")
print(Nos)

#Option-1
l = []
for i in range(6): 
    l.append(input())
nos = l.count("no")
print(nos) #変数は小文字で

#Option-2 与えられたデータが何行かわからない場合
l = []
n = True
while n == True:
    try:
        l.append(input())
    except:
        n = False
nos = l.count("no")
print(nos)