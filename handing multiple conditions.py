
country = input("What is your country? ").capitalize()

tax = 0
if country == "Canada":
    province = input("What is your province? ").capitalize()
    if province in ("Alberta", "Nunavut", "Yukon"):
        tax = 0.05

    elif province == "Ontario":
        tax = 0.13
    else:
        tax = .15
    print("Your province tax rate is: ", tax)

else:
    print("You don not need to pay tax!")
