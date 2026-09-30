print("🍎🍉GROCERY COST COMPARISON TOOL!🥳")
rice_price = 12
milk_price = 4
fruit_price = 8
number_of_baskets = 2
family_members = 4

basket_cost_per_person = (rice_price + milk_price + fruit_price) * number_of_baskets / family_members
print(basket_cost_per_person)

total_items = int(input("Please enter the total number of items: "))
people = int(input(" Please enter the number of people: "))

if people == 0:
    print(" Sry but you cannot share between 0 people")

else:
    if total_items % people == 0:
        print("They divide equally : ", total_items // people)
        

    else:
        print("They do not divide equally")
        print(total_items % people)

recorded_average = 65
total_weeks = 4
wrong_week_cost = 50
correct_week_cost = 80

total = recorded_average * total_weeks
total = total - wrong_week_cost + correct_week_cost
corrected_average = total / total_weeks

print("recorded average is:",recorded_average)
print("total is:",total )
print("corrected average is:",corrected_average)

store_a_average = 70
store_b_average = 75
store_c_average = 80

verdict = corrected_average < store_a_average and corrected_average < store_b_average and corrected_average < store_c_average
print(basket_cost_per_person, corrected_average, verdict)
print("Thx bye!😁")