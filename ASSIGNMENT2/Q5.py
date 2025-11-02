#Program to calculate the selling price of book based on cost price and discount
cp = float(input("Enter Cost Price: "))
discount = float(input("Enter Discount %: "))

sp = cp - (cp * discount / 100)
print("Selling Price of the book =", sp)
