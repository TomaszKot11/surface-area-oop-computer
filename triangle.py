from figure import Figure
from decimal import Decimal

class Triangle(Figure):

  def __init__(self, a, h):
    self.a = Decimal(a)
    self.h = Decimal(h)

  def get_surface_area(self):
    return Decimal(0.5) * (self.a * self.h)

  def get_capacity(self):
    return None
