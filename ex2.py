# Faulty Calculator
# 45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4
print("Enter first number :")
inp = int(input())
print("Enter Operator :")
op = input()
print("Enter second number")
inp2 = int(input())
if inp == 45 and inp2 == 3 and op == "*":
    print("Answer - 555")
elif inp == 56 and inp2 == 9 and op == "+":
    print("Answer - 77")
elif inp == 56 and inp2 == 6 and op == "/":
    print("Answer - 4")
elif op == "+":
    print("Answer - ",str(inp + inp2)) 
elif op == "-":
    print("Answer - ",str(inp - inp2)) 
elif op == "/":
    print("Answer - ",str(inp / inp2)) 
elif op == "*":
    print("Answer - ",str(inp * inp2)) 