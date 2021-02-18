#create a multiplication table for numbers 1 through 10

start = 1
end = 10
print("%3s" % " ", " | ", end="")
for columns in range(start, end + 1):
    print("%4s" % columns, end="")
print(end="\n")
print("---" * 16)

rows = 1

for a in range(start, end + 1):
    print("%3s" % rows, " | ", end="")
    for b in range(start, end + 1):
        print("%4s" % (a * b), end="")
    print(end="\n")
    a += 1
    rows += 1


