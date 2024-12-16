# Author: JT Englis
# Title: Pet Class Program
# Date: December 15, 2024
# Description: The program defines a 'Pet' class with name, type, and age fields, allowing the user to input and display pet details.

# Define the Pet class
class Pet:
    # Constructor to initialize the attributes
    def __init__(self):
        self.name = ""
        self.pet_type = ""
        self.age = 0

    # Mutators (Setters)
    def setName(self, name):
        self.name = name

    def setType(self, pet_type):
        self.pet_type = pet_type

    def setAge(self, age):
        self.age = age

    # Accessors (Getters)
    def getName(self):
        return self.name

    def getType(self):
        return self.pet_type

    def getAge(self):
        return self.age

# Main function to execute the program
def main():
    # Declare the variables to hold user input
    inputName = input("Enter your pet’s name: ")
    inputType = input("Enter your pet’s type: ")
    inputAge = int(input("Enter your pet’s age: "))
    
    # Create a Pet object
    Animal = Pet()
    
    # Set values for the pet using mutators
    Animal.setName(inputName)
    Animal.setType(inputType)
    Animal.setAge(inputAge)
    
    # Display the pet's details using accessors
    print(f"Your pet name: {Animal.getName()}")
    print(f"Your pet type: {Animal.getType()}")
    print(f"Your pet age: {Animal.getAge()}")

# Call the main function to run the program
main()
