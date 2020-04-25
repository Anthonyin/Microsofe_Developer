price = input("How much did you pay?")
price = float(price)
if price >= 1.00:
    tax = 0.07
else:
    tax = 0
print("Tax rate is: {}".format(str(tax)))

country = input("Enter the name of your home country: ").lower()
if country == "canada":
    print("So you much like Hockey!")
else:
    print("You are not from Canada")