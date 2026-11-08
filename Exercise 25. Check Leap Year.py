leap_years = []
for year in range(1, 3000):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year} is a leap year")
        leap_years.append(year)
    else:
        pass