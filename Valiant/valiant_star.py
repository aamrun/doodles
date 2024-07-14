from polygon import Polygon
from vector2d import Vector2D
import turtle,math

def simulate(polygon,velocity,steps,turtle):

  for step in range(steps):
    polygon.draw(turtle)
    unit_vectors = []  
    for vertex in range(polygon.num_vertices):
      unit_vectors.append(Vector2D(polygon.vertex_list[vertex % polygon.num_vertices][0],polygon.vertex_list[vertex % polygon.num_vertices][1],
                                   polygon.vertex_list[(vertex+1) % polygon.num_vertices][0],polygon.vertex_list[(vertex+1) % polygon.num_vertices][1]).unit_vector())

    for vertex in range(polygon.num_vertices):
      polygon.vertex_list[(vertex + 1) % polygon.num_vertices][0] += (unit_vectors[vertex][1][0] - unit_vectors[vertex][0][0])*velocity
      polygon.vertex_list[(vertex + 1) % polygon.num_vertices][1] += (unit_vectors[vertex][1][1] - unit_vectors[vertex][0][1])*velocity

star = Polygon(0,0,450,10,0)
star.initialize()

for i in range(1,10,2):
  star.vertex_list[i][0],star.vertex_list[i][1] = 150*math.cos(i*2*math.pi/10),150*math.sin(i*2*math.pi/10)  
  
t = turtle.Turtle()

t.hideturtle()

t.screen.title("Star")

simulate(star,-10,120,t)

turtle.done()
