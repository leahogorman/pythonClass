# a = input("what is your name?")
# if len(a) > 6:
#     if len(a) < 10:
#         print("Your name is greater than 6 characters, but less than than 10 characters. Your name is {} characters".format(len(a)))
#     else:
#         print("Your name is greater than than 10 characters. Your name is {} characters".format(len(a)))
# elif len(a) == 6:
#     print("Your name is {} characters".format(len(a)))
# else:
#     print("Your name is less than than 6 characters. Your name is {} characters".format(len(a)))

# a = 0
# while a <5:
#     print("#" * 5)
#     a += 1


# sum = 0
# value = ""
# while True:
#     value = int(input("please enter an integer"))
#     if sum < 34:
#         sum = sum + value
#     else:
#         print("exit your total is {}".format(sum))
#         break

value = ""
while True:
    value = input("please enter an integer")
    if value.upper() == "Q":
        print("quit")
        break
    elif int(value) % 10 == 0:
        print("{} is a multiple of 10".format(value))
    else:
        print("{} is not a multiple of 10".format(value))
