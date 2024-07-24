from polygon import Polygon
import turtle,math

t = turtle.Turtle()
t.hideturtle()
t.screen.title("Devil Star")

twisted_hexagon = Polygon(0,0,300,6,45)
twisted_hexagon.initialize()

twisted_hexagon.vertex_list[0],twisted_hexagon.vertex_list[1],twisted_hexagon.vertex_list[2],twisted_hexagon.vertex_list[3],twisted_hexagon.vertex_list[4],twisted_hexagon.vertex_list[5] = [-225,375],[225,375],[-225,0],[225,-375],[-225,-375],[225,0]

twisted_hexagon.simulate(-10,30,t)

turtle.done()
