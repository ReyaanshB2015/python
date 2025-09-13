a=int(input("enter the start value "))
b=int(input("enter the end value "))
empty_list=[]
for i in range(a,b+1):
    empty_list.append(i)
print("Original",empty_list)
square_list=[]
for i in empty_list:
    c=i*i
    square_list.append(c)
print("Square",square_list)
oddlist=[]
evenlist=[]
for i in square_list:
    if i%2==1:
        oddlist.append(i)
    else:
        evenlist.append(i)
print("oddlist",oddlist)
print("evenlist",evenlist)