from polygon import Polygon
import turtle,math

t = turtle.Turtle()
t.hideturtle()
t.screen.title("Devil Star")

devil_star = Polygon(0,0,300,5,18)
devil_star.initialize()

devil_star.vertex_list[1],devil_star.vertex_list[2],devil_star.vertex_list[3],devil_star.vertex_list[4] = devil_star.vertex_list[2],devil_star.vertex_list[4],devil_star.vertex_list[1],devil_star.vertex_list[3]

devil_star.simulate(-10,50,t)

turtle.done()
