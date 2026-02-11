#4.write a program to add 5 subject marks and print result with grade.
m1=int(input("Enter marks of subject 1:"))
m2=int(input("Enter marks of subject 2:"))
m3=int(input("Enter marks of subject 3:"))
m4=int(input("Enter marks of subject 4:"))
m5=int(input("Enter marks of subject 5:"))
if(m1>=30 and m2>=30 and m3>=30 and m4>=30 and m5>=30):
    print("Pass")
    result=((m1+m2+m3+m4+m5)*100)/500
    print("result is:",result)
    if(result<100 and result>=90):
        print("Your grade is: A+")
    elif(result<90 and result>=80):
        print("Your grade is: A")
    elif(result<80 and result>=70):
        print("Your grade is: B+")
    elif(result<70 and result>=60):
        print("Your grade is: B")
    elif(result<60 and result>=50):
        print("Your grade is: C")
    elif(result<50 and result>=40):
        print("Your grade is: D")
else:
    print("Fail")

