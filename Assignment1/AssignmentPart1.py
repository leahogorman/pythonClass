# Print "a" in range of 0 to 25
# where multiples of 3 are replaced by "Fizz"
# multiples of 5 are replaced by "Buzz"
# and multiples of both are replaced by "Fizz Buzz"

start = 0
end = 25

for a in range(start, end + 1):
    if a % 5 == 0 and a % 3 == 0:
        print(a, ": Fizz Buzz")
    elif a % 3 == 0:
        print(a, ": Fizz")
    elif a % 5 == 0:
        print(a, ": Buzz")
    else:
        print(a)
