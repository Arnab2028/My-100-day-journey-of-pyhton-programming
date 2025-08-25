from art import logo
print(f"{logo}\n"
      "---Welcome to the blind auction---")

# TODO-1: Ask the user for input
can_continue = True
while can_continue:
    user_name = input("What is your name?\n=> ")
    user_bid = int(input(f"{user_name} what is your bidding amount?\n=> "))

# TODO-2: Save data into dictionary {name: price}
    price = {}

# TODO-3: Whether if new bids need to be added

    price[user_name] = user_bid

    new_bidder = input(f"{user_name} is there any other bidders?\n"
                       f"a) Type 'Yes' if any.\n"
                       f"b) Type 'No' to print the name of the highest bidder and the bidding amount.\n=> ").lower()

    if new_bidder == "yes":
        can_continue = True
        print("\n" * 10000)





# TODO-4: Compare bids in dictionary
    elif new_bidder == "no":
        highest_bidder = ""
        highest_bid = 0
        for key in price:
            if highest_bid < price[key]:
                highest_bidder = key
                highest_bid = price[key]
        print(f"The highest bidder is: {highest_bidder}\n"
              f"The highest bidding amount is: {highest_bid}")
        can_continue = False

