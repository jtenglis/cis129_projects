# Author Name: JT Englis
# Title: Plant Care Reminder Program
# Course & CRN: CIS129-12432
# Date: December 18, 2024
# Description: A Python program that helps users track and care for their houseplants by sending reminders for watering, fertilizing, and other essential tasks. 
# The program allows users to add, update, delete, and generate reports for their plant care, while promoting a positive and enjoyable plant-care experience.

import datetime
import json
import time

# Initialize an empty list of plants
plants = []

# Function to save the plant data to a JSON file
def save_plants():
    with open('plants.json', 'w') as file:
        json.dump(plants, file)

# Function to load the plant data from a JSON file
def load_plants():
    global plants
    try:
        with open('plants.json', 'r') as file:
            plants = json.load(file)
    except FileNotFoundError:
        plants = []

# Function to add a new plant
def add_plant():
    name = input("\n🌱 What’s the name of your plant? ")
    water_schedule = int(input("💧 How often does it need water? (e.g., every 3 days): "))
    care_notes = input("🌸 Any special care notes for this little one? ")
    plant = {
        'name': name,
        'water_schedule': water_schedule,
        'care_notes': care_notes,
        'last_watered': str(datetime.date.today())
    }
    plants.append(plant)
    save_plants()
    print(f'\n🎉 {name} has been added to your plant family! 🌿💚')

# Function to delete a plant by name
def delete_plant():
    name = input("\n❌ Which plant would you like to say goodbye to? ")
    plant_found = False
    for plant in plants:
        if plant['name'].lower() == name.lower():
            plants.remove(plant)
            plant_found = True
            break
    if plant_found:
        save_plants()
        print(f'\n🌿 {name} has been removed from your plant family. Goodbye little one! 🌻')
    else:
        print(f'\n😢 Sorry, {name} is not in your plant family.')

# Function to update a plant's details
def update_plant():
    name = input("\n✏️ Which plant do you want to update? ")
    plant_found = False
    for plant in plants:
        if plant['name'].lower() == name.lower():
            plant_found = True
            print(f'\n🌿 Time to update details for {name}...')
            new_water_schedule = int(input(f'💧 How often should {name} be watered now? (e.g., every 3 days): '))
            new_care_notes = input("🌸 Any new care notes? ")
            plant['water_schedule'] = new_water_schedule
            plant['care_notes'] = new_care_notes
            plant['last_watered'] = str(datetime.date.today())  # Reset last watered to today
            save_plants()
            print(f'\n🌱 {name} has been updated! 🌻')
            break
    if not plant_found:
        print(f'\n😢 We couldn’t find {name} in your plant family.')

# Function to check which plants need care today
def check_reminders():
    today = datetime.date.today()
    print(f"\n🌸 Today's Care Reminders 🌿")
    plant_found = False
    for plant in plants:
        last_watered = datetime.datetime.strptime(plant['last_watered'], "%Y-%m-%d").date()
        days_since_watered = (today - last_watered).days
        if days_since_watered >= plant['water_schedule']:
            print(f'💧 Don’t forget to water {plant["name"]}! 🌿')
            plant_found = True
        else:
            print(f'{plant["name"]} is doing great today! Keep up the good work! 🌸')
    
    if not plant_found:
        print("\n🌼 All your plants are happy today! Keep it up! 🌻")

# Function to generate a care history report
def generate_report():
    print("\n🌿 Care History Report 🌸")
    if not plants:
        print("😢 Your plant family is empty. Add some plants to start caring for them! 🌱")
    else:
        for plant in plants:
            print(f'\n🌱 Plant Name: {plant["name"]}')
            print(f'💧 Last Watered: {plant["last_watered"]}')
            print(f'🌸 Care Notes: {plant["care_notes"]}')
            print('-' * 30)

# Function to view the list of plants in a user-friendly format
def view_plants():
    print("\n🌿 Your Plant Family 🌱")
    if not plants:
        print("😢 Your plant family is empty. Add some plants to start caring for them! 🌸")
    else:
        for plant in plants:
            print(f'🌱 {plant["name"]} - Needs water every {plant["water_schedule"]} days')
            print(f'   🌸 Notes: {plant["care_notes"]}')
            print(f'   💧 Last watered: {plant["last_watered"]}')
            print('-' * 30)

# Main program loop
def main():
    load_plants()  # Load plant data when the program starts

    while True:
        print("\n🌿 Welcome to the Plant Care Reminder! 🌱")
        print("1. Add a New Plant 🌵")
        print("2. Say Goodbye to a Plant ❌")
        print("3. Update a Plant’s Details ✏️")
        print("4. View Today's Care Reminders 💧")
        print("5. Generate Care History Report 📊")
        print("6. View Your Plant Family 🌸")
        print("7. Exit 🌸")
        
        choice = input("\n✨ Choose an option (1-7): ")

        if choice == '1':
            add_plant()
        elif choice == '2':
            delete_plant()
        elif choice == '3':
            update_plant()
        elif choice == '4':
            check_reminders()
        elif choice == '5':
            generate_report()
        elif choice == '6':
            view_plants()
        elif choice == '7':
            print("\n🌿 Exiting program. Have a leafy day! 🌱💚")
            break
        else:
            print("\n❌ Oops, invalid option. Please choose a valid number (1-7).")

        # Add a little pause for extra cuteness
        time.sleep(1)

# Run the program
if __name__ == '__main__':
    main()
