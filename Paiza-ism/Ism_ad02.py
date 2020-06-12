#encoding:utf-8
def test_func(*args):
    print(args)

test_func(1,2,3,4,5)
#引数名の前に「*」を付与することで可変長引数となる。アスタリスクは一つもしくは二つ。
#慣例としてargsもしくはkwargsと書くが、省略してアスタリスクのみでも良い
#可変長引数を設定すると、任意の数の引数を設定できる。

def my_sum(*args):
    return sum(args)
print(my_sum(1, 2, 3, 4))
# 10
print(my_sum(1, 2, 3, 4, 5, 6, 7, 8))
# 36