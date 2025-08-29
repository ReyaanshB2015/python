def calculate(billamount,paidamount):
    a=billamount-paidamount
    return a
billamount=float(input("enter ur bill amount "))
paidamount=float(input("enter ur paid amount "))
restamount=calculate(billamount,paidamount)
print("you have to pay ",restamount)