

def tipcalc():
    bill = 0
    while True:
        try:
            bill = float(input("How much was the total bill?: $ "))
        except ValueError:
            print("Only input the numbers please.")
            main()

        try:
            tip = int(input("What % did your server earn tonight?\nTypicall between 15-20%: "))
            break
        except ValueError:
            print("Only input numbers please. ")

    ftip = float(tip/100)
    ftip = float(ftip * bill)
    ftip = '%0.2f' % ftip

    print("The total tip is: ",ftip)
    main()

def main():
    q1 = input("Would you like me to help with your tip?: ")
    while q1 == 'y' or 'yes':
        tipcalc()
    if q1 == 'n' or 'no':
        print("Hope you enjoyed everything!")
        quit()




























#bill = float(input("How much was the total bill?: "))

#tip = int(input("What % would you like to tip?: "))

#tip = float(tip/100)

#fTip = float(bill * tip)
#fTip = '%0.2f' % fTip

#print(fTip)
