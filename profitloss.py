actualcost = float(input("Enter the Actual Product Price: "))
saleamount = float(input("Enter the sales amount: "))

if (saleamount > actualcost):
    amount = saleamount - actualcost
    print("Total profit = {0}".format(amount))
else:

    print("No profit!!")
