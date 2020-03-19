print("\U0001F49C")

#****************** To take any input **********
#user_input=input("Enter any input ")
#print("You just entered"+" "+user_input)
#user_age=int(input("\nEnter your age :"))
#print(user_input+" "+"I got your age i.e."+" "+str(user_age))


#---------two or more inputs in one line-------------
#name,age=input("Enter your name and age").split()
#print("Your entered name and age is "+name+" "+age)

#---------string formatting------------

#name,age=input("Enter your name and age").split()
#print(f"your name is {name} and age is {age}")
#print(r"your name is "+name+" your age is"+age)

#-------------print average of three numbers using string formatting---
one_mark,two_mark,three_mark=input("Enter three values ").split(",")
avg=(int(one_mark)+int(two_mark)+int(three_mark))/3
print(f"Average of three numbers you entered is {avg}")

