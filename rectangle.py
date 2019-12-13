from figure import Figure
from decimal import Decimal

# every square is also the rectangle
class Rectangle(Figure):

  def __init__(self, a, b):
    self.a = Decimal(a)
    self.b = Decimal(b)

  def get_surface_area(self):
    return self.a * self.b

  def get_capacity(self):
    return None
