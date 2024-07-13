import math

class Vector2D:

    def __init__(self,x1,y1,x2,y2):
      self.x1 = x1
      self.y1 = y1
      self.x2 = x2
      self.y2 = y2

    def abs(self):
      self.abs_value = math.sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)

    def unit_vector(self):
      self.abs()

      if self.abs_value == 0:
       return None

      return [[self.x1/self.abs_value,self.y1/self.abs_value],[self.x2/self.abs_value,self.y2/self.abs_value]]

