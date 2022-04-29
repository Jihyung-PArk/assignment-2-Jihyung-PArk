"""
Filename: palce.py
github URL: https://github.com/Jihyung-PArk/assignment-2-Jihyung-PArk.git
"""


class Place:
    """..."""
    def __init__(self, name="", country="", priority=0, is_visited=False):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        return "{}, {}, {}, {}".format(self.name,
                                       self.country, self.priority, self.is_visited)

    # Change visit statement visit <-> un-visit
    def toggle_visited_status(self):
        self.is_visited = not self.is_visited

    # If priority is 1 or 2, priority is important.
    def is_important_place(self):
        return self.priority <= 2
