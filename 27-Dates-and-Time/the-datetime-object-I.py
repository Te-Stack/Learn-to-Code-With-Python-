from datetime import datetime 

print(datetime(1999,7,24))
print(datetime(1999,7,24,12,17,58))


today = datetime.today()
print(today)
print(datetime.now())

print(today.weekday())

same_time_twenty_years_ago = today.replace(year = 1999)
print(same_time_twenty_years_ago)

start_of_january_1999 = today.replace(1999,1,1)
print(start_of_january_1999)

