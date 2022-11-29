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

__author__ = "Becky"


def invert_gravity(simulation):
    simulation.gravity = simulation.gravity * -1


def wipe_screen(simulation):
    simulation.turtle.clear()


def double_speed(simulation):
    simulation.x_vel *= 2
    simulation.y_vel *= 2


def half_speed(simulation):
    simulation.x_vel /= 2
    simulation.y_vel /= 2


def set_rainbow(simulation):
    color_offset = 128
    calc_time = simulation.frame % 640
    red = sin(0.01 * calc_time) * (color_offset - 1) + color_offset
    green = sin(0.01 * calc_time + 2) * (color_offset - 1) + color_offset
    blue = sin(0.01 * calc_time + 4) * (color_offset - 1) + color_offset
    simulation.screen.bgcolor(int(red), int(green), int(blue))
