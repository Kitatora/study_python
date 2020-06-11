#encoding:utf-8

import sys

args = sys.argv

print(args)
print("第一引数"+args[1])
print("第二引数"+args[2])
print("第三引数"+args[3])
#6行目のsys.argvに起動時に設定した引数が格納される。リストで値が返されるが、最初の要素には実行ファイルが入る