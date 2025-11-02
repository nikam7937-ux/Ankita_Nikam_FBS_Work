#Program to find sum of three digit number
num = int(input("Enter 3-digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

sum = c + b + a
print("Sum of digits =", sum)

