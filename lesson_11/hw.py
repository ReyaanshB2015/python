digit=int(input("enter ur number "))
counter=1
while digit>=10 :
    counter=counter+1
    digit=digit/10
    print("digit",digit,"::",counter)
print("number of digit is ",counter)