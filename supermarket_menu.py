#Supermarket program created by Alex Kowalczuk


print("Welcome to CS110 Supermarket!")

pot = 0
tom = 0
app = 0
man = 0


again = True 
while again == True:
	print("1: Potatoes ($0.25 per potato)")
	print("2: Tomatoes ($1.25 per tomato)")
	print("3: Apples ($0.75 per apple)")
	print("4: Mangoes ($1.75 per mango)")
	print("5: Checkout \n")

	x = int(input("Please enter your choice (1-5): ")) #select option

	if x == 1:
		Potatoes = int(input("How many potatoes would you like to buy?: "))
		if Potatoes > 0:
			pot = pot + Potatoes
			print("Price:",(pot * 0.25))
		else:
			print("Please enter valid number of product")

	elif x == 2:
		Tomatoes = int(input("How many tomatoes would you like to buy?: "))
		if Tomatoes > 0:
			tom = tom + Tomatoes
			print("Price:",(tom * 1.25))
		else:
			print("Please enter valid number of product")

	elif x == 3:
		Apples = int(input("How many apples would you like to buy?: "))
		if Apples > 0:
			app = app + Apples
			print("Price:",(app * 0.75))
		else:
			print("Please enter valid number of product")

	elif x == 4:
		Mangoes = int(input("How many mangoes would you like to buy?: "))
		if Mangoes > 0:
			man = man + Mangoes
			print("Price:",(man * 1.75))
		else:
			print("Please enter valid number of product")

	elif x == 5:
		print("Potatoes:$",(pot * 0.25))
		print("Tomatoes:$",(tom * 1.25))
		print("Apples:$",(app * 0.75))
		print("Mangoes:$",(man * 1.75))

		Total = ((pot * 0.25)+(tom * 1.25)+(app * 0.75)+(man * 1.75))
		print("Total to pay:$",(Total))

		t = float(input("Please enter the amount to pay for your cart: "))

		c = 0

		for i in range(t>=Total):
			pass
			if t >= Total:
				c = t - Total
				print("Change is: $", c)
			else:
				print("Please enter valid amount to pay off your cart! Do not try to rob my CS110 store !")

		bills ={5 : "$5 bill(s)", 1 : "$1 bill(s)", 0.25 : " quarter(s)", 0.1 : "dime(s)", 0.05 : "nickel(s)", 0.01 : "penny(ies)"}

		print("Give the customer: ")
		for z in bills.keys():
			number = c // z
			##print("$ " + str(z) + "    "+ str(number))
			print(str(int(number)) + " " + bills.get(z))
			c = c - number * z

		again = False

	else:
		print("Please enter valid choice from 1 to 5")