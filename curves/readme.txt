This folder contains two scripts which draw the same 5 curves as follows : 

Lower left hand corner or 3rd quadrant : 

x = sin(i) + 0.5 cos(5i) + 0.25 sin(13i) , y = cos(i) + 0.5 sin(5i) + 0.25 cos(13i)

Upper left hand corner or 2nd quadrant : 

x = sin(i) - sin(2.3i) , y = cos(i)

Lower right hand corner or 4th quadrant : 

x = sin(i) + 0.5 sin(5i) + 0.25 cos(2.3i) , y = cos(i) + 0.5 cos(5i) + 0.25 sin(2.3i)

Upper right hand corner or 1st quadrant :

r = sin(2.4i)^2 + cos(2.4i)^4

Centerscreen : 

r = sin(1.2i)^2 + cos(6i)^3

The first and larger script :

curves_demo.py

takes the traditional approach of replicating the same sequence of steps for every curve.

The second and smaller script :

curves_lambda.py

uses lambdas to minimize the code by passing the x and y expressions to the method which draws them.

Another take which produces a shorter overall code and is more Pythonic although the script size is larger than curves_lambda.py is 

curves_lamda_list.py

which stores all the curve parameters in a list of dictionaries, even the lambda expressions are stored as key-value pairs in the dictionaries.

Uses the Python default math module and the default turtle module which internally uses tkinter.

On Windows and Linux

python3 <script name>

or

python <script name>

If it fails on Windows, check whether tcl/tkinter is installed.

On Linux ( Ubuntu like distros )

apt install python3-tk

The scripts may fail on WSL due to known compatibility issues with tkinter.
