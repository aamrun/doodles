from polygon import Polygon
import turtle,math

t = turtle.Turtle()
t.hideturtle()
t.screen.title("Devil Star")

double_arrow = Polygon(0,0,300,4,45)
double_arrow.initialize()

double_arrow.vertex_list[0],double_arrow.vertex_list[1],double_arrow.vertex_list[2],double_arrow.vertex_list[3] = [-450,-225],[-225,225],[225,-225],[450,225]

double_arrow.simulate(-10,50,t)

turtle.done()
