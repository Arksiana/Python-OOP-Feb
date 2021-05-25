import math
import time


class Person:

    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

    def __repr__(self):
        return '; '.join(f"{key}={value}" for (key, value) in self.__dict__.items())


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


def get_values(obj, attr_names):
    return [getattr(obj, attr_name) for attr_name in attr_names]


class Tracker:
    def __init__(self):
        self.last_id = 0
        self.object = []

    def add_object(self, obj):
        self.last_id += 1
        setattr(obj, 'track_id', self.last_id)
        self.object.append(obj)

    def track(self):
        while True:
            for obj in self.object:
                print(getattr(obj, "track_id", None))
            time.sleep(2)


tracker = Tracker()
tracker.add_object(Person('Pesho', 11, 'Burgas', "Bulgaria"))
tracker.add_object(Circle(4))

tracker.track()
