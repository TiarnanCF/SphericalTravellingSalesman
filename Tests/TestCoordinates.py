import unittest
from Sphere.Geometry.coordinates import *
import math

class TestAngleConversionMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_degrees_to_radians(self):
        self.assertAlmostEqual(2*math.pi, degrees_to_radians(360))
        self.assertAlmostEqual(math.pi, degrees_to_radians(180))
        self.assertAlmostEqual(math.pi / 2, degrees_to_radians(90))

    def test_radians_to_degrees(self):
        self.assertAlmostEqual(360, radians_to_degrees(2*math.pi))
        self.assertAlmostEqual(180, radians_to_degrees(math.pi))
        self.assertAlmostEqual(90, radians_to_degrees(math.pi / 2))

class TestCartestianCoordinates(unittest.TestCase):

    def setUp(self):
        self.coordinates = [CartesianCoordinates(-3,2.3,4), CartesianCoordinates(-1,0,0), CartesianCoordinates(0,6.3,4)]

    def test_init(self):
        x: float = 1
        y: float = 2.7
        z: float = 3.5

        coordinates: CartesianCoordinates = CartesianCoordinates(x,y,z)
        self.assertTrue(isinstance(coordinates, CartesianCoordinates))
        self.assertEqual(coordinates.x, x)
        self.assertEqual(coordinates.y, y)
        self.assertEqual(coordinates.z, z)
        
    def test_calculate_distance(self):
        self.assertAlmostEqual(self.coordinates[0].calculate_distance(self.coordinates[2]), 5)
        
    def test_calculate_manhattan_distance(self):
        self.assertAlmostEqual(self.coordinates[0].calculate_manhattan_distance(self.coordinates[0]), 0)
        self.assertAlmostEqual(self.coordinates[0].calculate_manhattan_distance(self.coordinates[1]), 8.3)
        self.assertAlmostEqual(self.coordinates[0].calculate_manhattan_distance(self.coordinates[2]), 7)
        self.assertAlmostEqual(self.coordinates[1].calculate_manhattan_distance(self.coordinates[1]), 0)
        self.assertAlmostEqual(self.coordinates[1].calculate_manhattan_distance(self.coordinates[2]), 11.3)
        self.assertAlmostEqual(self.coordinates[2].calculate_manhattan_distance(self.coordinates[2]), 0)


if __name__ == '__main__':
    unittest.main()