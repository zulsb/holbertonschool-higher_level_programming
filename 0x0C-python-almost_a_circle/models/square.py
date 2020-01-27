#!/usr/bin/python3
from .rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        if args:
            ar = ["id", "size", "x", "y"]
            for k, v in zip(ar, args):
                setattr(self, k, v)
        else:
            if kwargs is not None:
                for k, v in kwargs.items():
                    setattr(self, k, v)

    def to_dictionary(self):
        dinary = {}
        ar = ["id", "size", "x", "y"]

        for i in ar:
            dinary[i] = getattr(self, i)
        return(dinary)
