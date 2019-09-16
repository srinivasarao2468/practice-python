name = input("enter your name: ")

print("welcome")

print("Hey ", name)

flag = True

while flag == True:
    date = int(input("Enter the date: "))
    if date>0 and date<=31:
        print("perfect {}".format(date))
        flag = False
    else:
        print("Entered Wrong date!!!!!")

flag = True

while flag == True:
    month = int(input("Enter the month: "))
    if month>0 and month<=12:
        print("perfect {}".format(month))
        flag = False
    else:
        print("Entered Wrong month!!!!!")

flag = True

while flag == True:
    year = int(input("Enter the year: "))
    if year>1900 and year<=2001:
        print("perfect {}".format(year))
        flag = False
    else:
        print("Entered Wrong year!!!!!")
