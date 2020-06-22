#encoding:utf-8
sample = {"a":[1,2,3,4,5], "b":[6,7,8,9,10]}
print(type(sample))
#print(sample("b"))
#実行結果：TypeError: 'dict' object is not callable
print(sample["b"][3])
print(sample["a"][1:3])

sample = {"c":[10,11,12,13], "d":[14,15,16,17,18]}
sample["e"] = [19, 20]
print(sample)