# Lab 5 The Bottle Return Program
# Author: JT Englis
# Date: 2024-10-15
# This program tracks the total number of bottles collected over seven days and calculates the total payout based on the bottles returned.

def main():
    # Step 1: Declare variables
    total_bottles = 0
    counter = 1
    today_bottles = 0
    total_payout = 0
    keep_going = "y"

    # Step 2: Loop to run program again
    while keep_going.lower() == "y":
        # Reset totals for a new week
        total_bottles = 0
        total_payout = 0

        # Get bottles for each day of the week (7 iterations)
        counter = 1
        while counter <= 7:
            # Ask for the number of bottles returned for the day
            print(f"Enter number of bottles returned for day #{counter}:")
            today_bottles = int(input())  # Input number of bottles for today
            total_bottles += today_bottles  # Accumulate total bottles
            counter += 1  # Increment the counter

        # Calculate total payout
        total_payout = total_bottles * 0.10  # Calculate payout based on total bottles

        # Print the total number of bottles and total payout
        print(f"The total number of bottles collected is {total_bottles}.")
        print(f"The total paid out is ${total_payout:.2f}.")

        # Ask if the user wants to enter another week's worth of data
        print("Do you want to enter another week’s worth of data? (Enter y or n):")
        keep_going = input()  # Input for continuation

    print("Program has ended.")  # End message

# Call the main function to run the program
if __name__ == "__main__":
    main()
