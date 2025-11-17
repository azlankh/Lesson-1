cost = float(input("Write The Cost Price="))
selling = float(input("Write The Selling Price="))
if (cost > selling):
    print("Its A LOSS")
    loss = cost-selling
    print(loss)
else:
    print("Its A PROFIT")
    profit = selling-cost
    print(profit)
 