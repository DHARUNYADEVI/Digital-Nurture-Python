def login(user,pwd):
    if user!="":
        if pwd!="":
            if user=="admin" and pwd=="pass123":
               print("Login successfully")
            else:
                print("Invalid credentials")
        else:
            print("Password is Empty")
    else:
        print("Username is empty") 
user="admin"
pwd="pass123"
login(user,pwd)                       