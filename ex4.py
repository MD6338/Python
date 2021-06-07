# Pattern

# For true
# *
# **
# ***
# ****

# For false
# ****
# ***
# **
# *

print("Enter a number :")
n = int(input())
print("Enter 1 or 0")
n2 = bool(int(input()))

if n2 == True:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()


else:
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()