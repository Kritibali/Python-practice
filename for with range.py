num=int(input("Enter any number :"))
total=0
for i in range(1,num+1):
    total=total+i
print(f"sum is{total}")


# sum of every digit
num=input("Enter any number :")
total=0
for i in range(0,len(num)):
    total=total+int(num[i])
print(f"Sum is {total}")


# count for every character
name=input("Enter any name :")
for i in range(0,len(name)):
    print(f"{name[i]} : {name.count(name[i])}")
