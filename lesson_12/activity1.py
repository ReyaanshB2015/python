string=input("enter ur string :")
char=input("enter the char ur looking for in the string u entered :")
i=0
count=0
while i<len(string):
    if string [i]==char:
        count=count+1
    i=i+1
print("the total number of times ",char," has occured ",count)