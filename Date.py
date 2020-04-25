from datetime import datetime, timedelta

current_date = datetime.now()
print("Day: " + str(current_date.day))
print("Month: ", str(current_date.month))
print("Year: ", str(current_date.year))

birthday = input("When is your birthday? (dd/mm/yy)")
birthday_date = datetime.strptime(birthday, '%d/%m/%y')
print("Birthday: "+str(birthday_date))
one_day = timedelta(days=5)
print(one_day)
birthday_eve = birthday_date - one_day
print("Day before birthday: " + str(birthday_eve))
birthday_days = current_date - birthday_date
print("Days of your birthday: " + str(birthday_days))


