def check_nested():
    condition1=True
    condition2=True
    if condition1:
        if condition2:
            print("Nested")
    print("Indentation error")
check_nested()            