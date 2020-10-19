import datetime
import math
pi = 22 / 7


def add():
    num1 = float(input("Enter the number"))
    num2 = float(input("Enter the second number"))
    return num1 + num2


def subtract():
    num1 = float(input("Enter the number"))
    num2 = float(input("Enter the second number"))
    return num1 - num2


def multiply():
    num1 = float(input("Enter the number"))
    num2 = float(input("Enter the second number"))
    return num1 * num2


def divide():
    num1 = float(input("Enter the number"))
    num2 = float(input("Enter the second number"))
    return num1 / num2


def sin():
    num = float(input("Enter the number"))
    return math.sin(num)


def cos():
    num = float(input("Enter the number"))
    return math.cos(num)


def tan():
    num = int(input("Enter the number "))
    return math.tan(num)


def factorial():
    num = int(input("Enter the number"))
    return math.factorial(num)


def power():
    num1 = int(input('Enter the number'))
    num2 = int(input('Enter the power'))
    return num1**num2


def root():
    num1 = int(input('Enter the number'))
    num2 = int(input('Enter the power'))
    if num2 != 0 and num2 > 0:
        return num1**1 / num2

# physics


def speed():
    distance = int(input("Enter the distance"))
    time = int(input("Enter th etime"))
    return distance / time


def velocity():
    displacement = int(input("Enter the displacement"))
    time = int(input("Enter th etime"))
    return displacement / time


def time():
    return datetime.datetime.now()


def time_from():
    distance = float(input("Enter the distance/displacement"))
    speed = float(input("Enter the speed/velocity"))
    # speed = d/t time
    return distance / speed


def distance_from():
    " Gives you the distance from time and velocity"

    time = float(input("Enter the time"))
    speed = float(input("Enter the speed/velocity"))
    # s=d/t => d= s x t
    return time * speed

# shapes
# shapes only


class Square():
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

    def perimeter(self):
        return self.side * 4


class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.length + self.width)


def Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius**2)

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Trapezium():
    def __init__(self, base1, base2, height):
        self.height = height
        self.base1 = base1
        self.base2 = base2

    def area(self):
        area = self.height / 2 * (self.base1 + self.base2)
        return area

    def perimeter(self):
        # TODO: Add an advanced formula
        pass


class Cylinder():
    def __init__(self, radius, height):
        self.height = height
        self.radius = radius

    def volume(self):
        circle_area = pi * (self.radius**2)
        volume = circle_area * self.height
        return volume

    def total_surface_area(self):
        total_circle_area = 2 * (pi * (self.radius**2))
        rect_area = self.height * (pi * 2 * self.radius)
        return rect_area + total_circle_area

    def lateral_surface_area(self):
        rect_area = self.height * (pi * 2 * self.radius)
        return rect_area


class Triangle():
    def __init__(self):
        pass

    def area(self):
        method = int(input('''
how do u want to calculate the area
1) b * h * 1/2
2) heron's formula
        '''))
        if method == 2:
            side1 = float(input('Enter the side'))
            side2 = float(input('Enter the side'))
            side3 = float(input('Enter the side'))
            s = (side1 + side2 + side3) / 2
            return (s * (s - side1) * (s - side2) * (s - side3))**0.5

        else:
            base = float(input('Enter the base'))
            height = float(input('Enter the height'))
            return 1 / 2 * base * height

    def perimeter(self):
        side1 = float(input('Enter the side'))
        side2 = float(input('Enter the side'))
        side3 = float(input('Enter the side'))
        return side1 + side2 + side3


class Cuboid():
    def __init__(self, height, length, width):
        self.height = height
        self.length = length
        self.width = width

    def volume(self):
        return self.length*self.height*self.width

    def total_surface_area(self):
        lb = self.length * self.width
        bh = self.height * self.width
        lh = self.length * self.height
        return 2*(lb+bh+lh)
    # todo:
    # def lateral_surface_area(self):


class Cube():
    def __init__(self, side):
        self.side = side

    def volume(self):
        return self.side**3

    def total_surface_area(self):
        return 6*(self.side**2)

    def lateral_surface_area(self):
        return 4*(self.side**2)


# testing
# rect = Rectangle(length=20, width=30)
# rect.area()
