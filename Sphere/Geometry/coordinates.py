import math

tolerance: float = 0.0000000001

def degrees_to_radians(degrees: float) -> float:
    return (degrees * math.pi) / 180

def radians_to_degrees(radiants: float) -> float:
    return (radiants * 180) / math.pi

class CartesianCoordinates:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

class SphericalCoordinate:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    ## Up to a rescaling we may assume points lie on the unit sphere
    ## Therefore, the spherical distance is simply the central angle
    def calculate_spherical_distance(self, other_spherical_coordinate) -> float:
        delta_longitude: float = math.abs(self.longitude - other_spherical_coordinate.longitude)
        central_angle: float = math.acos(
            math.sin(degrees_to_radians(self.Latitude)) * math.sin(degrees_to_radians(other_spherical_coordinate.Latitude))
            + math.cos(degrees_to_radians(self.latitude)) * math.cos(degrees_to_radians(other_spherical_coordinate.latitude)) * math.cos(delta_longitude)
            )
        return central_angle
    
    ## Can think of as distance from A to B then distance from B to C
    ## For which B has the latitude of A and the longitude of C
    ## If longitude is unchanged distance is just delta latitude
    def calculate_manhattan_spherical_distance(self, other_spherical_coordinate) -> float:
        midpoint: SphericalCoordinate = SphericalCoordinate(self.latitude, other_spherical_coordinate.longitude)
        distance_self_to_midpoint: float = self.calculate_spherical_distance(midpoint)
        distance_midpoint_to_other: float = math.abs(self.latitude - other_spherical_coordinate.latitude)
        return distance_self_to_midpoint + distance_midpoint_to_other

class CoordinateConverter:
    def cartesian_to_spherical(cartesian_coordinates: CartesianCoordinates) -> SphericalCoordinate:
        longitude: float = 90 if math.abs(cartesian_coordinates.x) < tolerance else radians_to_degrees(math.atan(cartesian_coordinates.y / cartesian_coordinates.x))
        latitude: float = radians_to_degrees(math.acos(cartesian_coordinates.z))
        return SphericalCoordinate(longitude, latitude)

    def spherical_to_cartesian(spherical_coordinates: SphericalCoordinate) -> CartesianCoordinates:
        return CartesianCoordinates(
            x = math.sin(degrees_to_radians(spherical_coordinates.latitude)) * math.cos(degrees_to_radians(spherical_coordinates.longitude)),
            y = math.sin(degrees_to_radians(spherical_coordinates.latitude)) * math.sin(degrees_to_radians(spherical_coordinates.longitude)),
            z = math.cos(degrees_to_radians(spherical_coordinates.latitude)))
     