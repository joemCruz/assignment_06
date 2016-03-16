import math     # For all of the math used
# import utils

from utils import generate_rand_points
# ------------------------------------------------------------------
#
# Joseph Cruz
# analytics.py
#
# Stores the functions from point_pattern.py that perform analysis
# on data.
# ------------------------------------------------------------------

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# function mean_nearest_neighbors_randomPoints
#
# Determines the mean nearest neighbor of randomly generated points
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def permutations(p = 99, n = 100):
    list_means = []

    for i in range(p):
        # randPoints = utils.generate_rand_points(n)
        rand_points = generate_rand_points(n)
        newMean = average_nearest_neighbor_distance(rand_points)
        list_means.append(newMean)

    return list_means

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# function find_crit_points
#
# Finds the critical points (min and max) of a list
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def find_crit_points(list_means):
    entries = list_means
    maxEntry = 0
    minEntry = 2
    for i in range(len(list_means)):
        if entries[i] > maxEntry:
            maxEntry = entries[i]
        if entries[i] < minEntry:
            minEntry = entries[i]

    return minEntry,maxEntry

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# function crit_point_check
#
# Checks if the observed value is within the range of the min and max
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def crit_point_check(minEntry, maxEntry, observed):
    if observed < minEntry or observed > maxEntry:
        return True
    else:
        return False


def mean_center(points):
    """
    Given a set of points, compute the mean center

    Parameters
    ----------
    points : list
         A list of points in the form (x,y)

    Returns
    -------
    x : float
        Mean x coordinate

    y : float
        Mean y coordinate
    """
    x = 0
    y = 0
    numOfPoints = len(points)

    for i in range(numOfPoints):
        x = x + points[i][0]
        y = y + points[i][1]

    x = x/numOfPoints
    y = y/numOfPoints
    
    return x, y

def average_nearest_neighbor_distance(points):
    """
    Given a set of points, compute the average nearest neighbor.

    Parameters
    ----------
    points : list
             A list of points in the form (x,y)

    Returns
    -------
    mean_d : float
             Average nearest neighbor distance

    References
    ----------
    Clark and Evan (1954 Distance to Nearest Neighbor as a
     Measure of Spatial Relationships in Populations. Ecology. 35(4)
     p. 445-453.
    """
    mean_d = 0
    total = 0
    local_nn = 0
    numOfPoints = len(points)

    for i in range(numOfPoints):
        local_nn = 0 #reset local_nn for the new point
        for j in range(numOfPoints):
            if i != j:
                newDistance = euclidean_distance(points[i],points[j])
                if local_nn == 0:
                    local_nn = newDistance
                elif newDistance < local_nn:
                    local_nn = newDistance

        total = total + local_nn
        
    mean_d = total/numOfPoints
        

    return mean_d


def minimum_bounding_rectangle(points):
    """
    Given a set of points, compute the minimum bounding rectangle.

    Parameters
    ----------
    points : list
             A list of points in the form (x,y)

    Returns
    -------
     : list
       Corners of the MBR in the form [xmin, ymin, xmax, ymax]
    """
    mbr = [0,0,0,0]
    numOfPoints = len(points)
    for i in range(numOfPoints):
        #Check for min and max x
        if points[i][0] < mbr[0]:
            mbr[0] = points[i][0]
        if points[i][0] > mbr[2]:
            mbr[2] = points[i][0]
        #Check for min and max y
        if points[i][1] < mbr[1]:
            mbr[1] = points[i][1]
        if points[i][1] > mbr[3]:
            mbr[3] = points[i][1]

    return mbr


def mbr_area(mbr):
    """
    Compute the area of a minimum bounding rectangle
    """
    area = (mbr[2] - mbr[0])*(mbr[3] - mbr[1])

    return area


def expected_distance(area, n):
    """
    Compute the expected mean distance given
    some study area.

    This makes lots of assumptions and is not
    necessarily how you would want to compute
    this.  This is just an example of the full
    analysis pipe, e.g. compute the mean distance
    and the expected mean distance.

    Parameters
    ----------
    area : float
           The area of the study area

    n : int
        The number of points
    """

    expected = (1/2)*math.sqrt(area/n)
    return expected

def manhattan_distance(a, b):
    """
    Compute the Manhattan distance between two points

    Parameters
    ----------
    a : tuple
        A point in the form (x,y)

    b : tuple
        A point in the form (x,y)

    Returns
    -------
    distance : float
               The Manhattan distance between the two points
    """
    distance =  abs(a[0] - b[0]) + abs(a[1] - b[1])
    return distance


def euclidean_distance(a, b):
    """
    Compute the Euclidean distance between two points

    Parameters
    ----------
    a : tuple
        A point in the form (x,y)

    b : tuple
        A point in the form (x,y)

    Returns
    -------

    distance : float
               The Euclidean distance between the two points
    """
    distance = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    return distance

def check_coincident(a, b):
    """
    Check whether two points are coincident
    Parameters
    ----------
    a : tuple
        A point in the form (x,y)

    b : tuple
        A point in the form (x,y)

    Returns
    -------
    equal : bool
            Whether the points are equal
    """
    return a == b


def check_in(point, point_list):
    """
    Check whether point is in the point list

    Parameters
    ----------
    point : tuple
            In the form (x,y)

    point_list : list
                 in the form [point, point_1, point_2, ..., point_n]
    """
    return point in point_list

