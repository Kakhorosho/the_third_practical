ATT, COMP, YDS, TD, INT = map(int, input().split())
x = ((COMP/ATT) - 0.3)*5
y = ((YDS/ATT) - 3)/4
z = (TD/ATT)*20
w = 2.375 - ((INT/ATT) * 25)
print(x, y, z, w)
if x < 0 or y < 0 or z < 0 or w < 0:
    print('passer rating = 0')
else:
    if x > 2.375 or y > 2.375 or z > 2.375 or w > 2.375:
        print('passer rating = 2.375')
    else:
        passer_rating = (x + y + z + w)/6 * 100
        print(round(passer_rating, 2))
