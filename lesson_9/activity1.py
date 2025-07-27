a=int(input("show your attendance "))
mc=input("do u have a medical cause: y or n ")
if mc=="y":
    print("u can enter")
else:
    if a>=75:
        print("u can enter aswell")
    else:
        print("u cannot participate in the exam")
