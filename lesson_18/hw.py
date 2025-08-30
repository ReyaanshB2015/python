try:
    age=int(input("enter ur age "))
    print("age is ",age)
except ValueError as ex:
    print("it is not a valid age")
if age%2==1:
    print("the age is odd")
else:
    print("the age is even")