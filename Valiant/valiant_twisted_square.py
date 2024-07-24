from polygon import Polygon
import turtle,math

t = turtle.Turtle()
t.hideturtle()
t.screen.title("Devil Star")

twisted_square = Polygon(0,0,300,4,45)
twisted_square.initialize()

twisted_square.vertex_list[2],twisted_square.vertex_list[3] = twisted_square.vertex_list[3],twisted_square.vertex_list[2]

twisted_square.simulate(-10,50,t)

turtle.done()
