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

def inc(n):
    n.append(4)

l = [1, 2]
inc(l)
print(l)
