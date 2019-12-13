from figure import Figure
from decimal import Decimal

# https://pl.wikipedia.org/wiki/Ostros%C5%82up_prawid%C5%82owy
class ShapelyPyramid(Figure):
  def __init__(self, n, a, r, H, h):
    self.n = Decimal(n)
    self.a = Decimal(a)
    self.r = Decimal(r)
    self.H = Decimal(H)
    self.h = Decimal(h)

  def get_surface_area(self):
    return self.n / Decimal(2) * (self.a * self.h)

  def get_capacity(self):
    return (self.n * self.a * self.r * self.h) / Decimal(6)