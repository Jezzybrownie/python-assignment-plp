def calculate_discount(price,discount_percent):
	
	if discount_percent >= 0.2:
		price *= (1- discount_percent)
	else:
		price = price
	return price
price = int(input('enter a price: '))
discount_percent= float(input("enter percentage discount as decimal: "))
htt= calculate_discount(price,discount_percent)
print(htt)