tuple1=(2,3,4,5,6,7,8)
a=len(tuple1)
print(a)
b=1
for i in range(0,a,1):
    b=b*tuple1[i]
    print(b)