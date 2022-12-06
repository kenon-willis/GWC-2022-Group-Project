"""
Use this file as a template for your own! Set your name and add any functions you'd like. When you're ready to go, add this file to main.py like this:

import becky_funcs

and "register" your functions like this:

bb.add_randomly_selectable_method(becky_funcs.invert_gravity,
                                  "invert gravity")


If your name was Matilda, you might name this file matilda_funcs.py and:

import matilda_funcs

and "register" like:

bb.add_randomly_selectable_method(matilda_funcs.invert_gravity,
                                  "invert gravity")

So module.function_name first, then a description of what it's going to do
"""

from math import sin

__author__ = "Brody"

def willis_head(simulation):
	simulation.screen.register_shape("willis.gif")
	simulation.turtle.shape("willis.gif")