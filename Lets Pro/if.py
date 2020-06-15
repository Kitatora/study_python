#encoding=utf-8

age = 18
print("年齢は" + str(age) + "です。")

if age < 20:
    print("お酒は20歳から")
else:
    print("毎度ありがとうございます")


#郵便番号から住所を導く
postcode = "125-0062"
print("郵便番号は " + postcode + " です。")

if postcode == "140-0015":
    address = "東京都品川区西大井"
elif postcode == "102-0072":
    address = "東京都千代田区飯田橋"
elif postcode == "125-0062":
    address = "東京都葛飾区青戸"
else:
    address = "不明"

print("住所は " + address + " です。")

print("¥n")

postcode = "102-0072"
print("郵便番号は " + postcode + " です。")

if postcode == "140-0015":
    address = "東京都品川区西大井"
elif postcode == "102-0072":
    address = "東京都千代田区飯田橋"
elif postcode == "125-0062":
    address = "東京都葛飾区青戸"
else:
    address = "不明"

print("住所は" + address + "です。")