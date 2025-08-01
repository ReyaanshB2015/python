unit=int(input("enter ur unit "))
if unit<=50:
    amount=2.60*unit+25
elif unit>50 and unit<=100:
    amount=130+3.25*(unit-50)+35
elif unit>100 and unit<=200:
    amount=130+162.50+5.26*(unit-100)+45
else:
    amount=130+162.50+526+8.45*(unit-200)+75
print("u have to pay",amount)