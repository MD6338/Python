print("Enter your age:")
age = int(input())

if age>18 and age<=100:
    print("You can drive")
elif age == 18:
    print("Padhai kar ek sal ruk")
else:
    print("You can't drive")

l = [10, 14, 15]

# if 158 in l:
#     print("Exists in list")
# else:
#     print("Don't exists in list")

if 14 not in l:
    print("Don't Exists in list")
else:
    print("Exists in list")