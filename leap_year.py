def is_leap(year):
    leap = False
    
    if year%4 == 0 and year/100 == 4 and year/400 ==4:
        leap = True
    return leap

year = int(raw_input())
