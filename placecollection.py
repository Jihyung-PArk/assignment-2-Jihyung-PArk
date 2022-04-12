"""
File name : placecollection.py
github URL: https://github.com/Jihyung-PArk/assignment-2-Jihyung-PArk.git
"""

from place import Place

# Constants
FILE_NAME = 'places.csv'


class PlaceCollection:
    """..."""

    def __init__(self, places=None):
        if places is None:
            places = []
        self.places = places

    def __str__(self):
        return '\n'.join(str(place) for place in self.places)

    def load_places(self, csv_file):
        pass

    def save_places(self, csv_file):
        pass

    def add_places(self, place):
        pass

    def num_of_unvisited_places(self):
        pass

    def sort(self, attribute_name):
        pass