from decimal import Decimal
from math import pi as PI
from figure import Figure

class Oval(Figure):
  def __init__(self, a, b):
    self.a = Decimal(a)
    self.b = Decimal(b)

  def get_surface_area(self):
    return self.a * self.b * Decimal(PI)

  def get_capacity(self):
    return None