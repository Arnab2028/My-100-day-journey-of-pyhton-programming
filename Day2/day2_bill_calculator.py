print("Hello user !\nWelcome to tip calculater...")
bill = float(input("What is the bill amount ?\n=> "))
people = int(input("How many people to split the bill ?\n=> "))
tip = int(input("What percentage tip would you like to give ? 10, 12, 15\n=> "))
split = ((bill / people) * (100 + tip)) / 100
print(f"every person need to pay {split}/-Rupees each. ")