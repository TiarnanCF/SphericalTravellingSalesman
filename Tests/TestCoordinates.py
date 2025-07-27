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
        self.assertIsInstance(coordinates, CartesianCoordinates)
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

class TestSphericalCoordinates(unittest.TestCase):

    def setUp(self):
        self.coordinates = [SphericalCoordinates(90,90), SphericalCoordinates(-156,30), SphericalCoordinates(-44,23), SphericalCoordinates(-44,57)]

    def test_init(self):

        longitude: float = 15.4
        latitude: float = 44.7

        coordinates: SphericalCoordinates = SphericalCoordinates(longitude, latitude)
        self.assertIsInstance(coordinates, SphericalCoordinates)
        self.assertEqual(coordinates.longitude, longitude)
        self.assertEqual(coordinates.latitude, latitude)
        
    def test_calculate_distance(self):
        self.assertAlmostEqual(self.coordinates[0].calculate_distance(self.coordinates[0]), 0)
        self.assertAlmostEqual(self.coordinates[1].calculate_distance(self.coordinates[2]),1.675,2)
        self.assertAlmostEqual(self.coordinates[2].calculate_distance(self.coordinates[3]),0.5934119456780721)
        
    def test_calculate_manhattan_distance(self):
        self.assertAlmostEqual(self.coordinates[0].calculate_manhattan_distance(self.coordinates[0]), 0)
        self.assertAlmostEqual(self.coordinates[2].calculate_manhattan_distance(self.coordinates[3]),0.5934119456780721)
        self.assertAlmostEqual(self.coordinates[1].calculate_manhattan_distance(self.coordinates[2]),1.724,2)

class TestCoordinateConverter(unittest.TestCase):

    def setUp(self):
        self.converter = CoordinateConverter()
        self.coordinates = [ 
            (SphericalCoordinates(90,90), CartesianCoordinates(0,1,0)),
            (SphericalCoordinates(0,90), CartesianCoordinates(1,0,0)),
            (SphericalCoordinates(0,0), CartesianCoordinates(0,0,1))]

    def test_cartesian_to_spherical(self):
        for coordinates_pair in self.coordinates:
            spherical_coordinates = CoordinateConverter.cartesian_to_spherical(coordinates_pair[1])
            self.assertAlmostEqual(spherical_coordinates.latitude, coordinates_pair[0].latitude)
            if spherical_coordinates.latitude not in (0, 180):
                self.assertAlmostEqual(spherical_coordinates.longitude, coordinates_pair[0].longitude)
        
    def test_spherical_to_cartesian(self):
        for coordinates_pair in self.coordinates:
            cartesian_coordinates = CoordinateConverter.spherical_to_cartesian(coordinates_pair[0])
            self.assertAlmostEqual(cartesian_coordinates.x, coordinates_pair[1].x)
            self.assertAlmostEqual(cartesian_coordinates.y, coordinates_pair[1].y)
            self.assertAlmostEqual(cartesian_coordinates.z, coordinates_pair[1].z)

if __name__ == '__main__':
    unittest.main()