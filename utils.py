import math    #For all of the math used
import random  # For random used
# ------------------------------------------------------------------
#
# Joseph Cruz
# utils.py
#
# Stores the functions from point_pattern.py that are a form of
# utility needed for use in other functions
# ------------------------------------------------------------------

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# function generate_rand_points()
#
# Generates an integer number of random points based on user input
# Points will be within the domain [0,1]
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def generate_rand_points(n):
    rng = random.Random()
    listofPoints = [(random.uniform(0,1), random.uniform(0,1)) for i in range(n)]
                    
    return listofPoints
    
def shift_point(point, x_shift, y_shift):
    """
    Shift a point by some amount in the x and y directions

    Parameters
    ----------
    point : tuple
            in the form (x,y)

    x_shift : int or float
              distance to shift in the x direction

    y_shift : int or float
              distance to shift in the y direction

    Returns
    -------
    new_x : int or float
            shited x coordinate

    new_y : int or float
            shifted y coordinate

    Note that the new_x new_y elements are returned as a tuple

    Example
    -------
    >>> point = (0,0)
    >>> shift_point(point, 1, 2)
    (1,2)
    """
    x = getx(point)
    y = gety(point)

    x += x_shift
    y += y_shift

    return x, y

def getx(point):
    """
    A simple method to return the x coordinate of
     an tuple in the form(x,y).  We will look at
     sequences in a coming lesson.

    Parameters
    ----------
    point : tuple
            in the form (x,y)

    Returns
    -------
     : int or float
       x coordinate
    """
    return point[0]


def gety(point):
    """
    A simple method to return the x coordinate of
     an tuple in the form(x,y).  We will look at
     sequences in a coming lesson.

    Parameters
    ----------
    point : tuple
            in the form (x,y)

    Returns
    -------
     : int or float
       y coordinate
    """
    return point[1]
