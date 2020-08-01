
a, op, b, d, c = map(str, input().split())

if a == "x":
    if op == "+":
        print(int(c) - int(b))
    elif op == "-":
        print(int(c) + int(b))
elif b == "x":
    if op == "+":
        print(int(c) - int(a))
    elif op == "-":
        print(int(a) - int(c))
elif c == "x":
    if op == "+":
        print(int(a) + int(b))
    elif op == "-":
        print(int(a) - int(b))