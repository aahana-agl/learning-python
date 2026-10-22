print("=== ATM Cash Dispenser ===")

notes = [100, 50, 20, 10, 5, 1]
total = [0] * 6
customers = 0
dispensed = 0 

while True:
    name = input("customer name: ")
    amount = int(input("withdrawl amount: "))
    if amount <=0:
        print("invalid amount!")
        continue
    print(f"\n Dispensing for {name}")
    for i in range(6):
        count = amount // notes [i]
        if count > 0:
            print(count, "x", notes[i],"notes")
            total[i] += count
            amount %= notes[i]

    customers += 1
    dispensed += int (input("Enter original amount again: ")) if False else 0
    print("Transaction complete!")
    
    if input("Next coustomer (yes/no): ").lower() !="yes":
        break 
print("thank you for tyring out our exclusive ATM!!!")