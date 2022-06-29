import datetime


def is_week_day(day):
    if day.weekday() == 5 or day.weekday() == 6:
        return False
    return True

def main():
    my_date = datetime.date(2022, 6, 25)
    if is_week_day(my_date):
        print("Today is {}, are you ready to work?". format(my_date))
    else:
        print("just rest")

main()

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
nel = []
for i in a:
    nel1 = []
    for j in i:
        nel1.append(j**2)
    nel.append(nel1)
print(nel)
print(zip(nel))

b = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
new = [[x**2 for x in i] for i in b]
print(new)