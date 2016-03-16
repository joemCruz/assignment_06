import random
import unittest

from .. import io_geojson
from .. import point


class TestFunctionalPointPattern(unittest.TestCase):

    def setUp(self):
        random.seed(12345)
        i = 0
        marks = ["elf", "dwarf", "human", "orc"]
        rand_marks = []
        for i in range(100):
            rand_marks.append(random.choice(marks))

        self.points = []
        while i < 100:
            seed = point.Point(round(random.random(),2), round(random.random(),2), rand_marks[i])
            self.points.append(seed)
            n_additional = random.randint(5,10)
            i += 1
            c = random.choice([0,1])
            if c:
                for j in range(n_additional):
                    x_offset = random.randint(0,10) / 100
                    y_offset = random.randint(0,10) / 100
                    pt = point.Point(round(seed.x + x_offset, 2), round(seed.y + y_offset,2), random.choice(marks))
                    self.points.append(pt)
                    i += 1
                    if i == 100:
                        break
            if i == 100:
                break

    def test_point_pattern(self):
        """
        This test checks that the code can compute an observed mean
         nearest neighbor distance and then use Monte Carlo simulation to
         generate some number of permutations.  A permutation is the mean
         nearest neighbor distance computed using a random realization of
         the point process.
        """
        marks = ["elf", "dwarf", "human", "orc"]
        random.seed()  # Reset the random number generator using system time
        # I do not know where you have moved avarege_nearest_neighbor_distance, so update the point_pattern module
        observed_avg_elf = point.average_nearest_neighbor_distance(self.points,"elf")
        self.assertAlmostEqual( 0.02555, observed_avg_elf, 3)
        observed_avg_dwarf = point.average_nearest_neighbor_distance(self.points,"dwarf")
        self.assertAlmostEqual( 0.02555, observed_avg_dwarf, 3)
        observed_avg_human = point.average_nearest_neighbor_distance(self.points,"human")
        self.assertAlmostEqual( 0.02555, observed_avg_human, 3)
        observed_avg_orc = point.average_nearest_neighbor_distance(self.points,"orc")
        self.assertAlmostEqual( 0.02555, observed_avg_orc, 3)
        # Again, update the point_pattern module name for where you have placed the point_pattern module
        # Also update the create_random function name for whatever you named the function to generate
        #  random points
        rand_points = point.create_random_marked_points(100,marks)
        self.assertEqual(100, len(rand_points))

        # As above, update the module and function name.
        permutations = point.permutations(99)
        self.assertEqual(len(permutations), 99)
        self.assertNotEqual(permutations[0], permutations[1])

        # As above, update the module and function name.
        lower, upper = point.find_crit_points(permutations)
        self.assertTrue(lower > 0.03)
        self.assertTrue(upper < 0.07)
        self.assertTrue(observed_avg_elf < lower or observed_avg_elf > upper)

        # As above, update the module and function name.
        significant = point.crit_point_check(lower, upper, observed_avg_elf)
        self.assertTrue(significant)

