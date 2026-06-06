try:
    x = int(input("Enter number"))
    y = 10/x
    print(y)
except ZeroDivisionError as e:
    print(e)
    
print("ABCD")