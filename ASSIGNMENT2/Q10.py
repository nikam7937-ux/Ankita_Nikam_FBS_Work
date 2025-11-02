#Program to reverse 3 digit numbers
num = int(input("Enter 3-digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

rev = c*100 + b*10 + a
print("Reverse number =", rev)

num = int(input("Enter 2-digit number: "))

a = num // 10
#b = (num // 10) % 10
c = num / 1

rev = c*10 + a
print("Reverse number =", rev)