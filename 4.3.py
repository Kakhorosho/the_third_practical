x, y, n = map(int, input().split())
numner_of_rbls = x*n + int(y*n/100)
numner_of_penny = y*n % 100
print(numner_of_rbls, 'руб.', numner_of_penny, 'коп.')

