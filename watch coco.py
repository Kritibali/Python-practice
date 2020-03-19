name,age=input("Enter your name and age comma separated :").split(",")
if((name[0]=='a' or name[0]=='A') and int(age)>=10):
    print("You can watch the movie coco")
else:
    print("Sorry you can't watch this movie.")
