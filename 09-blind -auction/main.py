import math

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}

bids: dict[str, int] = {}

def bid() -> None:
    user_name = input("Enter your name: ")
    user_price = int(input("Enter your price: "))
    bids[user_name] = user_price

bid()

# TODO-3: Whether if new bids need to be added
while True:
    is_new_bid = input("Do you want to bid? (Y/N): ").lower()
    if is_new_bid == "y":
        bid()
    elif is_new_bid == "n":
        print("Thanks for the entering into the auction!")
        break
    else:
        print("Please enter either 'y' or 'n'.\n")
        continue

# TODO-4: Compare bids in dictionary
max_bid_price = -math.inf
max_bid_user = ""
for bid, price in bids.items():
    if price > max_bid_price:
        max_bid_price = price
        max_bid_user = bid

print(f"Auction Winner: {max_bid_user} with price: {max_bid_price}")

# or
max_bid_user = max(bids, key=bids.get)
max_bid_price = bids[max_bid_user]
print(f"Auction Winner: {max_bid_user} with price: {max_bid_price}")

min_bid_user = min(bids, key=bids.get)
min_bid_price = bids[min_bid_user]
print(f"Auction Loser (least): {min_bid_user} with price: {min_bid_price}")