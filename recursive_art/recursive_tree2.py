import cairocffi as cairo
import sys
import getopt
import math
import numpy as np
import uuid

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
rotate_angle = np.pi / 4
line_shrink_rate = 0.7

cr.set_source_rgb(0.5, 0.1, 0.4)
cr.translate(width / 2.0, height)


def draw_line(line_length):
    # create first line
    cr.set_source_rgb(0.5, 0.1, 0.4)
    cr.move_to(0, 0)
    cr.line_to(0, -1 * line_length)
    cr.translate(0, -1 * line_length)
    cr.stroke()

    if line_length > 2:
        # draw one branch
        # Use cr.save() to push current context onto stack
        cr.save()
        cr.rotate(rotate_angle)
        draw_line(line_length * line_shrink_rate)
        cr.stroke()
        # Use cr.restore() to pop current context from stack
        cr.restore()

        # draw the inverse branch
        # Use cr.save() to push current context onto stack
        cr.save()
        cr.rotate(-rotate_angle)
        draw_line(line_length * line_shrink_rate)
        cr.stroke()
        # Use cr.restore() to pop current context from stack
        cr.restore()

draw_line(300)

cr.show_page()
