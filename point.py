import random
import math


class Point:
    """
    For whatever reason, cannot get import to work, just moved functionality
    into this file instead.
    """
    def __init__(self,x = 0,y = 0,mark = ""):
        self.x = x
        self.y = y
        self.mark = mark

    def shift_point(self,x_move,y_move):
        this_point = (self.x,self.y)
        self.x += x_move
        self.y += y_move

    def coincident(self, check_point):
        if check_point.x == self.x and check_point.y == self.y:
            return True
        else:
            return False


def create_random_marked_points(n, marks = []):
    list_of_tuples = [(random.uniform(0,1), random.uniform(0,1)) for i in range(n)]
    list_of_marks = [random.choice(marks) for i in range(n)]
    list_of_points = []
    for j in range(n):
        new_point = Point(list_of_tuples[j][0],list_of_tuples[j][1],list_of_marks[j])
        list_of_points.append(new_point)

    return list_of_points


def euclidean_distance(a, b):
    distance = math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
    return distance


def average_nearest_neighbor_distance(points, mark=""):
    mean_d = 0
    total = 0
    local_nn = 0
    num_of_points = len(points)

    if not mark:
        for i in range(num_of_points):
            local_nn = 0
            for j in range(num_of_points):
                if i != j:
                    new_distance = euclidean_distance(points[i],points[j])
                    if local_nn == 0:
                        local_nn = new_distance
                    elif new_distance < local_nn:
                        local_nn = new_distance

            total += local_nn

    else:
        for i in range(num_of_points):
            local_nn = 0
            for j in range(num_of_points):
                if i != j and points[i].mark == points[j].mark:
                    new_distance = euclidean_distance(points[i],points[j])
                    if local_nn == 0:
                        local_nn = new_distance
                    elif new_distance < local_nn:
                        local_nn = new_distance

            total += local_nn

    mean_d = total/num_of_points
    return mean_d


def permutations(p = 99, n = 100):
    list_means = []

    for i in range(p):
        marks = ["elf", "dwarf", "human", "orc"]
        rand_points = create_random_marked_points(n, marks)
        newMean = average_nearest_neighbor_distance(rand_points)
        list_means.append(newMean)

    return list_means


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


def crit_point_check(minEntry, maxEntry, observed):
    if observed < minEntry or observed > maxEntry:
        return True
    else:
        return False