from sys import exception
from tkinter import CURRENT
from coordinates import SphericalCoordinate, Coordinate

half_way_longitude: float = 180

def calculate_furthest_coordinate_distance(coordinates: list[Coordinate], comparison_coordinate: Coordinate) -> float:
    if coordinates is None or len(coordinates) == 0:
        raise exception("At least one coordinate required")

    current_furthest_coordinate: Coordinate = next([x for x in coordinates if x is not comparison_coordinate], None)

    if current_furthest_coordinate is None:
        raise exception("At least one coordinate in list must be different from comparison coordinate")

    current_furthest_coordinate_distance: float = coordinate.calculate_distance(current_furthest_coordinate)

    for coordinate in coordinates: 
        if coordinate is comparison_coordinate:
            continue

        coordinate_distance: float = coordinate.calculate_distance(comparison_coordinate)
        if coordinate_distance < current_furthest_coordinate_distance:
            continue

        current_furthest_coordinate_distance = coordinate_distance
        current_furthest_coordinate = coordinate

    return current_furthest_coordinate_distance



def calculate_corner_coordinate(coordinates: list[Coordinate]):
    if coordinates is None or len(coordinates) == 0:
        raise exception("At least one coordinate required")

    if len(coordinates) == 1:
        return coordinates[0]

    corner_coordinate: Coordinate = coordinates[0]
    current_furthest_coordinate_distance: float = calculate_furthest_coordinate_distance(coordinates, corner_coordinate)

    for coordinate in coordinates:
        new_furthest_coordinate_distance: float = calculate_furthest_coordinate_distance(coordinates, coordinate)

        if new_furthest_coordinate_distance < current_furthest_coordinate_distance:
            continue

        corner_coordinate = coordinate
        current_furthest_coordinate_distance = new_furthest_coordinate_distance

    return corner_coordinate

class Sphere:
    def __init__(self):
        self.spherical_coordinates: list[SphericalCoordinate] = []

    def __init__(self, spherical_coordinates: list[SphericalCoordinate]):
        self.spherical_coordinates = spherical_coordinates

    def add_point(self, spherical_coordinate: SphericalCoordinate) -> None:
        self.spherical_coordinates.append(spherical_coordinate)

    def add_points(self, spherical_coordinates: list[SphericalCoordinate]) -> None:
        self.spherical_coordinates.extend(spherical_coordinates)

    def reset_points(self) -> None:
        self.spherical_coordinates = []

    def containing_longitudes(self) -> tuple[float, float]:
        longitudes = [x.longitude for x in self.spherical_coordinates]
        return (min(longitudes), max(longitudes))

    def containing_latitudes(self) -> tuple[float, float]:
        latitudes = [x.latitude for x in self.spherical_coordinates]
        return (min(latitudes), max(latitudes))

    def find_corner_point(self) -> SphericalCoordinate:
        (min_longitude, max_longitude): tuple[float, float] = self.containing_longitudes()
        if max_longitude - min_longitude > half_way_longitude:
            return None # Handle when coordinates span across more than one hemisphere

        return calculate_corner_coordinate(self.spherical_coordinates)
