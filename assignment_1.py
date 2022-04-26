import csv
from place import Place

# Constants
FILE_NAME = 'places.csv'


class TravelTracker(Place):
    """..."""

    def __init__(self, places=None, name="", country="", priority=0, is_visited=False):
        super().__init__(name, country, priority, is_visited)
        if places is None:
            places = []
        self.places = places

    def __str__(self):
        return '\n'.join(str(place) for place in self.places)

    def load_places(self, file_name):

        try:
            infile = open(file_name, 'r')
            for line in infile:
                temp_list = line.strip().split(',')

                # convert the second item, which is priority, from str to int
                temp_list[2] = int(temp_list[2])
                self.name = temp_list[0]
                self.country = temp_list[1]
                self.priority = temp_list[2]
                self.is_visited = temp_list[3]
                self.places.append(temp_list)

            infile.close()

            return self.places

        except IOError as error:
            print("I/O error: {}".format(error))

    def list_places(self):

        num = 0
        un_visit = 0
        visit = 0

        try:
            for place in self.places:
                num += 1
                not_visited = " "
                if place[3] == "n":
                    not_visited = "*"
                # place.insert(0, not_visited)

                un_visit += place[3].count("n")
                visit += place[3].count("v")

                print("{0}{1}. {2: <{3}} in {4: <{5}} priority {6}".format(not_visited, num,
                                                                           place[0],
                                                                           self.find_max_name(),
                                                                           place[1],
                                                                           self.find_max_country(),
                                                                           place[2]))

        except IOError as error:
            print("I/O error: {}".format(error))

    def add_new_place(self):
        appending_list = [self.method_name, self.method_country, self.method_priority, "n"]

        self.places.append(appending_list)

    def mark_a_place_visited(self):

        num_check = 0
        visit = 0
        un_visit = 0

        # self.sort(self.places)

        for list_check in self.places:
            num_check += 1
            visit += list_check[3].count("v")
            un_visit += list_check[3].count("n")

    def save_places(self, file_name):
        try:
            infile = open(file_name, "w")
            writer = csv.writer(infile)
            writer.writerows(self.places)
            infile.close()

            return self.places

        except IOError as error:
            print("I/O error: {}".format(error))

    def find_max_name(self):
        name_list = []
        for i in range(0, len(self.places)):
            name_list.append(self.places[i][0])
        max_name = sorted(name_list, key=len)
        max_name = max_name[-1]
        return len(max_name)

    def find_max_country(self):
        country_list = []
        for i in range(0, len(self.places)):
            country_list.append(self.places[i][1])
        max_country = sorted(country_list, key=len)
        max_country = max_country[-1]
        return len(max_country)

    @property
    def sort(self):
        sort_by = input("Sort by : ")

        try:
            if sort_by == "name":
                self.places.sort(key=lambda name: name[0])
                return self.places
            elif sort_by == "country":
                self.places.sort(key=lambda country: country[1])
                return self.places
            elif sort_by == "priority":
                self.places.sort(key=lambda priority: priority[2], reverse=True)
                return self.places
            elif sort_by == "is_visited":
                self.places.sort(key=lambda is_visited: is_visited[3], reverse=True)
                return self.places

        except IOError as error:
            print("I/O error: {}".format(error))

    def method_name(self):

        while True:
            name_value = input("name: ")
            if name_value == "":
                print("Input can not be blank")

            elif name_value.isnumeric() or name_value[0] == "-":
                print("Input can not be integer")

            else:
                return name_value

    def method_country(self):
        while True:
            country_value = input("country: ")
            if country_value == "":
                print("Input can not be blank")

            elif country_value.isnumeric() or country_value[0] == "-":
                print("Input can not be integer")

            else:
                return country_value

    def method_priority(self):
        while True:
            try:
                priority_input = int(input("Priority: "))

                if int(priority_input) <= 0:
                    print("Number must be > 0")
                else:
                    return priority_input

            except ValueError:
                print("Invalid input; enter a valid number")

    def mark_place_error_check(self):

        try:
            list_change = int(input("Enter the number of a place to mark as visited :"))
            list_change_for_csv = list_change
            list_change_for_csv -= 1

            if int(list_change) <= 0:
                print("Number must be > 0")

            elif int(list_change) > len(self.places):
                print("Invalid place number")

            # check mark
            elif self.places[int(list_change_for_csv)][3] == "v":
                return print("That place is already visited")

            else:
                # change mark
                self.places[int(list_change_for_csv)][3] = "v"
                return print("{0} in {1} visited".format(self.places[list_change_for_csv][0],
                                                         self.places[list_change_for_csv][1]))

        except ValueError:
            print("Invalid input; enter a valid number")

    def display_menu():
        print("Menu:")
        print("L - List places")
        print("A - Add new place")
        print("M - Mark a place as visited")
        print("S - Sort by")
        print("Q - Quit")
