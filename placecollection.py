"""
File name : placecollection.py
Github URL: https://github.com/Jihyung-PArk/assignment-2-Jihyung-PArk.git
"""
import csv

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

    # load 'csv' file to list
    def load_places(self, file_name):

        try:
            infile = open(file_name, 'r')

            # split file list to each line
            for line in infile:
                temp_list = line.strip().split(',')

                # convert the second item, which is priority, from str to int
                temp_list[2] = int(temp_list[2])
                self.places.append(temp_list)

            infile.close()

            return self.places

        except IOError as error:
            print("I/O error: {}".format(error))

    # save list to 'csv' file
    def save_places(self, file_name):

        try:
            infile = open(file_name, "w")
            writer = csv.writer(infile)
            writer.writerows(self.places)
            infile.close()

            return self.places

        except IOError as error:
            print("I/O error: {}".format(error))

    # add place to list
    def add_place(self, place):
        try:
            places_test = str(place)
            add_list = places_test.split(",")
            add_list[2] = int(add_list[2])

            # visit state is boolean. Need to change "n" or "v"
            if add_list[3] == " False":
                add_list[3] = "n"
            elif add_list[3] == " True":
                add_list[3] = "v"

            infile = open(FILE_NAME, 'a')
            self.places.append(add_list)
            infile.close()

            return self.places

        except IOError as error:
            print("I/O error: {}".format(error))

    # sort list by name, priority, country, or visit state
    def sort(self, sort_by):
        try:
            if sort_by == "priority":
                self.places.sort(key=lambda priority: priority[2], reverse=True)
            elif sort_by == "name":
                self.places.sort(key=lambda name: name[0])
            elif sort_by == "country":
                self.places.sort(key=lambda country: country[1])
            elif sort_by == "is_visited":
                self.places.sort(key=lambda is_visited: is_visited[3], reverse=True)
            return self.places

        except IOError as error:
            print("I/O error: {}".format(error))

    # check how many places visited
    def get_num_of_unvisited(self):
        try:
            un_visit = 0
            for line in self.places:
                un_visit += line[3].count("n")

            print("{} place(s) unvisited".format(un_visit))

        except IOError as error:
            print("I/O error: {}".format(error))
