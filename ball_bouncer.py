"""
The ball bouncing object itself, and all its logic.

You probably don't want to edit this directly, but referencing it might give you an idea of some of the things you can modify!
"""

import random
import turtle
import inspect

box_side_length = 350

__author__ = "Becky"

class BallBouncer(object):
  
  def __init__(self):
    ### A few things to alter ###
    self.gravity = 0.2
    self.x_vel = 8
    self.y_vel = 2
    self.x_pos = 50
    self.y_pos = 200
    ############################
    self.frame = 1
    self.selectable_methods = []
    self.recurring_methods_to_call = {}
    self.screen = turtle.Screen()
    self.screen.setup(0, 0, box_side_length, box_side_length)
    self.screen.colormode(255)
    self.screen.setworldcoordinates(0, 0, box_side_length, box_side_length)
    self.turtle = turtle.Turtle()
    self.turtle.ht()
    self.turtle.speed(0)
    self.turtle.shape("circle")
    self.turtle.penup()
    self.turtle.goto(self.x_pos, self.y_pos)
    self.turtle.st()
    self.turtle.pendown()
    
  def update_physics(self):
    if self.x_pos < 3 or self.x_pos > box_side_length-3:
      self.x_vel *= -1
    if self.y_pos < 3 or self.y_pos > box_side_length-3: 
      self.y_vel *= -1
    self.x_pos += self.x_vel
    self.y_pos += self.y_vel
    self.y_vel -= self.gravity
    self.turtle.goto(self.x_pos, self.y_pos)
    
  def add_randomly_selectable_method(self, function, description):
    author = inspect.getmodule(function).__author__
    self.selectable_methods.append({"author": author,
                                    "description": description,
                                    "function": function})
        
  def add_randomly_selectable_recurring_method(self, function, description):
    author = inspect.getmodule(function).__author__
    def gen_func(self, author, description, function):
      def anon_func(self):
        self.recurring_methods_to_call[author+"'s \""+description+"\""] = function
      return anon_func

    self.selectable_methods.append({
      "author": author,
      "description": description,
      "function": gen_func(self, author, description, function)
    })
    
  def call_random(self):
    if len(self.selectable_methods) == 0: return
    chosen = random.choice(self.selectable_methods)
    print("Calling {}'s \"{}\"".format(chosen["author"],
                                        chosen["description"]))
    chosen["function"](self)

  def update_recurrers(self):
    for f in self.recurring_methods_to_call.values():
      f(self)

  def cull_one_recurring(self):
    if len(self.recurring_methods_to_call.keys()) == 0:
      print("Nothing to stop!")
      return
    to_remove = random.choice(list(self.recurring_methods_to_call.keys()))
    self.recurring_methods_to_call.pop(to_remove)  
    print("Stopped "+to_remove)