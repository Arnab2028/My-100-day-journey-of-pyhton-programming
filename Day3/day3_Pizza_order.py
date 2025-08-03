bill = 0
print("Welcome to Python Pizza Deliveries!")
print("Small pizza(S): $15.\nMedium pizza(M): $20.\nLarge pizza(L): $25. \n")
size = input("What size pizza do you want? S, M or L: ")

print("\npepperoni for small pizza: $2.\nPepperoni for medium and large pizza: $3.\n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

print("\nExtra cheese for any size of pizza is $1\n")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#---Bill based on size of the pizza---
if size == "S" or size == "s":
    bill = 15
elif size == "M" or size == "m":
    bill = 20
elif size == "L" or size == "l":
    bill = 25
else:
    print("\n---Invalid input of pizza size---\n")
    quit()

#--- bill based on [size + add-on(pepperoni)]---
if pepperoni == "Y" or pepperoni == "y":
    if size == "S" or size == "s":
        bill += 2
    else:
        bill += 3

#---bill based on [size + add-on(pepperoni + extra cheese)]---
if extra_cheese == "Y" or "y":
    bill += 1

 #---output---
print(f"\nNet bill: ${bill}")

