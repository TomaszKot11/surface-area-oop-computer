from figure import Figure
from decimal import Decimal

class Cube(Figure):
  def __init__(self, a):
    self.a = Decimal(a)

  def get_surface_area(self):
    return Decimal(6) * self.a

  def get_capacity(self):
    return pow(self.a, 3)