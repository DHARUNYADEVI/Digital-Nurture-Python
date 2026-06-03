def convert_weight():
    kg=float(input("Enter weight in kg: "))
    if kg<=0:
        print("Invalid weight")
        return 
    lbs=kg*2.20462
    print(f"Weight in pounds: {lbs:.2f}")
convert_weight()