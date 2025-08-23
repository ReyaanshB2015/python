def calc(bill_amount,perc_amount):
    total=bill_amount*(1+0.01*perc_amount)
    total=round(total,2)
    print("please pay $",total)
calc(100,20)