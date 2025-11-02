#Program to convert distance given in feet and inches into meter and centimeter
feet = float(input("Enter feet: "))
inch = float(input("Enter inches: "))

meters = feet * 0.3048
centimeters = inch * 2.54

print("Distance in meters =", meters)
print("Distance in centimeters =", centimeters)
