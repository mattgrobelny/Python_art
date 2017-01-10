import cairocffi as cairo
import sys
import getopt
import math
import numpy as np
import uuid
import random
# prints a unique_filename for each drawing
unique_filename = str(uuid.uuid4())

###############################################################################
#
# Define the path to file
outpath = '/Users/matt/github/Python_art/recursive_art/' + \
    unique_filename[0:6] + '_art_tree.pdf'

height = 1080
width = 1920
ps = cairo.PDFSurface(str(outpath), float(width), float(height))
cr = cairo.Context(ps)

# paint background
cr.set_source_rgb(0.0, 0.0, 0.0)  # black
cr.rectangle(0, 0, width, height)
cr.fill()

# stroke a thicker line
cr.set_line_width(1.5)

# Drawing parameters
rotate_angle = 120
line_shrink_rate = 0.8
min_line_length = 15

# Draw a tree with trunk length : line_length


def draw_branch(line_length):
    # create first line
    cr.move_to(0, 0)
    cr.line_to(0, -1 * line_length)
    cr.translate(0, -1 * line_length)
    cr.stroke()

    if line_length > min_line_length:
        # draw one branch
        # Use cr.save() to push current context onto stack
        cr.save()
        cr.rotate(np.radians(rotate_angle))
        draw_branch(line_length * line_shrink_rate)
        cr.stroke()
        # Use cr.restore() to pop current context from stack
        cr.restore()

        # draw the inverse branch
        # Use cr.save() to push current context onto stack
        cr.save()
        cr.rotate(np.radians(-rotate_angle))
        draw_branch(line_length * line_shrink_rate)
        cr.stroke()
        # Use cr.restore() to pop current context from stack
        cr.restore()
##################################

# added random shrinkage


def draw_three_branches(line_length):
    # create first line
    cr.move_to(0, 0)
    cr.line_to(0, -1 * line_length)
    cr.translate(0, -1 * line_length)
    cr.stroke()

    if line_length > min_line_length:
        # draw one branch
        # Use cr.save() to push current context onto stack
        cr.save()
        cr.rotate(np.radians(rotate_angle))
        draw_three_branches(
            line_length * random.uniform(0.5, line_shrink_rate))
        cr.stroke()
        # Use cr.restore() to pop current context from stack
        cr.restore()

        # draw the inverse branch
        # Use cr.save() to push current context onto stack
        cr.save()
        cr.rotate(np.radians(rotate_angle / 2))
        draw_three_branches(
            line_length * random.uniform(0.5, line_shrink_rate))
        cr.stroke()
        # Use cr.restore() to pop current context from stack
        cr.restore()

        # draw the inverse branch
        # Use cr.save() to push current context onto stack
        cr.save()
        cr.rotate(np.radians(-rotate_angle))
        draw_three_branches(
            line_length * random.uniform(0.5, line_shrink_rate))
        cr.stroke()
        # Use cr.restore() to pop current context from stack
        cr.restore()


def draw_tree(x_start, y_start, size, c1, c2, c3, angle, shrink, min_line):

    # Drawing parameters
    global rotate_angle
    rotate_angle = angle

    global line_shrink_rate
    line_shrink_rate = shrink

    global min_line_length
    min_line_length = min_line
    cr.save()
    cr.translate(x_start, y_start)
    cr.set_source_rgb(c1, c2, c3)
    draw_branch(size)
    cr.restore()

# Stack multiple trees on top of each other and color them with different
# colors
draw_tree(width / 2.0, height / 1.6, 400, 0.4, 0.5, 0.19, 130, 0.8, 15)

draw_tree(width / 2.0, height / 1.6, 400, 0.12, 0.8, 0.9, 130, 0.8, 20)

draw_tree(width / 2.0, height / 1.6, 400, 0.82, 0.7, 0.17, 130, 0.8, 30)

draw_tree(width / 2.0, height / 1.6, 400, 0.12, 0.8, 0.4, 130, 0.8, 40)

draw_tree(width / 2.0, height / 1.6, 400, 0.1, 0.0, 0.9, 130, 0.8, 50)

cr.show_page()
