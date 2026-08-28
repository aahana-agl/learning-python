temperature = int(input("Enter today's temperature in Celsius: "))
if temperature < 20:
    activity = "something inside"
    print("It is cool today.")
    print("you shold Do", activity)
else:
    activity = "somthing fun outside"
    print("It is warm today.")
    print("you sholud Do", activity)
 
# PART 3: Ask whether it is raining
is_raining = input("Is it raining today? (yes/no): ")
 
# PART 4: Add a rain reminder only if it is raining
if is_raining == "yes":
    print("Choose something to do inside (e.g uno, sequince, a board game) or bring an umbrella!")
 
# PART 5: Ask for the homework time
homework_time = int(input("Enter homework time in minutes: "))
 
# PART 6: Decide whether study break is needed
if homework_time >70:
    needs_break = "yes"
    print("You have a long homework session today.")
    print("Take a short break before you do", activity)
else:
    needs_break = "no"
    print("you have a decent amount of homework today.")
    print("if you want to take a short break but its not needed before you do", activity)
 
# PART 7: Ask whether there is free time
has_free_time = input("Do you have free time today? (yes/no): ")
 
# PART 8: Decide between hobby time and planning time
if has_free_time == "yes":
    hobbies = "fun time to spend in your hobbies"
    print("You have free time today.")
    print("Enjoy your", hobbies)
else:
    final_task = "planning time"
    print("You do not have much free time today.")
    print("Use some time for", final_task)
 
# PART 9: This message always prints, no matter what was chosen above
print("")
print("Daily activity check complete!")
 
# PART 10: Print the final activity summary
print("◑︿◐ (=θωθ=) (⊙ｏ⊙)  !!!!!!!!DAILY ACTIVITY PLANNER!!!!!!!!!  :0 :D :-) (⊙﹏⊙)")
print("Temperature:", temperature)
print("Activity Chosen:", activity)
print("Raining:", is_raining)
print("Study Break Needed:", needs_break)
print("Final Task:", final_task)
print("﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")