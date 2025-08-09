var=int(input("enter ur number "))
rem=" "
r=0
while var>1:
    r=int(var%2)
    rem=str(r)+rem
    var=var/2
rem=str(int(var))+rem
print("the binary number is ",rem)