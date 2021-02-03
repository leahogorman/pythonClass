currentTempC = input("What is the current temperature in Celsius")
currentTempF = 9/5 * float(currentTempC) + 32
print(currentTempF)

newTempF = input("What is the current temperature in Fahrenheit")
newTempC = (float(newTempF) - 32) / (9/5)
print(newTempC)

firstName = input("Enter your First Name")
lastName = input("Enter your Last Name")
firstNameUpper = firstName.upper()
lastNameUpper = lastName.upper()

print("your first and last initials are {} . {} .".format(firstNameUpper[0], lastNameUpper[0]), end="")
print("the temperature outside is {} degrees Fahrenheit and {} degrees Celsius".format(currentTempF, currentTempC))