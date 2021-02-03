import decimal

my_text = "this is a quote \" symbol"

my_text2 = 'this is a quote " symbol'

my_text3 = "this is a backslash \\"

my_text4 = "this is a \nbreak \nthis is a \t tab"

print("X" * 10)
print(my_text)
print(my_text2)
print(my_text3)
print(my_text4)

# line_length = input("What length is the line?")
# character = input("What character should I use")
# print(character * int(line_length))

my_name = "leah"
course_name = "Python"
print("My name is \" {} \" and I am taking {}".format(my_name, course_name))

print("Gas price is {0:2d}, and cost per litre is :{1:8.2f}".format(123, 00.564))

a = decimal.Decimal("10.45")


print(a + 6)
# len is length so it comes back with length of my_name
print(len(my_name))
# title will put the first character as uppercase
print(my_name.title())

print(my_name.strip())

print("X", end="")
print("Y")

s = "Hello"
# Substrings of Hello called String Slices in Python
print(s[1:4])
print(s[1:])
print(s[:])
print(s[1:50])
# third character from the left
print(s[-3])

g = 1

g = g + 1
g += 1
g -= 1
g *= 1
print(g)
print(5 % 2 == 0)

