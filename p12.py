##write a program to input a number and display whether number is prime or not

n=int(input("Enter no: "))
for i in range(2,n):
    if n%i==0:
        print("no is not prime")
        break
    else:
        print("no is prime")
        break
