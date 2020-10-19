from calc import *
from basicfunc import *
what = input('''
Choose figure:
1) Square
2) Rectangle
3) Triangle
4) Circle
5) Cuboid
6) Cube
7) Cylinder
''')
try:
    what = int(what)
except ValueError:
    print('You have not entered a number')
if what == 1:
    s = Square(side=take_input_as_float('Enter the side'))
    print(f'Area - {s.area()}\nPerimeter - {s.perimeter()}')
elif what == 2:
    r = Rectangle(length=take_input_as_float('Enter the length'),
                  width=take_input_as_float('Enter the width'))
    print(f'Area - {r.area()}\nPerimeter-{r.perimeter()}')
elif what == 3:
    t = Triangle()
    choice = int(
        input('What do you want to do ? \n1) calculate area\n2)Perimeter'))
    if choice == 1:
        t.area()
    else:
        t.perimeter()
elif what == 4:
    c = Circle(radius=take_input_as_float('Enter the radius'))
    print(f'The area is {c.area()}\nThe perimeter is {c.perimeter()} ')
elif what == 5:
    c = Cuboid(height=take_input_as_float('Enter the height'), width=take_input_as_float(
        'ENter the width'), length=take_input_as_float('Enter the length'))
    print(f'The volume {c.volume()}\nThe area - {c.area()}')
elif what == 6:
    c = Cube(side=take_input_as_float('Enter the side'))
    print(
        f'The Total Surface Area is {c.total_surface_area()}\n The Lateral Surface Area is {c.lateral_surface_area()}\n The volume is {c.volume()} ')
elif what == 7:
    c = Cylinder(radius=take_input_as_float('Enter the radius'),
                 height=take_input_as_float('Enter the height'))
    print(f'''
The total surface area is - {c.total_surface_area()}
The lateral surface area is  - {c.lateral_surface_areaI()}
the volume is - {c.volume()}
    ''')
else:
    a = type(what)
    if a == "str":
        print('You have not entered a number')
    else:
        print('The number was not from the given numbers')
