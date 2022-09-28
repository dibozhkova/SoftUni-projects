budget = int(input())
price_product = input()
while price_product != "End":
    budget -= int(price_product)
    if budget < 0:
        print("You went in overdraft!")
        break
    price_product = input()
else:
    print("You bought everything needed.")
