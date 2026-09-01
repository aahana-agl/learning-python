# Library Visit Planner-made by an 11yr old

print("=== Library Visit Planner ===")
print("Answer 3  easy and quick questions and I will plan your library visit :) !\n\n")

day       = input("What day is it? (Monday - Sunday): ").strip().capitalize()
weather   = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()
book_due  = input("Do you have a book to return? (yes / no): ").strip().lower()

print("\n\n")
print(f"=== Your Library Plan for {day} ===")
print("-" * 35)

# Topic 1 -- if-elif-else: classify the day
if day in ("Saturday", "Sunday"):
    print("Day type    : Its the weekend - a good time for a relaxed and nice library visit!(0-0)")
elif day == "Monday":
    print("Day type    : Start of the week. Check your what plans you have for today.")
elif day == "Friday":
    print("Day type    : Last school day - Rememeber to return your books before the weekend.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type    : Regular school day - If you can its better to plan a short library visit.")
else:
    print("Day type    : Day not recognised. Please check the spelling.")

if weather == "sunny" and book_due == "yes":
    print("Library tip : Great weather! Return your book and borrow a new one.\n")

if weather == "rainy" or weather == "cloudy":
    print("Weather tip : Carry an umbrella if you are going to the library.\n\n")

if not (book_due == "yes"):
    print("Book status : No book return needed today. You can browse new books :) .")

# Topic 5 -- Combining AND + OR + NOT together
if weather == "rainy" and book_due == "yes":
    print("Best plan   : Visit the library carefully doge the rain and return your book on time.")
elif weather == "sunny" and book_due == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan   : Stop by the library after school and return your book.")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan   : Perfect day for a longer reading session at the library!")
else:
    print("Best plan   : Check your schedule and plan a simple library visit.")

print()
print("Library plan complete! Happy reading!")
