# Variables
myAge = 14
iAm = "Chinmay Kulthe"
print("I am " + iAm + " years " + str(myAge) + " old")

# Type conversion
x = str(14)
y = int(14.963)
z = float(34)
print(x)
print(y)
print(z)

# Geting type of a variable
print(type(myAge))
print(type(iAm))

# Multiple values to multiple variables
lang1, lang2, lang3 = "C++","C","Python"
print(lang1)
print(lang2)
print(lang3)

# One value to multiple variables
a = b = c = "JavaScript"
print(a)
print(b)
print(c)
print(c)

# Taking Input From User
print("Enter two numbers :")
num1,num2 = int(input()), int(input())

# Variable Name Rules -
"""
- A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
"""