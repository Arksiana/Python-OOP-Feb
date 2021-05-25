import math


class Shape:
    def perimeter(self):
        pass

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * self.radius * math.pi

    def area(self):
        return self.radius * self.radius * math.pi


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.height + self.width)

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Serializer:
    def serialize(self, obj):
        pass


class JsonSerializer(Serializer):
    def serialize(self, obj):
        pass


class TextSerializer(Serializer):
    def serialize(self, obj):
        pass


def get_serializer(type):
    if type == 'json':
        return JsonSerializer()
    else:
        return TextSerializer


type = 'json'
serializer = get_serializer(type)
print(serializer.serialize(Square(3)))


def print_shape(s: Shape):
    print(f"Inside func with {s.__class__.__name__}")
    print(f"Perimeter is: {s.perimeter()}")
    print(f"Area is: {s.area()}")


def print_shapes(shapes: [Shape]):
    for s in shapes:
        print(f"Inside func with {s.__class__.__name__}")
        print(f"Perimeter is: {s.perimeter()}")
        print(f"Area is: {s.area()}")


circle = Circle(10)
rect = Rectangle(5, 4)

# print_shapes([
#     circle,
#     rect,
#     Shape(),
#     Square(4),
# ])

# print_shape(circle)
# print_shape(rect)
