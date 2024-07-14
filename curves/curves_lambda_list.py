import turtle
import math

curves_list = [{"x_center":0,"y_center":0,"circumradius":150,"steps":1000,"multiplier":10.5,"colour":"red",
                "x_expr": lambda i :(math.sin(1.2 * i)**2 + math.cos(6 * i)**3) * math.cos(i),"y_expr": lambda i :(math.sin(1.2 * i)**2 + math.cos(6 * i)**3) * math.sin(i)},
               {"x_center":450,"y_center":210,"circumradius":150,"steps":1000,"multiplier":12,"colour":"blue",
                "x_expr": lambda i :(math.sin(2.4 * i)**2 + math.cos(2.4 * i)**4) * math.cos(i),"y_expr": lambda i :(math.sin(2.4 * i)**2 + math.cos(2.4 * i)**4) * math.sin(i)},
               {"x_center":-450,"y_center":-210,"circumradius":150,"steps":1000,"multiplier":2.1,"colour":"brown",
                "x_expr": lambda i :math.sin(i) + 0.5 * math.cos(5 * i) + 0.25 * math.sin(13 * i),"y_expr": lambda i :math.cos(i) + 0.5 * math.sin(5 * i) + 0.25 * math.cos(13 * i)},
               {"x_center":450,"y_center":-210,"circumradius":150,"steps":1000,"multiplier":23,"colour":"green",
                "x_expr": lambda i :math.sin(i) + 0.5 * math.sin(5 * i) + 0.25 * math.cos(2.3 * i),"y_expr": lambda i :math.cos(i) + 0.5 * math.cos(5 * i) + 0.25 * math.sin(2.3 * i)},
               {"x_center":-450,"y_center":210,"circumradius":150,"steps":1000,"multiplier":23,"colour":"orange",
                "x_expr": lambda i :math.sin(i) - math.sin(2.3 * i),"y_expr": lambda i :math.cos(i)}]

def draw_curve(pen,x_center,y_center,radius,steps,factor,x_expr,y_expr,colour):

  pen.penup()
  pen.color(colour)

  for i in range(steps):
    pen.goto(x_center + radius * x_expr(i * factor),y_center + radius * y_expr(i * factor))
    pen.pendown()

t = turtle.Turtle()

t.screen.title("Parametric Curves")

for curve in curves_list:

  draw_curve(t,curve["x_center"],curve["y_center"],curve["circumradius"],curve["steps"],curve["multiplier"]*math.pi/curve["steps"],curve["x_expr"],curve["y_expr"],curve["colour"])

turtle.done()
