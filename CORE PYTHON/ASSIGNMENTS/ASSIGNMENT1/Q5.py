# Program to calculate the compound interest

p=float(input("Enter the principal amount ="))
t=float(input("Enter the time (years) = "))
r=float(input("Enter the rate of interest (%) ="))

ci= p *(( 1 + r / 100 ) ** t ) - p

print("Compound interest = ",ci)

