"""
Travel Tracker (Kivy)
Name: Jihyung Park
Date:12/04/2022
Brief Project Description:
GitHub URL: https://github.com/Jihyung-PArk/assignment-2-Jihyung-PArk.git
"""
# Create your main program in this file, using the TravelTrackerApp class
# main.py

import csv
from kivy.app import App
from kivy import Config
from kivy.lang import Builder
from placecollection import PlaceCollection
from place import Place



#constants
TITLE = 'Travel Tracker'



class TravelTrackerApp(App):
    """..."""
    # define properties here
    place_collection = PlaceCollection()
    place_collection.load_places('places.csv')

    def build(self):
        self.title = TITLE
        self.root = Builder.load_file('app.kv')
        return self.root
    # Place(self.root.ids.name_input.text,)
    # place_collection.add_place(self.root.ids.name_input.text, )


if __name__ == '__main__':
    Config.set('graphics', 'width', 600)
    Config.set('graphics', 'height', 400)
    TravelTrackerApp().run()
