from rectangle import Rectangle
from triangle import Triangle
from cube import Cube
from oval import Oval
from shapely_pyramid import ShapelyPyramid

# uses standard naming conventions in math e.g
# H - the height of the 3D figure
# h - height of 2D figure or one side of the 3D figure
# n - number of edges
class Dispatcher:
  def __init__(self):
    # TODO: private property
    self.switcher = {
      0: self.triangle,
      1: self.rectangle,
      2: self.square,
      3: self.cube,
      4: self.shapely_pyramid, # ostrosłup foremny
      5: self.oval,
      6: self.exit
    }

  def get_surface_and_capacity(self, option):
    function_to_call = self.switcher.get(option, self.exit)
    return function_to_call()

  # TODO: private methods? -> encapsulate
  def rectangle(self):
    a = input("Insert a: ")
    b = input("Insert b: ")
    rectangle = Rectangle(a, b)
    return (True, rectangle)

  def square(self):
    a = input("Insert a: ")
    square = Rectangle(a, a)
    return (True, square)

  def triangle(self):
    a = input("Insert a: ")
    h = input("Insert h: ")
    triangle = Triangle(a, h)
    return (True, triangle)

  def shapely_pyramid(self):
    n = input("Insert n: ")
    a = input("Insert a: ")
    r = input("Insert r: ")
    h = input("Insert h: ")
    H = input("Insert H: ")
    shapely_pyramid = ShapelyPyramid(n, a, r, H, h)
    return (True, shapely_pyramid)

  def oval(self):
    a = input("Insert a: ")
    b = input("Insert b: ")
    oval = Oval(a, b)
    return (True, oval)

  def cube(self):
    a = input("Insert a: ")
    cube = Cube(a)
    return (True, cube)

  def exit(self):
    print('Thank you for using our calculator! See you soon! ♡')
    return (False, [])






