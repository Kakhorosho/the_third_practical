a = int(input())
a = str(a)
if len(a) > 7:
    a = int(a)
    b = a % 1000 // 100
    print(b)
else:
    print('it is not a bitcoin')