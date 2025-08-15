r=int(input("enter the number of rows :"))
for i in range(0,r+1,1):
    s=""
    c=""  
    print()
    for k in range(0,r-i,1):
        s=" "+s
      
    for j in range (0,i,1): 
        c=c+"*"   
    print(s,c)
