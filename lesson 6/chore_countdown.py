total_chores = 4
completed = 0
chore_num = 1

while chore_num <= total_chores:
    if chore_num == 1: chore = "make your bed"
    elif chore_num == 2: chore = "clean your room"
    elif chore_num == 3: chore = "brush your teeth"
    else: chore = "complete your homework if you have any"
    answer = input(f"finished {chore}? (yes/no)")

    if answer == "yes":
        completed += 1
        chore_num += 1
        print("great job, keep it up!")

    else:
        print("finish it and try again!")

    print("chores remaning",total_chores - completed)

print("all chores complete good job!")