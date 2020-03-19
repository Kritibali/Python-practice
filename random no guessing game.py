import random
actual_num=randint(1,100)
num=int(input("Enter any number from 1 to 100:"))
while(num!=actual_num):
    if(num==actual_num):
        print("You guesses it ! well done.")
    elif(num<actual_num):
        print("too low")
    else:
        print("too high")
        
