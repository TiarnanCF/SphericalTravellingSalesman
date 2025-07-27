import unittest
from Sphere.Geometry.coordinates import Coordinates
from Sphere.Geometry.geometries import *
import math

class MockCoordinates(Coordinates):

    def __init__(self, distance: float):
        self.distance = distance

    def calculate_distance(self, other_coordinates) -> float:
        return self.distance - other_coordinates.distance

    def calculate_manhattan_distance(self, other_coordinates) -> float:
        return self.distance - other_coordinates.distance

class TestGeometryMethods(unittest.TestCase):

    def setUp(self):
        self.mock_coordinates: list[MockCoordinates] = [MockCoordinates(12), MockCoordinates(1), MockCoordinates(11), MockCoordinates(33)]
        self.corner_coordinates: MockCoordinates = self.mock_coordinates[1]
        self.comparison_coordinates: MockCoordinates = MockCoordinates(4)

    def test_calculate_furthest_coordinate_distance(self):
        self.assertEqual(29, calculate_furthest_coordinate_distance(self.mock_coordinates, self.comparison_coordinates))

    def test_calculate_corner_coordinate(self):
        corner_coordinates: MockCoordinates = calculate_corner_coordinate(self.mock_coordinates)
        self.assertIs(corner_coordinates, self.corner_coordinates)

if __name__ == '__main__':
    unittest.main()