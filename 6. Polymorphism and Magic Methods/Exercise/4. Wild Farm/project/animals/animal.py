from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, weight):
        self.food_eaten = 0
        self.name = name
        self.weight = weight

    def make_sound(self):
        pass

    def feed(self, food, grams):
        pass

    def gain_weight(self, grams, food):
        self.weight += food.quantity * grams
        self.food_eaten += food.quantity


class Bird(Animal):
    @abstractmethod
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    @abstractmethod
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
