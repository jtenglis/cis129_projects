# Module 4 Lab-4
# JT Englis
# Date: 2024-10-01
# This program calculates store and employee bonuses based on sales performance.

# Step 1: Declare local variables
monthlySales = 0  # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount = 0  # employee bonus amount
salesIncrease = 0.0  # percent of sales increase
prompt = "Enter the monthly sales: "  # prompt for user input

# Step 2: Get the monthly sales
monthlySales = float(input(prompt))

# Step 3: Calculate the store bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

# Step 4: Get the percent of sales increase
salesIncrease = float(input("Enter the percent of sales increase: "))
salesIncrease = salesIncrease / 100  # Convert percentage to decimal format

# Step 5: Determine the employee bonus
if salesIncrease >= 0.05:
    empAmount = 75
elif salesIncrease >= 0.04:
    empAmount = 50
elif salesIncrease >= 0.03:
    empAmount = 40
else:
    empAmount = 0

# Step 6: Print the store and employee bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)

# Additional message for the highest bonus amounts
if (storeAmount == 6000) and (empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible!')
