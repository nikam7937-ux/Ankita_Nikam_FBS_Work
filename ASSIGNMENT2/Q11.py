
amt = int(input("Enter amount: "))

n1000 = amt // 1000
amt = amt % 1000
n500 = amt // 500
amt = amt % 500
n200 = amt // 200
amt = amt % 200
n100 = amt // 100
amt = amt % 100
n50 = amt // 50
amt = amt % 50
n20 = amt // 20
amt = amt % 20
n10 = amt // 10
amt = amt % 10

print("1000 =", n1000)
print("500  =", n500)
print("200  =", n200)
print("100  =", n100)
print("50   =", n50)
print("20   =", n20)
print("10   =", n10)
