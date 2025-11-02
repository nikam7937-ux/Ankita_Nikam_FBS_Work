#Program to find the roots of quadratic equations
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = (b*b) - 4*a*c
x1 = (-b + d**0.5)/(a*a)
x2 = (-b - d**0.5)/(a*a)
print("Roots are:", x1, x2)
