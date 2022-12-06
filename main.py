# The prototype group project for Granada GWC 2022
# A simple physics simulation--a ball bouncing in a box--rolls a random method to call every 100 frames
# Programmers are welcomed to register their own methods! The more there are, the more unpredictable the simulation becomes

from ball_bouncer import BallBouncer

import becky_funcs
import vaidehi_funcs
import prisha_funcs
import brody_funcs
import shirley_funcs

bb = BallBouncer()
####################  Add your methods to the pool here   ##############
bb.add_randomly_selectable_method(becky_funcs.invert_gravity, "invert gravity")
bb.add_randomly_selectable_method(
    becky_funcs.wipe_screen,
    "screen wiper",
)

bb.add_randomly_selectable_method(becky_funcs.double_speed, "double_speed")
bb.add_randomly_selectable_method(becky_funcs.half_speed, "half speed")
bb.add_randomly_selectable_recurring_method(becky_funcs.set_rainbow, "rainbow")
bb.add_randomly_selectable_method(BallBouncer.cull_one_recurring, "wipeout")
############################set_screen_white##################
bb.add_randomly_selectable_method(vaidehi_funcs.cat_head, "whites out screen")
bb.add_randomly_selectable_method(shirley_funcs.stop, "stops ball short")

bb.add_randomly_selectable_method(prisha_funcs.shapeChanger, "Shape Changer")
bb.add_randomly_selectable_method(prisha_funcs.triple_speed, "triple speed")
bb.add_randomly_selectable_method(shirley_funcs.add_vel, "adds velocity")
########################################################
bb.add_randomly_selectable_method(brody_funcs.willis_head, "WILLIS HEAD")

######  MAIN LOOP, DON'T EDIT ######
while (True):
    if bb.frame % 100 == 0:
        bb.call_random()
    bb.update_physics()
    bb.update_recurrers()
    bb.frame += 1
####################################

#while (True):
#    if bb.frame % 100 == 0:
#        bb.call_random()date_physics()
#    bb.update_recurrers()
#    bb.frame += 1
