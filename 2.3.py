number = 86400
b = int(input())
if 1 < b <= 86400:
    number_of_hours = int(b/3600)
    number_of_minutes = int(b % 3600 / 60)
    number_of_seconds = int(b % 3600 % 60 / 60)
    print(number_of_hours, number_of_minutes, number_of_seconds, sep='.')
