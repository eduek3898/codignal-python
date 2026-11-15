a = int(input("Enter a value: "))
b = int(input("Enter a value: "))
c = int(input("Enter a value: "))
avg = (a + b + c) / 3
print("Avg = ", avg)
if avg> a and avg > b and avg > c:
    print("Average is greater than all three numbers: %d" %(avg))
elif avg > a and avg > b:
    print("Average is greater than a and b: %d" %(avg))
elif avg > a and avg > c:
    print("Average is greater than a and c: %d" %(avg))
elif avg > b and avg > c:
    print("Average is greater than b and c: %d" %(avg))
elif avg > a:
    print("Average is greater than just a: %d" %(avg))
elif avg > b:
    print("Average is greater than just b: %d" %(avg))
elif avg > c:
    print("Average is greater than just c: %d" %(avg))
else:
    print("invalid input")