from polygon import Polygon
from vector2d import Vector2D
import turtle

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


triangle = Polygon(0,0,300,3,90)
triangle.initialize()

square = Polygon(-150,-150,180,4,0)
square.initialize()

pentagon = Polygon(-150,300,180,5,30)
pentagon.initialize()

decagon = Polygon(-140,250,210,10,36)
decagon.initialize()

t = turtle.Turtle()

t.screen.title("Valiant Recreation")

t.color("blue")
simulate(decagon,-30,45,t)

t.color("green")
simulate(square,-10,25,t)

t.color("orange")
simulate(pentagon,-5,55,t)

t.color("red")
simulate(triangle,-10,36,t)

turtle.done()
