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


s1 = "Best School"
print(id(s1))
s2 = "Best School"
print(id(s2))
print(s1 is s2)
