weight = float(input("Weight: "))

units = input("(K)g or (L)bs: ")

if units.upper() == 'K':
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
elif units.upper() == 'L':
    converted = weight * 0.45
    print("Weight in Kg: " + str(converted))