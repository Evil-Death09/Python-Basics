'''WAP that calculates your number of days left until the user nesxt birthday based on the current date. '''

from datetime import date

current_date = date.today()
print("Today is: ",current_date)

birth_day = int(input("Enter your birth day: "))
birth_month = int(input("Enter your birth month: "))

next_birthday = date(current_date.year,birth_month,birth_day)
print("Your next birthday is: ",next_birthday)

if next_birthday == current_date:
    print("Happy Birthday!!!")

elif next_birthday < current_date:
    next_birthday = date(current_date.year +1,birth_month,birth_day)
    days_left = (next_birthday - current_date).days
    print(f"{days_left} days left for your bithday...")
    print("Happy Birthday in advance..")

else:
    days_left = (next_birthday - current_date).days
    print(f"{days_left} days left for your bithday")
    print("Happy Birthday in advance..")



