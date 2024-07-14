from polygon import Polygon
import turtle,math

star = Polygon(0,0,450,10,0)
star.initialize()

for i in range(1,10,2):
  star.vertex_list[i][0],star.vertex_list[i][1] = 150*math.cos(i*2*math.pi/10),150*math.sin(i*2*math.pi/10)  
  
t = turtle.Turtle()

t.hideturtle()

t.screen.title("Star")

star.simulate(-10,120,t)

turtle.done()
