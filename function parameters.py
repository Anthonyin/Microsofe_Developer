def get_initial(name, force_uppercase=True):
    if force_upperc ase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


first_name = input("Enter your first name: ")
email_address = input("Enter your email address: ")

print("Your initial is: " + get_initial(first_name))
print("Your initial is: " + get_initial(name=first_name))