 
print("Step 1: Pick your holiday type")
print("  1 - Beach Holiday")
print("  2 - Carinaval Holiday")
print()
 
choice = int(input("Enter 1 or 2: "))
print()
 
if choice == 1:
   
    print("Step 2: Pick your beach activity")
    print("  1 - Swimming")
    print("  2 - Sunbathing")
    print()
 
    beach_activity = int(input("Enter 1 or 2: "))
    print()
 
    if beach_activity == 1:
        print("You picked  : Swimming")
        print("Best time   : Morning")
        print("Remember to : Carry sunscreen and water so you dont get burnt")
    else:
        print("You picked  : Sunbathing")
        print("Best time   : Mostly when its sunny")
        print("Remember to : Carry a mat/chair to sit on and an umbrella")
 
elif choice == 2:
    print("Step 2: Pick your carnival activity")
    print("  1 - Play fun games")
    print("  2 - Go for cool rides")
    print()
 
    carnival_activity = int(input("Enter 1 or 2: "))
    print()
 
    if carnival_activity == 1:
        print("You picked  : Play fun games ")
        print("Best for    : Winning a prize")
        print("Remember to : not give up easily (I know it's hard) )")

    else:
        print("You picked  : Go for cool rides")
        print("Best for    : Enjoy the ride")
        print("Remember to : Not push yourself to go its your choice if you want to")