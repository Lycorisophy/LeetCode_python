def dayOfTheWeek(day: int, month: int, year: int) -> str:
    pass_four, else_four = divmod(year - 1971, 4)
    pass_day = pass_four * 1461 + 365 * else_four
    if else_four > 1:
        pass_day += 1
    elif else_four == 1 and month > 2 and year != 2100:
        pass_day += 1
    pass_day += [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334][month] + day
    return ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", ][pass_day % 7]


if __name__ == '__main__':
    print(dayOfTheWeek(day=1, month=1, year=1971))
    print(dayOfTheWeek(day=31, month=8, year=2019))
    print(dayOfTheWeek(day=18, month=7, year=1999))
    print(dayOfTheWeek(day=15, month=8, year=1993))
