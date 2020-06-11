#encoding:utf-8

for value in "ABCDEF":
    print(value)

samplelist = []
samplelist.append("あ")
samplelist.append("い")
samplelist.append("う")
samplelist.append("え")
samplelist.append("お")

for value in samplelist:
    print(value)

testlist = [["alpha", "beta"], ["gamma", "sigma"]]
for value in testlist:
    print(value)

for value_1, value_2 in testlist:
    print(value_1, value_2)