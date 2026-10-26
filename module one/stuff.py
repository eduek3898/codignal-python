Weight = input("weight: ")
unit = input("(K)g or (L)bs: ")
if unit == "K":
    print("Weight in bs: ", float(Weight) * 2.20462)
elif unit == "L":
    print("Weight in kg: ", float(Weight) / 2.20462)