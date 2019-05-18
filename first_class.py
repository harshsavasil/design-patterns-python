import math


class Point:
    """
    A Class representing a point in a 2d geometry.
    """

    def __init__(self, x=0, y=0):
        """
        Method that initializes the new point with the co-ordinates passed
        or else the deafault position i.e. origin is passed.
        """
        self.move(x, y)

    def move(self, x, y):
        """
        Move the point to new location in 2d space.
        """
        self.x = x
        self.y = y

    def reset(self):
        """
        Reset the position of the point to origin.
        """
        self.move(0, 0)

    def calculate_distance(self, other_point):
        """
        Calculations the distance between the current point and other point using Pythagoras Theorem.
        """
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y)**2)
