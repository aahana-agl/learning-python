cost=float(input("please enter product price"))
sale=float(input("please enter sale amount"))
if sale>cost:
    amount=sale-cost
    print("profit",amount)
else:
    loss=cost-sale
    print("loss",loss)