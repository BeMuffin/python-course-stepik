from datetime import timedelta, date

year,month,day = input().split(' ')
add_date = int(input())

old_date = date(int(year),int(month),int(day))
new_date = old_date + timedelta(days=add_date)

print(f'{new_date.year} {new_date.month} {new_date.day}')

