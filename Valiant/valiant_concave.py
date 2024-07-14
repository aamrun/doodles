from polygon import Polygon
import turtle

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

arrowhead.simulate(-10,45,t)

concave_pentagon.simulate(-10,45,t)

concave_hexagon.simulate(-10,45,t)

concave_heptagon.simulate(-10,50,t)

concave_nonagon.simulate(-10,72,t)

turtle.done()
