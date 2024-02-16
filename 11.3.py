import math


a, b, c = map(int, input().split())
bac = math.acos((c**2 + b**2 - a**2)/(2*c*b)) / math.pi * 180
abc = math.acos((c**2 - b**2 + a**2)/(2*c*a)) / math.pi * 180
bca = math.acos((-c**2 + b**2 + a**2)/(2*b*a)) / math.pi * 180
print(bac, abc, bca, sep='\n')