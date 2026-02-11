##write a program to input a number and display whether number is prime or not between 1 to 100

num=int(input("Enter no: "))
flag=0
for i in range(2,num):
    if num%i==0:
        flag = 1
        break
    if flag == 1:
        print("not prime")
    else:
        print("prime")
