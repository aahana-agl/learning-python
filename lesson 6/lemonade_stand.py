def happy_customer():
    print("welcome to the amazing lemonade stand")

happy_customer()

price = float(input("price per cup: "))
cup = int(input("cups sold:"))

def total(price, cups):
    return round(price * cups,2)

total_p = total(price, cup)
print("total cost:",total_p)

paid = float(input("Amount paid:  "))

def change(paid, total):
    return round(paid - total)

print("change Due:" ,change(paid, total_p))

cups = int(input("haow many cups you have bought?"))
if cups >= 5:
    print("wow thankyou, ill give you this discount card, come back next time!")

else:
    print("thanks, come again!")

print("==== RECEIPT ====")
print("price: ",price)
print("cups: ",cups)
print("total: ",total_p)
print("paid: ",paid)
print("===================")