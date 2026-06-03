def split_bill(bill,people):
    if people<0:
        print("Invalid input!!")
    else:
        return people//bill  
people=1250
bill=4
print("Each person pays: ",split_bill(bill,people))      