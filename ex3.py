n = 18
# guesses - 9
gusses = 1
while(gusses<=9):
    inp = int(input("Enter a number \n"))
    if inp < 18:
        print("You entered lesser number please input greater number")
    elif inp > 18:
        print("You entered greater number please input lesser number")
    else:
        print("You won the game")
        print("You took", gusses, "guesses")
        break
    print("Number of gusses left", 9-gusses)
    gusses += 1

if gusses > 9:
    print("You lost")