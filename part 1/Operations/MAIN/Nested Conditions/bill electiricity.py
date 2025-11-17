units = int(input("Enter the no's of units Consumed: "))
if (units < 50):
    ammount = units * 2.60
    tax = 25
elif (units <= 100):
    ammount = 130 + ((units - 50) * 3.25)
    tax = 35
else:
    ammount = 130 + 162.50 + ((units - 100) * 5.26)
    tax = 45
bill = ammount + tax
print("Your Electricity Billl Is: ", bill)