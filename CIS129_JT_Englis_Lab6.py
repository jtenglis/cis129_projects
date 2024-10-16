# Hotdog Cookout Calculator
# Author: JT Englis
# Date: 2024-10-16
# This program calculates the number of hot dog and bun packages needed for a cookout, and the leftovers, based on the number of people and hot dogs per person.

# Function to get the total number of hot dogs needed
def get_total_hot_dogs():
    # Get the number of people attending the cookout
    people = int(input("Enter the number of people attending the cookout: "))
    # Get the number of hot dogs per person
    hot_dogs_per_person = int(input("Enter the number of hot dogs for each person: "))
    # Calculate the total number of hot dogs needed
    total_hot_dogs = people * hot_dogs_per_person
    return total_hot_dogs

# Function to display the results
def show_results(dogs_left, min_dogs, buns_left, min_buns):
    print(f"Minimum packages of hot dogs needed: {min_dogs}")
    print(f"Minimum packages of hot dog buns needed: {min_buns}")
    print(f"Hot dogs left over: {dogs_left}")
    print(f"Hot dog buns left over: {buns_left}")

# Main function
def main():
    # Constants for the package sizes
    DOGS_PER_PACKAGE = 10
    BUNS_PER_PACKAGE = 8
    
    # Get the total number of hot dogs needed
    total_hot_dogs = get_total_hot_dogs()

    # Calculate the number of leftover hot dogs and buns
    dogs_left = (DOGS_PER_PACKAGE - total_hot_dogs % DOGS_PER_PACKAGE) % DOGS_PER_PACKAGE
    buns_left = (BUNS_PER_PACKAGE - total_hot_dogs % BUNS_PER_PACKAGE) % BUNS_PER_PACKAGE

    # Calculate the minimum number of packages required (manually rounding up)
    min_dogs = (total_hot_dogs + DOGS_PER_PACKAGE - 1) // DOGS_PER_PACKAGE
    min_buns = (total_hot_dogs + BUNS_PER_PACKAGE - 1) // BUNS_PER_PACKAGE

    # Show the results
    show_results(dogs_left, min_dogs, buns_left, min_buns)

# Run the main function
if __name__ == "__main__":
    main()
