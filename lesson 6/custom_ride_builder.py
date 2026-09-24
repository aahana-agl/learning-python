print("custom ride builder")
print("STEP 1) pick your vehicle")
print("1. bike")
print("2. car")
print("\n\n")
choice = int(input("enter the options in either 1 or 2"))

if choice == 1:
    print("STEP2) pick yor bike type")
    print(" 1 - moutain bike")
    print(" 2 - bullet bike")
    print()

    bike_type = int(input(" again can you enter the options in either 1 or 2"))
    if bike_type == 1:
        print(" Good choice!, you have selected the moutain bike!")

    else:
        print(" Good choice!, you have selected the bullet bike")
elif choice == 2:
    print("STEP2) pick yor Car type")
    print(" 1 - Tesla(any)")
    print(" 2 - BMW(any)")
    print()

    car_type = int(input(" again can you enter the options in either 1 or 2"))
    if car_type == 1:
        print(" Good choice!, you have selected the tesla!")
    
    else:
        print(" Good choice!, you have selected the BMW!")
    