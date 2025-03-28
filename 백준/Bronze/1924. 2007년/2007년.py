x, y = map(int, input().split())

month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
count = 0
if x >1:
    for i in range(x-1): # 3-> 0,1,2
        count += month_day[i]
    count += y
else :
    count += y
    
if count%7 == 1:
    print('MON')
elif count%7==2:
    print("TUE")
elif count%7==3:
    print("WED")
elif count%7==4:
    print("THU")
elif count%7==5:
    print("FRI")
elif count%7==6:
    print("SAT")
else:
    print("SUN")