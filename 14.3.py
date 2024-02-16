n = int(input())
if 0 <= n <= 360:
    number_of_hours = int(n/360 * 12)
    number_of_minutes = int(((n - number_of_hours*30)/360) * 60)
    print(number_of_hours)
    print(number_of_minutes)
