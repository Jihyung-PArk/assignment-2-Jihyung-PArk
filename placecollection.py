"""
File name : placecollection.py
Github URL: https://github.com/Jihyung-PArk/assignment-2-Jihyung-PArk.git
"""
from place import Place
import csv

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

    def load_places(self, file_name):

        try:
            infile = open(file_name, 'r')
            for line in infile:
                temp_list = line.strip().split(',')

                # convert the second item, which is priority, from str to int
                temp_list[2] = int(temp_list[2])
                self.places.append(temp_list)

                # list sort by visited status and by priority
            infile.close()

            return self.places
        except IOError as error:
            print("I/O error: {}".format(error))

    def save_places(self, file_name):
        infile = open(file_name, "w")
        writer = csv.writer(infile)
        # save new csv file
        writer.writerows(self.places)
        infile.close()

        return self.places

    def add_place(self, Place):
        # add_list = []
        #
        # places_test = super().__str__()
        # add_list.append(places_test)
        #
        # print(places_test)
        #
        # print(add_list)
        # infile = open(FILE_NAME, 'a')
        # self.places.append(Place)
        # infile.close()
        pass

    def sort(self, sort_element):
        if sort_element == "priority":
            self.places.sort(key=lambda priority: priority[2], reverse=True)
            return self.places
        elif sort_element == "name":
            self.places.sort(key=lambda name: name[0])
            return self.places
        elif sort_element == "country":
            self.places.sort(key=lambda country: country[1])
            return self.places
        elif sort_element == "is_visited":
            self.places.sort(key=lambda is_visited: is_visited[3], reverse=True)
            return self.places

    def get_num_of_unvisited(self):
        un_visit = 0
        for line in self.places:
            un_visit += line[3].count("n")

        print("{} place(s) unvisited".format(un_visit))

    # def sort(self, places):
    #     self.places.sort(key=lambda priority: priority[2])
    #     self.places.sort(key=lambda visit: visit[3])
    #     return places
