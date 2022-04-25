
from assignment_1 import TravelTracker

def run_test():

    travel_tracker = TravelTracker()
    print("Travel Tracker 1.0 - by Jihyung Park")
    travel_tracker.load_places('places.csv')
    print(travel_tracker)
    travel_tracker.display_menu()
    choice = input("Enter a choice: ").strip().upper()
    while choice != 'Q':

        if choice == 'L':
            travel_tracker.list_places()
        elif choice == 'A':
            travel_tracker.add_new_place()
        elif choice == 'M':
            travel_tracker.mark_place_error_check()
        elif choice == "S":
            travel_tracker.sort()
        else:
            print("Invalid menu choice")
        travel_tracker.display_menu()
        choice = input("Enter a choice: ").strip().upper()
    travel_tracker.save_places("places.csv")
    print("Have a nice day :)")

run_test()