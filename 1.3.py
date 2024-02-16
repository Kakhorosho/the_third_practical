bitcoin = float(input())
bitcoin = int(bitcoin)
bitcoin = str(bitcoin)
if len(bitcoin) == 7:
    bitcoin = int(bitcoin)
    b = bitcoin % 1000 // 100
    print(b)
else:
    print('it is not a bitcoin')
