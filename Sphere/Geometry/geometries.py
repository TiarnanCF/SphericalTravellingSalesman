from coordinates import SphericalCoordinate

class Sphere:
    def __init__(self):
        self.spherical_coordinates: list[SphericalCoordinate] = []

    def __init__(self, spherical_coordinates: list[SphericalCoordinate]):
        self.spherical_coordinates = spherical_coordinates

    def add_point(self, spherical_coordinate: SphericalCoordinate) -> None:
        self.spherical_coordinates.append(spherical_coordinate)

    def add_points(self, spherical_coordinates: list[SphericalCoordinate]) -> None:
        self.spherical_coordinates.extend(spherical_coordinates)