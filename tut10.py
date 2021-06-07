i = 1

# while(True):
#     print(i,end=" ")
#     if(i==13):
#         break
#     i = i + 1

while(True):
    if i<=6:
        i = i + 1
        continue
    print(i,end=" ")
    if(i==13):
        break
    i = i + 1


# Quiz
while(True):
    n = int(input("\nEnter a number :\n"))
    if n < 100:
        print("Please enter number more than 100")
        continue
    else:
        print("Congarts you have entered number greater than 100")
        break
