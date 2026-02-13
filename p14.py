##write a program to input a number and display whether number is prime or not between 1 to 100

num = int(input("Enter a number between 1 and 100: "))

if num < 1 or num > 100:
    print("Please enter a number between 1 and 100.")
elif num == 1:
    print("1 is not a prime number.")
else:
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
