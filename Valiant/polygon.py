from vector2d import Vector2D
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
    
    def starify(self,innerradius):
      self.innerradius = innerradius
      for i in range(1,self.num_vertices,2):
        self.vertex_list[i][0],self.vertex_list[i][1] = self.center_x + self.innerradius*math.cos(i*2*math.pi/self.num_vertices),self.center_y + self.innerradius*math.sin(i*2*math.pi/self.num_vertices)

    def simulate(self,velocity,steps,turtle):
    
      for step in range(steps):
        self.draw(turtle)
        unit_vectors = []
        for vertex in range(self.num_vertices):
          unit_vectors.append(Vector2D(self.vertex_list[vertex % self.num_vertices][0],self.vertex_list[vertex % self.num_vertices][1],
                                       self.vertex_list[(vertex+1) % self.num_vertices][0],self.vertex_list[(vertex+1) % self.num_vertices][1]).unit_vector())
    
        for vertex in range(self.num_vertices):
          self.vertex_list[(vertex + 1) % self.num_vertices][0] += (unit_vectors[vertex][1][0] - unit_vectors[vertex][0][0])*velocity
          self.vertex_list[(vertex + 1) % self.num_vertices][1] += (unit_vectors[vertex][1][1] - unit_vectors[vertex][0][1])*velocity

    def draw(self,turtle):
      turtle.penup()
      turtle.goto(self.vertex_list[0][0],self.vertex_list[0][1])
      for vertex in self.vertex_list[1:]:
        turtle.pendown()
        turtle.goto(vertex[0],vertex[1])
      turtle.goto(self.vertex_list[0][0],self.vertex_list[0][1])        
