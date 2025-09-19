tuple1 = (1, 0, 0, 0, 1, 1, 0)
s = 0
r = 0

for i in range(0, 7):
    if tuple1[i] == 0:
        r =r+ 1
    else:
        s =s+ 1

if s > r:
    print("Sunny weather")
else:
    print("rainy weather")
