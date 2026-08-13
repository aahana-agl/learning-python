fyeld1=23
fyeld2=24
fyeld3=101
feild4=404
feild5=34

total=fyeld1+fyeld2+fyeld3+feild4+feild5
average=total/5

print("total harvest: ", total,"kg") 
print("average per feild: ", average,"kg")

price_per_kg = 14
earnings = total * price_per_kg
print("total earnings :",earnings)

bags=total // 25
leftover=total % 25

print("full bags packed: ",bags)
print("leftover grain",leftover,"kg")