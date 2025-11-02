# Program to convert days into years,weeks and days
days = int(input("Enter the number days = "))
year = days//365
remaining_days = days % 365

week = remaining_days // 7
day_left = remaining_days % 7

print (f"{days} days = {year} years , {week} weeks , {day_left} days")
