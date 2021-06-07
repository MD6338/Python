n = input("Enter a number :\n")
n2 = input("Enter a number :\n")

try:
    print("Addition is ",int(n)+int(n2))
except Exception as e:
    print(e)


print("Exception Handling Successfully implemented")