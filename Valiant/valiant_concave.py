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


arrowhead = Polygon(0,0,300,4,0)
arrowhead.initialize()

arrowhead.vertex_list[2] = [0,0]
arrowhead.vertex_list[1][0],arrowhead.vertex_list[3][0] = -300,-300

concave_pentagon = Polygon(-600,210,250,5,72)
concave_pentagon.initialize()

concave_pentagon.vertex_list[2] = [-600,210]

concave_hexagon = Polygon(600,300,250,6,-30)
concave_hexagon.initialize()

concave_hexagon.vertex_list[2] = [600,300]

concave_heptagon = Polygon(-660,-210,250,7,-90)
concave_heptagon.initialize()

concave_heptagon.vertex_list[2] = [-660,-210]

concave_nonagon = Polygon(600,-210,250,9,-45)
concave_nonagon.initialize()

concave_nonagon.vertex_list[2] = [600,-210]

t = turtle.Turtle()

t.hideturtle()

t.screen.title("Concave Polygons")

simulate(arrowhead,-10,45,t)

simulate(concave_pentagon,-10,45,t)

simulate(concave_hexagon,-10,45,t)

simulate(concave_heptagon,-10,50,t)

simulate(concave_nonagon,-10,72,t)

turtle.done()
