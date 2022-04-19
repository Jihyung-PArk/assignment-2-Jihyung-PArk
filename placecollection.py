"""
File name : placecollection.py
github URL: https://github.com/Jihyung-PArk/assignment-2-Jihyung-PArk.git
"""
import csv
from place import Place


# Constants
FILE_NAME = 'places.csv'


class PlaceCollection(Place):
    """..."""

    def __init__(self, places=None, **kwargs):
        super().__init__(**kwargs)
        if places is None:
            places = []
        self.places = places

    def __str__(self):
        return '\n'.join(str(place) for place in self.places)

    def load_places(self, places):
        try:
            infile = open(FILE_NAME, 'r')
            for line in infile:
                temp_list = line.strip().split(',')

                # convert the second item, which is priority, from str to int
                temp_list[2] = int(temp_list[2])
                self.places.append(temp_list)

                # list sort by visited status and by priority
                self.sort(places)
            infile.close()
            print("{} places loaded from {}".format(len(places), FILE_NAME))

            # (check point) below print check list element
            # print(places)

        except IOError as error:
            print("I/O error: {}".format(error))

    def save_places(self, csv_file, places):
            infile = open(FILE_NAME, "w")
            writer = csv.writer(infile)
            # save new csv file
            writer.writerows(places)
            infile.close()

            print('{} places saved to {}'.format(len(places), csv_file))

    def add_place(self, places):
        appending_list = []
        # Add name and check error
        self.method_name(appending_list)

        # add country and check error
        self.method_country(appending_list)

        # add priority and check error
        self.method_priority(appending_list)

        # new place is always un_visit
        appending_list.append("n")

        # print new place information
        print(
            "{0} in {1} (priority {2}) added to Travel Tracker".format(appending_list[0],
                                                                       appending_list[1],
                                                                       appending_list[2]))
        # add new place information and sort by visited status and by priority
        places.append(appending_list)
        self.sort(places)

    def num_of_unvisited_places(self, places):
        num = 0
        num_check = 0
        visit = 0
        un_visit = 0

        # list sort by visited status and by priority
        self.sort(places)

        # check visit and un_visit place number
        for list_check in places:
            num_check += 1
            visit += list_check[3].count("v")
            un_visit += list_check[3].count("n")

        # check no un_visit place
        if num_check == visit:
            print("No unvisited places")
        else:

            # list of places
            for places in places:
                num += 1
                print("{0}. {1: <{2}} in {3: <{4}} priority {5}".
                      format(num, places[0], self.find_max_name(places), places[1],
                             self.find_max_country(places), places[2]))
            print("{0} places. You still want to visit {1} places.".format(num, un_visit))

            # check input(mark) error
            self.mark_place_error_check(places, num)

    def sort(self, places):
        self.places.sort(key=lambda priority: priority[2])
        self.places.sort(key=lambda visit: visit[3])
        return places

    def method_name(self, appending_list):
        while True:
            name_input = str(input("Name: "))
            # check name_input is blank
            if name_input == "":
                print("Input can not be blank")
            # check name_input is integer
            elif name_input.isnumeric() or name_input[0] == "-":
                print("Input can not be integer")
            else:
                appending_list.append(name_input)
                break

    def method_country(self, appending_list):
        while True:
            country_input = input("Country: ")
            # check county_input is blank
            if country_input == "":
                print("Input can not be blank")
            # check country_input is integer
            elif country_input.isnumeric() or country_input[0] == "-":
                print("Input can not be integer")
            else:
                appending_list.append(country_input)
                break

    def method_priority(self, appending_list):
        while True:
            try:
                priority_input = int(input("Priority: "))

                # check priority_input is negative number
                if int(priority_input) <= 0:
                    print("Number must be > 0")
                else:
                    appending_list.append(priority_input)
                    break

            # check priority_input is not integer
            except ValueError:
                print("Invalid input; enter a valid number")

    def find_max_name(self, places):
        name_list = []
        for i in range(0, len(places)):
            name_list.append(places[i][0])
        max_name = sorted(name_list, key=len)
        max_name = max_name[-1]
        return len(max_name)

    def find_max_country(self, places):
        country_list = []
        for i in range(0, len(places)):
            country_list.append(places[i][1])
        max_country = sorted(country_list, key=len)
        max_country = max_country[-1]
        return len(max_country)

    def mark_place_error_check(self, places, num):
        while True:
            try:
                list_change = int(input("Enter the number of a place to mark as visited :"))
                list_change_for_csv = list_change
                list_change_for_csv -= 1

                if int(list_change) <= 0:
                    print("Number must be > 0")

                elif int(list_change) > num:
                    print("Invalid place number")

                # check mark
                elif places[int(list_change_for_csv)][3] == "v":
                    print("That place is already visited")
                    break

                else:
                    # change mark
                    places[int(list_change_for_csv)][3] = "v"
                    print("{0} in {1} visited".format(places[list_change_for_csv][0],
                                                      places[list_change_for_csv][1]))
                    break
            except ValueError:
                print("Invalid input; enter a valid number")

    def display_menu(self):
        print("Menu:")
        print("L - List places")
        print("A - Add new place")
        print("M - Mark a place as visited")
        print("Q - Quit")
