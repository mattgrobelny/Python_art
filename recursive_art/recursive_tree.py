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

height = 1000
width = 1000
ps = cairo.PDFSurface(str(outpath), float(height), float(width))
cr = cairo.Context(ps)

# paint background
cr.set_source_rgb(0.0, 0.0, 0.0)  # black
cr.rectangle(0, 0, height, width)
cr.fill()


# stroke a thicker line
cr.set_line_width(3)

# create first line

cr.set_source_rgb(0.5, 0.1, 0.4)
line_length = -300
cr.translate(width / 2.0, height)
cr.move_to(0, 0)
cr.line_to(0, line_length)

# translate to end of first line
cr.translate(0, line_length)

cr.stroke()

shrink_factor = 0.7

# size of first branch
line_length = -200

# line color
cr.set_source_rgb(0.5, 0.1, 0.4)

# curve back rate [0.5 to 1]
curve_back = 0.5
degree_split = 20

branch_vertex_array = []


def recursive_line_3(n):
    if n == 0:
        return "done"
    global branch_vertex_array
elif n > 1:
        global line_length
        line_length = line_length * shrink_factor
        x_new = line_length
        y_new = line_length * -1
        branch_vertex_array.append([x_new, y_new])

        cr.move_to(0, 0)
        cr.rotate(np.radians((1 + curve_back) * degree_split * n * .8))
        cr.line_to(x_new, y_new)
        cr.stroke()

        cr.translate(x_new, y_new)
        return recursive_line_3(n)
    elif len(branch_vertex_array) != 0:
        x, y = branch_vertex_array.pop()
        cr.translate(x, y)

        x_new = line_length
        y_new = line_length * -1

        cr.rotate(-np.radians((1 + curve_back) *
                              degree_split * n * .8))
        cr.move_to(0, 0)
        cr.line_to(x_new, y_new)
        cr.stroke()
        branch_vertex_array.append([x_new, y_new])
        n -= 1
        print n
        return recursive_line_3(n)
recursive_line_3(100)

cr.show_page()
