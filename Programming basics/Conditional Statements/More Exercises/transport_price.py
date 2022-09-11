km = int(input())
tariff = input()
price = 0
if tariff == "day":
 if km < 20:
  price = km * 0.79 + 0.7
 elif km >= 100:
  price = km * 0.06
 else:
  price = km * 0.09
if tariff == "night":
   if km < 20:
    price = km * 0.9 + 0.7
   elif km >= 100:
    price = km * 0.06
   else:
    price = km * 0.09
print(f"{price:.2f}")
