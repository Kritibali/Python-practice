user_input=int(input("Enter the no. upto which you want to see the sum of :"))
total=0
i=1
while(i<=user_input):
    total=i+total;
    i+=1;

print(f"Sum become of {user_input} is {total}")

# -------ask user for an input and make sum of the numbers
kb=input("Enter any input of not less than 2 digits")
length=len(kb)
i=0
total=0
while(i<length):
    total=total+int(kb[i])
    i+=1
print(f"Sum of the numbers you entered is {total}")

#-------------count of each character--------------
name=input("enter your name :")
i=0
while(i<len(name)):
     print(f"{name[i]}:{name.count(name[i])}")
     i+=1
