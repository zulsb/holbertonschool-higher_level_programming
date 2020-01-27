#!/usr/bin/python3
"""
    Module contains Square class.
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle.
        Args:
            Rectangle: Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Get the size of square. """
        return self.width

    @size.setter
    def size(self, value):
        """ Set the value of square.
            Args:
                value: Value of square.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """ Return string representation of square. """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """ Function to update the class Square by adding the public method.
            Args:
                args: Is the list of arguments - no-keyworded arguments.
                kwargs: keyworded arguments.
        """
        if args:
            ar = ["id", "size", "x", "y"]
            for k, v in zip(ar, args):
                setattr(self, k, v)
        else:
            if kwargs is not None:
                for k, v in kwargs.items():
                    setattr(self, k, v)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle. """
        dinary = {}
        ar = ["id", "size", "x", "y"]

        for i in ar:
            dinary[i] = getattr(self, i)
        return(dinary)
