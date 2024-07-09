# Exception handling
try:
    a=10
    b='10'
    c=a+b
    print(8/0)
except ZeroDivisionError as err:
    print("Please don't provide 0 in the denomenator")
    print(err)
except TypeError as err:
    print("Error occurs while exception because you are providing string instead of int")
    print(err)
