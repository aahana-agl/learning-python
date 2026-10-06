# Part 1
print("🗽This is the School club member badge🏫")
name = input("Enter your name: ")
club = input("Enter your club name: ")

# Part 2
member_number = 8
points = 9.5
is_active = True
print(type(member_number), type(points), type(is_active))

# Part 3
badge_code = name[0:3] + club[-1] + str(member_number)
print(badge_code)

# Part 4
print("===== CLUB BADGE =====")
print("Member: " + name)
print("Club: " + club)
print("Code: " + badge_code)
print("Points: " + str(points) + " | Active: " + str(is_active))