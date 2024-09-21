# Coffee Shop Simulator
# This program calculates the total cost of coffees and muffins purchased, applies a 6% tax, and displays a formatted receipt.

# Constants for prices and tax rate
COFFEE_PRICE = 5.00
MUFFIN_PRICE = 4.00
SANDWICH_PRICE = 7.00
JUICE_PRICE = 3.00
TAX_RATE = 0.06

# Input from the user
num_coffees = int(input("Number of coffees bought? "))
num_muffins = int(input("Number of muffins bought? "))
num_sandwiches = int(input("Number of sandwiches bought? "))
num_juices = int(input("Number of juices bought? "))

# Calculate costs
subtotal = (num_coffees * COFFEE_PRICE) + (num_muffins * MUFFIN_PRICE) + (num_sandwiches * SANDWICH_PRICE) + (num_juices * JUICE_PRICE)
tax = subtotal * TAX_RATE
total = subtotal + tax

# Display receipt
print("\n***************************************")
print("My Coffee and Muffin Shop")
print("***************************************")
print("\n***************************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{num_coffees} Coffee at ${COFFEE_PRICE} each: ${num_coffees * COFFEE_PRICE:.2f}")
print(f"{num_muffins} Muffins at ${MUFFIN_PRICE} each: ${num_muffins * MUFFIN_PRICE:.2f}")
print(f"{num_sandwiches} Sandwiches at ${SANDWICH_PRICE} each: ${num_sandwiches * SANDWICH_PRICE:.2f}")
print(f"{num_juices} Juices at ${JUICE_PRICE} each: ${num_juices * JUICE_PRICE:.2f}") 
print(f"6% tax: ${tax:.2f}")
print("---------")
print(f"Total: ${total:.2f}")
print("***************************************")
print("Thank you for visiting My Coffee Shop!")
