import datetime

i = datetime.date.today()
today = i.year

birthday = input("enter your birthday: ")
splited_b = birthday.split("/")

if int(splited_b[1]) > 12 or int(splited_b[2]) > 31:
    print("WRONG")
else:
    print(today - int(splited_b[0]) )