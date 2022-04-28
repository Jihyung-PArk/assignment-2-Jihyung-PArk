"""
Travel Tracker (Kivy)
Name: Jihyung Park
Date:12/04/2022
Brief Project Description:
GitHub URL: https://github.com/Jihyung-PArk/assignment-2-Jihyung-PArk.git
"""
# Create your main program in this file, using the TravelTrackerApp class
# main.py

from kivy.app import App
from kivy import Config
from kivy.lang import Builder
from placecollection import PlaceCollection
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.properties import ListProperty




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
    place = place_collection.load_places('places.csv')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""

        for line in self.place:

            if line[3] == "v":
                temp_button = Button(text="{} in {}, priority {} (visited)"
                                     .format(line[0], line[1], line[2]), background_color=(0, 1, 0, 1))
                temp_button.bind(on_press=lambda x, value=line: self.press_widgets(value))
                self.root.ids.list_of_place.add_widget(temp_button)

            elif line[3] == "n":
                temp_button = Button(text="{} in {}, priority {}".format(line[0], line[1], line[2]))
                temp_button.bind(on_press=lambda x, value=line: self.press_widgets(value))
                self.root.ids.list_of_place.add_widget(temp_button)
            # print(self.place)

    def press_widgets(self, value):
        if value[3] == "v":
            self.announced = "{} already visited.".format(value[0])
            # print(value)

        elif value[3] == "n":
            self.announced = "{} will be mark".format(value[0])
            for line in self.place:
                if line[0] == value[0] and line[1] == line[1] and line[2] == line[2]:
                    line[3] = "v"
                # print(self.place)
            self.clear_widgets()
            self.create_widgets()
            self.clear_visited_widgets()
            self.places_to_visit()

    def clear_widgets(self):
        self.root.ids.list_of_place.clear_widgets()

    def places_to_visit(self):
        num = 0
        for line in self.place:
            if line[3] == 'n':
                num += 1

        visit_num = Label(text="Places to visit: {}".format(num))
        self.root.ids.is_visited.add_widget(visit_num)

    def clear_visited_widgets(self):
        self.root.ids.is_visited.clear_widgets()

    def sort_value(self, sort_by):

        if sort_by == "Priority":
            self.clear_widgets()
            self.place.sort(key=lambda priority: priority[2], reverse=True)
            self.create_widgets()
        elif sort_by == "Name":
            self.clear_widgets()
            self.place.sort(key=lambda name: name[0])
            self.create_widgets()
        elif sort_by == "Country":
            self.clear_widgets()
            self.place.sort(key=lambda country: country[1])
            self.create_widgets()
        elif sort_by == "Visited":
            self.clear_widgets()
            self.place.sort(key=lambda is_visited: is_visited[3], reverse=True)
            self.create_widgets()

    def build(self):
        self.title = TITLE
        self.root = Builder.load_file('app.kv')
        # self.create_widgets()
        self.places_to_visit()
        self.sort_by = sorted(SORT)
        self.sort = self.sort_by[0]
        return self.root



if __name__ == '__main__':
    Config.set('graphics', 'width', 600)
    Config.set('graphics', 'height', 400)
    TravelTrackerApp().run()
