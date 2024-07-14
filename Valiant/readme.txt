Recreates the Valiant demo image as shown in Valiant.jpg using Python's standard turtle module.

Requires tkinter. 

On Linux, you may need to install it e.g. for Ubuntu : 

apt install python3-tk

On Windows ensure that tcl/tk/tkinter is installed.

Unstable on WSL due to known issues with tkinter code running on WSL.

The modules are as follows : 

polygon.py : Polygon class representing a regular polygon defined by it's center, circumradius, number of sides and rotation or phase.

vector2d.py : Vector class providing unit vector functionality.

valiant_demo.py : Demo script which includes the above two in addition to the turtle module.

To run the demo :

On Windows

python valiant_demo.py

or

python3 valiant_demo.py

Tested on Python 3.x, may work with Python 2.x but not guaranteed.

Have fun !
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

valiant_concave.py demonstrates the pursuit simulation for 5 concave quadrilaterals starting with the arrowhead ( concave analogue of the square ), concave pentagon, 
concave hexagon, concave heptagon and concave nonagon.

Unlike their convex counterparts, the concave polygons are not symmetric and similar as they contract. The concave quadrilaterals change into convex ones, the sides are unequal and thenumber of sides also decrease.

The concave quadrilaterals do not remain within their bounds as they contract.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
valiant_star.py demonstrates the same simulation on a 5 pointed star. 
The generated image shows the rich texture and geometry of such creations.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
simulate method was added to the Polygon class and valiant scripts were refactored.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
