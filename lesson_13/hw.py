rows=int(input("enter ur amount of rows "))
star=""
sp=""
for i in range(0,rows,1):
    star=""
    sp=""
    for k in range(rows-i):
        sp=sp+" "
    for j in range(0,i+1):
        star=star+"*"
    print(sp,star)
