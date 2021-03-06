"""
Travel Tracker (Kivy)
Name: Jihyung Park
Date:12/04/2022
Brief Project Description: Travel Tracker 2.0 (Complete)
GitHub URL: https://github.com/Jihyung-PArk/assignment-2-Jihyung-PArk.git
"""
# Create your main program in this file, using the TravelTrackerApp class
# main.py
import csv
from kivy.app import App
from kivy import Config
from kivy.lang import Builder
from placecollection import PlaceCollection
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from place import Place


# constants

TITLE = 'Travel Tracker'
CSV_FILE = 'places.csv'
SORT = ('Name', 'Country', 'Priority', 'Visited')


class TravelTrackerApp(App):
    """..."""

    # define properties here
    announced = StringProperty()
    sort = StringProperty()
    sort_by = ListProperty()
    place_collection = PlaceCollection()
    places = place_collection.load_places('places.csv')

    # create widgets by each place
    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""

        # clear widget before create widget
        self.root.ids.list_of_place.clear_widgets()
        try:

            # separate by line and create widget
            for line in self.places:

                if line[3] == "v":
                    temp_button = Button(text="{} in {}, priority {} (visited)"
                                         .format(line[0], line[1], line[2]))
                    temp_button.bind(on_press=lambda x, value=line: self.press_widgets(value))
                    self.root.ids.list_of_place.add_widget(temp_button)

                elif line[3] == "n":
                    temp_button = Button(text="{} in {}, priority {}"
                                         .format(line[0], line[1], line[2]), background_color=(0, 1, 0, 1))
                    temp_button.bind(on_press=lambda x, value=line: self.press_widgets(value))
                    self.root.ids.list_of_place.add_widget(temp_button)

            # save places to 'csv' file
            self.save_places('places.csv')

        except IOError as error:
            print("I/O error: {}".format(error))

    # when press widget change visit state ( visit <-> un-visit)
    def press_widgets(self, value):
        try:
            if value[3] == "v":
                for line in self.places:
                    if line[0] == value[0] and line[1] == value[1] and line[2] == value[2]:
                        line[3] = "n"
                        if value[2] <= 2:
                            self.announced = "You need to visit {}. Get going!".format(value[0])
                        else:
                            self.announced = "You need to visit {}".format(value[0])
                    # self.create_widgets()
                    # self.check_places_to_visit()

            elif value[3] == "n":
                for line in self.places:
                    if line[0] == value[0] and line[1] == value[1] and line[2] == value[2]:
                        line[3] = "v"
                        if value[2] <= 2:
                            self.announced = "You visited {}. Great travelling!".format(value[0])
                        else:
                            self.announced = "You visited {}".format(value[0])

            # create widget after change visit state
            self.create_widgets()

            # visit state is changed. Need count visit state again
            self.check_places_to_visit()

        except IOError as error:
            print("I/O error: {}".format(error))

    # count places to visit and display on is_visited BoxLayout
    def check_places_to_visit(self):
        num = 0

        try:

            # clear BoxLayout before count visit state
            self.root.ids.is_visited.clear_widgets()

            # count visit state each line
            for line in self.places:
                if line[3] == 'n':
                    num += 1

            # display visit state on is_visited BoxLayout
            visit_num = Label(text="Places to visit: {}".format(num))
            self.root.ids.is_visited.add_widget(visit_num)

        except IOError as error:
            print("I/O error: {}".format(error))

    # sort list by name, priority, country, or visit state
    def sort_by_element(self, element):

        try:
            if element == "Priority":
                self.places.sort(key=lambda priority: priority[2], reverse=True)
            elif element == "Name":
                self.places.sort(key=lambda name: name[0])
            elif element == "Country":
                self.places.sort(key=lambda country: country[1])
            elif element == "Visited":
                self.places.sort(key=lambda is_visited: is_visited[3], reverse=True)

            self.create_widgets()

        except IOError as error:
            print("I/O error: {}".format(error))

    # save place to 'csv' file
    def save_places(self, file_name):

        try:
            infile = open(file_name, "w")
            writer = csv.writer(infile)
            writer.writerows(self.places)
            infile.close()

        except IOError as error:
            print("I/O error: {}".format(error))

    # add new place to place list
    def add_places(self):
        try:

            # get input from TextInput box
            new_name = self.root.ids.name_input.text
            new_country = self.root.ids.country_input.text
            new_priority = self.root.ids.priority_input.text

            # check input field required
            if new_name == "" or new_country == "" or new_priority == "":
                self.announced = "All fields must be completed"
            elif new_priority[0] == "-" or new_priority[0] == "0":
                self.announced = "Priority must be > 0"
            elif not new_priority.isnumeric():
                self.announced = "Please enter a valid number"

            # add new place to current place list and clear InputBox
            else:
                add_list = [new_name, new_country, new_priority, "n"]
                infile = open('places.csv', 'a')
                self.places.append(add_list)
                infile.close()
                self.create_widgets()
                self.root.ids.name_input.text = ""
                self.root.ids.country_input.text = ""
                self.root.ids.priority_input.text = ""

        except IOError as error:
            print("I/O error: {}".format(error))

    # clear InputBox and announced Label
    def clear_add_place(self):
        try:
            self.announced = ""
            self.root.ids.name_input.text = ""
            self.root.ids.country_input.text = ""
            self.root.ids.priority_input.text = ""

        except IOError as error:
            print("I/O error: {}".format(error))

    def build(self):
        self.title = TITLE
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        self.check_places_to_visit()
        self.sort_by = sorted(SORT)
        self.sort = self.sort_by[0]
        self.announced = "Welcome to Travel Tracker 2.0"
        return self.root


if __name__ == '__main__':
    Config.set('graphics', 'width', 600)
    Config.set('graphics', 'height', 400)
    TravelTrackerApp().run()
