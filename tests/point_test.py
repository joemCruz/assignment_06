from .. import point
import unittest
import random


class TestPointClass(unittest.TestCase):

    def set_up(self):
        pass

    def test_point_pattern(self):
        random.seed(12345)
        rand_tuple = (random.randint(0,10),random.randint(0,10))
        check_point = point.Point(rand_tuple[0],rand_tuple[1],"some mark")
        """ Tests that the point is being set correctly """
        self.assertEqual(check_point.x, 6)
        self.assertEqual(check_point.y, 0)

        """ Tests to insure coincidence is read properly """
        rand_tuple2 = (random.randint(0,10),random.randint(0,10))
        copy_point = point.Point(6,0,"balrog")
        check_point2 = point.Point(rand_tuple2[0],rand_tuple2[1],"some other mark")
        self.assertTrue(check_point.coincident(copy_point))
        self.assertFalse(check_point.coincident(check_point2))

        """ Tests for shift_point """
        pos_shift_point = point.Point(rand_tuple[0],rand_tuple[1],"some mark")
        neg_shift_point = point.Point(rand_tuple[0],rand_tuple[1],"some mark")

        pos_shift_point.shift_point(rand_tuple2[0],rand_tuple2[1])
        self.assertTrue(pos_shift_point.x == 10 and pos_shift_point.y == 5)

        neg_shift_point.shift_point(-rand_tuple2[0],-rand_tuple2[1])
        self.assertTrue(neg_shift_point.x == 2 and neg_shift_point.y == -5)

    def test_marks(self):
        list_of_points = []
        marks = ["elf", "dwarf", "human", "orc"]
        random.seed(12345)
        list_of_points = point.create_random_marked_points(20,marks)

        elf_counter = 0
        human_counter = 0
        dwarf_counter = 0
        orc_counter = 0

        for i in range(len(list_of_points)):
            if list_of_points[i].mark == "elf":
                elf_counter += 1
            elif list_of_points[i].mark == "human":
                human_counter += 1
            elif list_of_points[i].mark == "dwarf":
                dwarf_counter += 1
            elif list_of_points[i].mark == "orc":
                orc_counter += 1

        self.assertEqual(elf_counter, 4)
        self.assertEqual(human_counter, 5)
        self.assertEqual(dwarf_counter, 8)
        self.assertEqual(orc_counter, 3)

    def test_nearest_neightbor(self):
        random.seed(12345)
        marks = ["elf", "dwarf", "human", "orc"]
        list_of_points = point.create_random_marked_points(20,marks)

        distance_no_mark = point.average_nearest_neighbor_distance(list_of_points)
        distance_with_mark = point.average_nearest_neighbor_distance(list_of_points,"orc")

        self.assertAlmostEqual(distance_no_mark, 0.13861788961152158, 5)
        self.assertAlmostEqual(distance_with_mark, 0.253406515134334, 5)