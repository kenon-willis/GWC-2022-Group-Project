import random

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

__author__ = "Prisha Sheth"

my_list = ["triangle", "turtle", "square", "arrow"]

def shapeChanger(simulation):
    variable = random.choice(my_list)
    simulation.turtle.shape(variable)

def triple_speed(simulation):
    simulation.x_vel *= 3
    simulation.y_vel *= 3

def colorTrail(simulation):
    simulation.turtle.pencolor("purple")
    simulation.turtle.width(4)
    simulation.y_vel *= 3

def wipe_screen(simulation):
    simulation.turtle.clear()


def double_speed(simulation):
    simulation.x_vel *= 2
    simulation.y_vel *= 2


