import turtle
import math

t = turtle.Turtle()

t.screen.title("Parametric Curves")

x_center,y_center,radius,steps = 0,0,150,1000

factor = 10.5*math.pi/steps

t.penup()
t.color("red")

for i in range(steps):
  t.goto(x_center + radius * (math.sin(1.2 * i * factor)**2 + math.cos(6 * i * factor)**3) * math.cos(i*factor),
         y_center + radius * (math.sin(1.2 * i * factor)**2 + math.cos(6 * i * factor)**3) * math.sin(i*factor))
  t.pendown()

x_center,y_center = 450,210

factor = 12*math.pi/steps

t.penup()
t.color("blue")

for i in range(steps):
  t.goto(x_center + radius * (math.sin(2.4 * i * factor)**2 + math.cos(2.4 * i * factor)**4) * math.cos(i*factor),
         y_center + radius * (math.sin(2.4 * i * factor)**2 + math.cos(2.4 * i * factor)**4) * math.sin(i*factor))
  t.pendown()

x_center,y_center = 450,-210

factor = 23*math.pi/steps

t.penup()
t.color("green")

for i in range(steps):
  t.goto(x_center + radius * (math.sin(i * factor) + 0.5 * math.sin(5 * i * factor) + 0.25 * math.cos(2.3 * i * factor)),
         y_center + radius * (math.cos(i * factor) + 0.5 * math.cos(5 * i * factor) + 0.25 * math.sin(2.3 * i * factor)))
  t.pendown()

x_center,y_center = -450,-210

factor = 2.1*math.pi/steps

t.penup()
t.color("brown")

for i in range(steps):
  t.goto(x_center + radius * (math.sin(i * factor) + 0.5 * math.cos(5 * i * factor) + 0.25 * math.sin(13 * i * factor)),
         y_center + radius * (math.cos(i * factor) + 0.5 * math.sin(5 * i * factor) + 0.25 * math.cos(13 * i * factor)))
  t.pendown()

x_center,y_center = -450,210

factor = 23*math.pi/steps

t.penup()
t.color("orange")

for i in range(steps):
  t.goto(x_center + radius * (math.sin(i * factor) - math.sin(2.3 * i * factor)),
         y_center + radius * math.cos(i * factor))
  t.pendown()

turtle.done()
