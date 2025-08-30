try:
    number=int(input("enter ur number "))
    print("the number is ",number)
except ValueError as ex:
    print("the exception is: ",ex)