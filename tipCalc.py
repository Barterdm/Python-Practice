import math

bill = float(input("How much was the total bill?: "))

tip = int(input("What % would you like to tip?: "))

tip = float(tip/100)

fTip = float(bill * tip)
fTip = '%0.2f' % (fTip)

print(fTip)
