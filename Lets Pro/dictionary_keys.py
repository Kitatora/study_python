#encoding:utf-8

#辞書に含まれる値とkeyを全て取り出す。
#仕組み：dict.keys()メソッドを使う
sampledict = {"A":"a", "B":"b", "C":"c"}
print(sampledict.keys())
#dict_keys(['A', 'B', 'C']) keys()はdict_keys()の形で返す。keysをそれぞれ返す。

#応用：キーを縦に一つずつ並べる
sampledict = {"A":"a", "B":"b", "C":"c"}
for key in sampledict.keys(): #各種キーを入手
    print(key) #forでkeyを一つずつ縦に並べる


# 値を得る
# 仕組み：dict.values()メソッドを使う
sampledict = {"A":"a", "B":"b", "C":"c"}
print(sampledict.values())

#応用：値を縦に一つずつ並べる
sampledict = {"A":"a", "B":"b", "C":"c"}
for value in sampledict.values(): #各種値を入手
    print(value) #forでkeyを一つずつ縦に並べる

# キーと値を得る
# 仕組み：dict.items()メソッドを使う
sampledict = {"A":"a", "B":"b", "C":"c"}
print(sampledict.items())

#応用：値を縦に一つずつ並べる
sampledict = {"A":"a", "B":"b", "C":"c"}
for item in sampledict.items(): #各種値を入手
    print(item) #forでitemsを一つずつ縦に