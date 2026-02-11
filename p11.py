##Write a program to type a number and display factorial of that number. For example, factorial of 5=5*4*3*2*1=120
n=int(input("Enter no: "))
f=1
for i in range(1,n+1):
    f=f*i
print(f)
