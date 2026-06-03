def try_except(a,b):
    try:
        result=a/b
        print("Result: ",result)
    except ZeroDivisionError:
        print("Cannot divide by zero")
try_except(10,0)            