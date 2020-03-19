age=int(input("Enter your age :"))
if age>=1 and age<=3:
    print("Your ticket is free.")
elif(age>=4 and age<=10):
    print("Your ticket fee is 150 Rs.")
elif(age>=11 and age<=60):
    print("your ticket fee is 250 Rs.")
else:
    print("your ticket fee is 2000")
