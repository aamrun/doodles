import math

class Polygon:

    def __init__(self,center_x,center_y,circumradius,num_vertices,rotation_in_degrees):
      self.center_x = center_x
      self.center_y = center_y
      self.circumradius = circumradius
      self.num_vertices = num_vertices
      self.rotation_in_degrees = rotation_in_degrees
      self.vertex_list = []

    def initialize(self):
      for vertex in range(self.num_vertices):
        self.vertex_list.append([self.center_x + self.circumradius * math.cos(math.radians(vertex * 360/self.num_vertices) + math.radians(self.rotation_in_degrees)),
                              self.center_y + self.circumradius * math.sin(math.radians(vertex * 360/self.num_vertices) + math.radians(self.rotation_in_degrees))])

    def draw(self,turtle):
      turtle.penup()
      turtle.goto(self.vertex_list[0][0],self.vertex_list[0][1])
      for vertex in self.vertex_list[1:]:
        turtle.pendown()
        turtle.goto(vertex[0],vertex[1])
      turtle.goto(self.vertex_list[0][0],self.vertex_list[0][1])        
      
