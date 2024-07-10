# lib/cli.py

from models.traveler import Traveler
from models.location import Location

from helpers import (
    exit_program,
    press_enter_to_continute
)

class Cli:
    def start(self):
        self.menu()

# Menu:

    def menu(self):
        print("Welcome to the menu please select from below:")
        print("")
        print("Type '1' to create a traveler")
        print("Type '2' to delete a traveler by their id")
        print("Type '3' to list out all travelers")
        print("Type '4' to find traveler by id")
        print("Type '5' to create a location")
        print("Type '6' to delete a location by it's id")
        print("Type '7' to list out all locations")
        print("Type '8' to find location by id") 
        print("Type 'exit' to exit program")
        self.selection()

# Selections:

    def selection(self):
        print("")
        user_input = input("Input Here: ")
        if user_input == "1":
            self.create_traveler()
        elif user_input == "2":
            self.delete_traveler()
        elif user_input == "3":
            self.list_travelers()
        elif user_input == "4":
            self.find_traveler_by_id()
        elif user_input == "5":
            self.create_location()
        elif user_input == "6":
            self.delete_location()
        elif user_input == "7":
            self.list_locations()
        elif user_input == "8":
            self.find_location_by_id()
        elif user_input == "exit":
            exit_program()
        else:
            print("invalid input, try again")
            press_enter_to_continute()
            self.menu()

# Traveler fuctions:

    def create_traveler(self):
        print("")
        name = input("Input traveler's name you would like to create: ")
        try:
            Traveler.create(name=name)
            print("Traveler has been created.")
        except ValueError as error:
            print("")
            print(error)
            print("")

        press_enter_to_continute()
        self.menu()

    def delete_traveler(self): 
        print("")
        id = input("Input traveler's id you would like to delete: ")
        traveler = Traveler.find_by_id(id)
        if traveler:
            print(f"{traveler.name} has been deleted")
            traveler.delete()
        else:
            print("")
            print("Traveler does not exist.")
            print("")

        press_enter_to_continute()
        self.menu()

    def list_travelers(self):
        travelers = Traveler.all()
        for traveler in travelers:
            self.list_traveler(traveler)
        press_enter_to_continute()
        self.menu()

    
    def list_traveler(self,traveler):
        print("")
        print(f"Name: {traveler.name}")
        print(f"Id: {traveler.id}")
        for location in traveler.locations():
            print(f'Location traveler is going to: {location.name}')

    

    def find_traveler_by_id(self): 
        entry = input("Input traveler's id you would like to find:")
        traveler = Traveler.find_by_id(entry)
        if traveler:
            self.traveler_info(traveler)
        else:
            print("")
            print(f"No traveler exists with the id: {entry}")
            
        press_enter_to_continute()
        self.menu()

    def traveler_info(self,traveler):
        print("")
        print(f"Traveler: {traveler.name}  Traveler Id: {traveler.id} ")
        for location in traveler.locations():
            print("")
            print(f"Locations: {location.name}  Location Id: {location.id} ")

# Location fuctions:

    def create_location(self):
        print("")
        name = input("Input location's name you would like to create: ")
        traveler_id = input("Input traveler's id that is going to this location that you would like to create: ")
        try:
            location_traveler_id_converted_to_int = int(traveler_id)
            Location.create(name=name,traveler_id=location_traveler_id_converted_to_int )
            print("Location has been created.")
        except ValueError as error:
            print("")
            print(error)
            print("")
            
        press_enter_to_continute()
        self.menu()


    def delete_location(self): 
        print("")
        id = input("Input location's id you would like to delete: ")
        location = Location.find_by_id(id)
        if location:
            print(f"{location.name} has been deleted")
            location.delete()
        else:
            print("")
            print("Location does not exist.")
            print("")

        press_enter_to_continute()
        self.menu()

    def list_locations(self):
        locations = Location.all()
        for location in locations:
            self.list_location(location)
        press_enter_to_continute()
        self.menu()

    
    def list_location(self,location):
        print("")
        print(f"Id: {location.id} and Name: {location.name}")
        print("")

    def find_location_by_id(self): 
        entry = input("Input the location's id you would like to find:")
        location = Location.find_by_id(entry)
        if location:
            self.location_info(location)
        else:
            print("")
            print(f"No location exists with the id: {entry}")
            
        press_enter_to_continute()
        self.menu()

    def location_info(self,location):
        print("")
        print(f"Location: {location.name}  Location Id: {location.id} ")
        # for location in traveler.locations():
        #     print("")
        #     print(f"Locations: {location.name}  Location Id: {location.id} ")