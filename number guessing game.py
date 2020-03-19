winning_no=17
guessed_no=int(input("Enter any number :"))
if(guessed_no==winning_no):
    print("You got it right !")
else:
    if(guessed_no<winning_no):
        print("Two low !!")
    else:
        print("Too high")
