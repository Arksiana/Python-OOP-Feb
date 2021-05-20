from abc import ABC, abstractmethod


class Animal(ABC):
    def eat(self):
        pass


class SoundMakingAnimal(Animal, ABC):
    @abstractmethod
    def get_sound(self):
        pass


class Mole(Animal):
    # Example of violation
    def get_sound(self):
        raise TypeError('Moles cannot make sounds')


class Cat(SoundMakingAnimal):
    sound = 'meow'

    def get_sound(self):
        return self.sound


class Dog(SoundMakingAnimal):
    sound = 'woof-woof'

    def get_sound(self):
        return self.sound


class Chicken(SoundMakingAnimal):
    sound = 'quack'

    def get_sound(self):
        return self.sound


class Donkey(SoundMakingAnimal):
    sound = 'im talking donkey'

    def get_sound(self):
        return self.sound


def animal_sound(animals: list):
    for animal in animals:
        print(animal.get_sound())


def animal_eat(animals: list):
    for animal in animals:
        print(animal.eat())


animals = [Cat(), Dog(), Chicken(), Donkey()]
animal_sound(animals)
animal_eat(animals + [Mole()])

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни - DONE
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
