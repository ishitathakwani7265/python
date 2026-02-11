age=int(input("Enter age:"))
if age<12:
    print("You are a kid")
elif age>=12 and age<=17:
    print("You are teenager")
elif age>=18 and age<60:
    print("You are an adult")
elif age>=60:
    print("Senior citizen")
else:
    print("please enter valid choice")
