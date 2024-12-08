# File: CIS129_YourName_Lab12.py
# Author: JT Englis
# Title: Pet Class Program
# Date: December 8, 2024

# Define the Pet class
class Pet:
    # Constructor to initialize fields
    def __init__(self, name="", type="", age=0):
        self.__name = name  # Private attribute
        self.__type = type  # Private attribute
        self.__age = age    # Private attribute

    # Mutator methods (setters)
    def setName(self, name):
        self.__name = name

    def setType(self, type):
        self.__type = type

    def setAge(self, age):
        self.__age = age

    # Accessor methods (getters)
    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def getAge(self):
        return self.__age

# Main program
def main():
    # Create a Pet object
    animal = Pet()

    # Get values for the pet from the user
    inputName = input("Enter a pet name: ")
    animal.setName(inputName)

    inputType = input("Enter a pet type: ")
    animal.setType(inputType)

    inputAge = int(input("Enter a pet age: "))
    animal.setAge(inputAge)

    # Show values for the pet
    print("\nThe pet name is:", animal.getName())
    print("The pet type is:", animal.getType())
    print("The pet age is:", animal.getAge())

# Call the main function
if __name__ == "__main__":
    main()
