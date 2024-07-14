from polygon import Polygon
import turtle

triangle = Polygon(0,0,300,3,90)
triangle.initialize()

square = Polygon(-150,-150,180,4,0)
square.initialize()

pentagon = Polygon(-150,300,180,5,30)
pentagon.initialize()

decagon = Polygon(-140,250,210,10,36)
decagon.initialize()

t = turtle.Turtle()
t.hideturtle()

t.screen.title("Valiant Recreation")

t.color("blue")
decagon.simulate(-30,45,t)

t.color("green")
square.simulate(-10,25,t)

t.color("orange")
pentagon.simulate(-5,55,t)

t.color("red")
triangle.simulate(-10,36,t)

turtle.done()
