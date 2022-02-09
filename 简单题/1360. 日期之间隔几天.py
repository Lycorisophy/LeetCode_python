def dayOfTheWeek(day: int, month: int, year: int) -> str:
    pass_four, else_four = divmod(year - 1971, 4)
    pass_day = pass_four * 1461 + 365 * else_four
    if else_four > 1:
        pass_day += 1
    elif else_four == 1 and month > 2 and year != 2100:
        pass_day += 1
    pass_day += [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334][month] + day
    return ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", ][pass_day % 7]


def is_runnian(year: int):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def dayOfYear(dates: [int]) -> int:
    days_dict = {'01': 0, '02': 31, '03': 59, '04': 90, '05': 120,
                 '06': 151, '07': 181, '08': 212, '09': 243,
                 '10': 273, '11': 304, '12': 334}
    month = dates[1]
    res = days_dict[month]+int(dates[2])
    if month == '01' or month == '02':
        return res
    year = int(dates[0])
    if is_runnian(year):
        return res + 1
    return res


def passday(dates: [int]) -> int:
    year, month, day = dates
    pass_four, else_four = divmod(year - 1971, 4)
    pass_day = pass_four * 1461 + 365 * else_four
    if else_four > 1:
        pass_day += 1
    elif else_four == 1 and month > 2 and year != 2100:
        pass_day += 1
    return pass_day + [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334][month] + day


def daysBetweenDates(date1: str, date2: str) -> int:
    def passday(dates: [int]) -> int:
        year, month, day = dates
        year, month, day = int(year), int(month), int(day)
        pass_four, else_four = divmod(year - 1971, 4)
        pass_day = pass_four * 1461 + 365 * else_four
        if else_four > 1:
            pass_day += 1
        elif else_four == 1 and month > 2 and year != 2100:
            pass_day += 1
        return pass_day + [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334][month] + day
    return abs(passday(date1.split(sep='-')) - passday(date2.split(sep='-')))


if __name__ == '__main__':
    print(daysBetweenDates("2019-06-29", date2 = "2019-06-30"))
    print(daysBetweenDates("2020-01-15", date2 = "2019-12-31"))


