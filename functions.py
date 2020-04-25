from datetime import datetime


#
# first_name = "Susan"
# print("task completed")
# print(datetime.datetime.now())
# print()
#
# for x in range(0,10):
#     print(x)
# print("Tast completed")
# print(datetime.datetime.now())
# print()

# def print_time():
#     print("tast completed")
#     print(datetime.now())
#     print()
#
#
# first_name = "Susan"
# print_time()
#
# for x in range(0, 10):
#     print(x)
# print_time()
#
# first_name = "Susan"
# print("first name assigned")
# print(datetime.now())
# print()
#
# for x in range(0,10):
#     print(x)
# print("Loop completed")
# print(datetime.now)
# print()

def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()


first_name = "Susan"
print_time("First name assigned")

for x in range(0, 10):
    print(x)
print_time("Loop completed")

first_name = input("Enter your first name: ")
first_name_initial = first_name[0:1]
last_name = input("Enter your last name: ")
last_name_initial = last_name[0:1]

print("Your initials are: " + first_name_initial + last_name_initial)


def get_initial(name):
    initial = name[0:1].upper()
    return initial


first_name = input("Enter your first name: ")
first_name_initial = get_initial(first_name)

last_name = input("Enter your last name: ")
last_name_initial = get_initial(last_name)

print("Your initials are: " + first_name_initial + last_name_initial)
print("Your initials are: " + get_initial(first_name) + get_initial(last_name))
