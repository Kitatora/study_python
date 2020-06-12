#encoding:utf-8

print("python")
print("-")
print("izm")
print("com")
#引数の値を指定された出力先へ出力する。"標準出力である"sys.stdoutがデフォルト尾出力先。
#子めんどプロンプトで実行した場合は、コマンドプロンmんぷとのコンソールへ出力。
#デフォルトでは開業(\n)付与されている

#出力先を一時的にファイルへ変更する場合、Python3系ではfile 引数へ出力先となるファイルオブジェクトを渡す。
f_obj = open("test.txt","w")
print("python-izm.com", file = f_obj)

#フォーマット出力。文字列、数値などを交えて出力を行ってみる。
print("Pythonの学習サイト: %s" % "Python-izm.com")
print("Pythonの学習サイト: %s-%s.%s" % ("python", "izm", "com"))

test_int = 100 + 100
test_str = "python-ism.com"
print("サイト回折 %d 日目! %s" % (test_int, test_str))