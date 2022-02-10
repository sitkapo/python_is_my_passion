
import unittest


def get_the_highest_number(w: List[int]) -> Tuple[int, int]:
    index = 0
    max_ = w[index]

    for i in range(1, len(w)):
        if w[i] >= max_:
            max_ = w[i]
            index = i

    return max_, index



class Z1Test(unittest.TestCase):

    def test_simple1(self):
        self.assertEqual(get_the_highest_number([5, 6, 8, 1, 2, 4]), (8, 2))

    def test_2_max_values(self):
        self.assertEqual(get_the_highest_number([5, 6, 8, 1, 2, 8]), (8, 5))

    def test_2values(self):
        self.assertEqual(get_the_highest_number([1, 2]), (2, 1))

    def test_2zeros(self):
        self.assertEqual(get_the_highest_number([0, 0]), (0, 1))


if __name__ == '__main__':
    unittest.main()