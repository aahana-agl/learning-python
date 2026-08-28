#Fun School day Planner:)
print("Fun School day Planner:):0:D")
print("please can you write what day is it today(Monday-Friday):")
day = input("please can you write what day is it today(Monday-Friday").strip().capitalize()
#if,elif,else statements: clasify the day
if day in ("saturday","sunday"):
    print("it's the weekends have fun do something outside/inside")
elif day == ("monday"):
    print("back to school be ready (dont worry I understand how stressful it is):D )")
elif day == ("friday"):
    print("last day of school (yay!)")
    print("enjoy the rest of your weekend")
elif day in ("wednessday","thursday","tuesday"):
    print("ugggh still suffering school (good luck) ")
else:
    print("day not recognised >:( )")