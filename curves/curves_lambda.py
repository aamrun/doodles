import turtle
import math

def draw_curve(pen,x_center,y_center,radius,steps,factor,x_expr,y_expr,colour):

  pen.penup()
  pen.color(colour)

  for i in range(steps):
    pen.goto(x_center + radius * x_expr(i * factor),y_center + radius * y_expr(i * factor))
    pen.pendown()

t = turtle.Turtle()

t.screen.title("Parametric Curves")

x_expr = lambda i : (math.sin(1.2 * i)**2 + math.cos(6 * i)**3) * math.cos(i)
y_expr = lambda i : (math.sin(1.2 * i)**2 + math.cos(6 * i)**3) * math.sin(i)

draw_curve(t,0,0,150,1000,10.5*math.pi/1000,x_expr,y_expr,"red")

x_expr = lambda i : (math.sin(2.4 * i)**2 + math.cos(2.4 * i)**4) * math.cos(i)
y_expr = lambda i : (math.sin(2.4 * i)**2 + math.cos(2.4 * i)**4) * math.sin(i)

draw_curve(t,450,210,150,1000,12*math.pi/1000,x_expr,y_expr,"blue")

x_expr = lambda i : math.sin(i) + 0.5 * math.cos(5 * i) + 0.25 * math.sin(13 * i)
y_expr = lambda i : math.cos(i) + 0.5 * math.sin(5 * i) + 0.25 * math.cos(13 * i)

draw_curve(t,-450,-210,150,1000,2.1*math.pi/1000,x_expr,y_expr,"brown")

x_expr = lambda i : math.sin(i) + 0.5 * math.sin(5 * i) + 0.25 * math.cos(2.3 * i)
y_expr = lambda i : math.cos(i) + 0.5 * math.cos(5 * i) + 0.25 * math.sin(2.3 * i)

draw_curve(t,450,-210,150,1000,23*math.pi/1000,x_expr,y_expr,"green")

x_expr = lambda i : math.sin(i) - math.sin(2.3 * i)
y_expr = lambda i : math.cos(i)

draw_curve(t,-450,210,150,1000,23*math.pi/1000,x_expr,y_expr,"orange")

turtle.done()
