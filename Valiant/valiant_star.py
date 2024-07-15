from polygon import Polygon
import turtle,math

star_params = [{"x_center":-761,"y_center":200,"circumradius":300,"arms":3,"orientation_in_degrees":0,"innerradius":100},
               {"x_center":590,"y_center":230,"circumradius":300,"arms":4,"orientation_in_degrees":-30,"innerradius":100},
               {"x_center":660,"y_center":-200,"circumradius":300,"arms":7,"orientation_in_degrees":0,"innerradius":100},
               {"x_center":-630,"y_center":-210,"circumradius":300,"arms":6,"orientation_in_degrees":0,"innerradius":100},
               {"x_center":0,"y_center":0,"circumradius":450,"arms":5,"orientation_in_degrees":0,"innerradius":150}]

t = turtle.Turtle()
t.hideturtle()
t.screen.title("Stars")

#starry = Polygon(star_params[0]["x_center"],star_params[0]["y_center"],star_params[0]["circumradius"],2*star_params[0]["arms"],star_params[0]["orientation_in_degrees"])
#starry.initialize()
#starry.starify(star_params[0]["innerradius"])
#starry.simulate(-10,120,t)
for star in star_params:

  starry = Polygon(star["x_center"],star["y_center"],star["circumradius"],2*star["arms"],star["orientation_in_degrees"])
  starry.initialize()
  starry.starify(star["innerradius"])
  starry.simulate(-10,120,t)

turtle.done()
