def dayOfYear(date: str) -> int:
    dates = date.split(sep='-')
    days_dict = {'01': 0, '02': 31, '03': 59, '04': 90, '05': 120,
                 '06': 151, '07': 181, '08': 212, '09': 243,
                 '10': 273, '11': 304, '12': 334}
    month = dates[1]
    res = days_dict[month]+int(dates[2])
    if month == '01' or month == '02':
        return res
    year = int(dates[0])
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return res + 1
    return res


if __name__ == '__main__':
    print(dayOfYear("2019-01-09"))
    print(dayOfYear("2019-02-10"))
    print(dayOfYear("2003-03-01"))
    print(dayOfYear("2004-03-01"))
