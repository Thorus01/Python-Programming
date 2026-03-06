"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a function to create a path, encoded as an Itinerary, that is shortest for some Vehicle.

@file path_finding.py
"""
import math
import networkx

from city import City, get_city_by_id
from itinerary import Itinerary
from vehicles import Vehicle, create_example_vehicles
from csv_parsing import create_cities_countries_from_csv


def find_shortest_path(vehicle: Vehicle, from_city: City, to_city: City) -> Itinerary | None:
    """
    Returns a shortest path between two cities for a given vehicle as an Itinerary,
    or None if there is no path.

    :param vehicle: The vehicle to use.
    :param from_city: The departure city.
    :param to_city: The arrival city.
    :return: A shortest path from departure to arrival, or None if there is none.
    """

    create_cities_countries_from_csv("worldcities_truncated.csv")
    G = networkx.Graph()    #creates an empty networkx graph
    
    for city in City.id_to_cities.values(): #adds all cities to the graph
        G.add_node(city)

    for i in City.id_to_cities.values():    #iterates through each city
        current_city_connections = []
        current_city = i
        for j in city.id_to_cities.values():    #connects each city to all cities that current vehicle can travel to from there
            destination = j
            if vehicle.compute_travel_time(from_city, to_city) != math.inf: #checks if vehicle can travel this link
                current_city_connections.append((current_city, destination, vehicle.compute_travel_time(current_city, destination)))
   
        G.add_weighted_edges_from(current_city_connections) #adds the edges to the graph

    if networkx.has_path(G, from_city, to_city) == True:    #checks if a path can be created
        return Itinerary(networkx.shortest_path(G, from_city, to_city)) #returns the successful path
    else:
        return None

if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")
    vehicles = create_example_vehicles()

    from_cities = set()
    for city_id in [1036533631, 1036142029, 1458988644]:
        from_cities.add(get_city_by_id(city_id))

    #we create some vehicles
    vehicles = create_example_vehicles()

    to_cities = set(from_cities)
    for from_city in from_cities:
        to_cities -= {from_city}
        for to_city in to_cities:
            print(f"{from_city} to {to_city}:")
            for test_vehicle in vehicles:
                shortest_path = find_shortest_path(test_vehicle, from_city, to_city)
                print(f"\t{test_vehicle.compute_itinerary_time(shortest_path)}"
                      f" hours with {test_vehicle} with path {shortest_path}.")

