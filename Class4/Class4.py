a = 1
b = 100
for c in range (a,b + 1):
    if c%2==0:
        print(c)

size = int(input("How big would you like the square "))
for y in range(0, size):
    for x in range(0, size):
        print("*", end="")
    print()

size = int(input("How big would you like the square "))
for x in range(0, size):
    print("*" * size)


size = int(input("How big would you like the triangle "))
for a in range(0, size + 1):
    print("*" * a)
    a += 1

colours = ["red", "green", "blue", "yellow"]
prime_numbers = [2, 3, 5, 7, 9, 11, 19]
for c in colours:
    print(c)