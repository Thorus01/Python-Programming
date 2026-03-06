"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains the abstract class Vehicle and other classes that
inherit from it.

@file vehicles.py
"""
import math
from abc import ABC, abstractmethod
from city import City, get_city_by_id
from country import find_country_of_city, create_example_countries
from itinerary import Itinerary

class Vehicle(ABC):
    """
    A Vehicle defined by a mode of transportation, which results in a specific duration.
    """

    @abstractmethod
    def compute_travel_time(self, departure: City, arrival: City) -> float:
        """
        Returns the travel duration of a direct trip from one city
        to another, in hours, rounded up to an integer.
        Returns math.inf if the travel is not possible.

        :param departure: the departure city.
        :param arrival: the arrival city.
        :return: the travel time in hours, rounded up to an integer,
                 or math.inf if the travel is not possible.
        """
        pass #pass as it's abstract, it's like a blueprint

    def compute_itinerary_time(self, itinerary: Itinerary) -> float:
        """
        Returns a travel duration for the entire itinerary for a given vehicle.
        Returns math.inf if any leg (i.e. part) of the trip is not possible.

        :param itinerary: The itinerary.
        :return: the travel time in hours (an integer),
                 or math.inf if the travel is not possible.
        """

        travel_duration = 0 #stores the accumulation of total travel time of itinerary
        for i in range(len(itinerary.cities) - 1): #iterate through the itinerary's cities
            start = itinerary.cities[i] #departure city denoted by iterator
            end = itinerary.cities[i + 1] #arrival city, +1 moves the iterator to next place
            new_duration = self.compute_travel_time(start, end) #computes travel time between the departure and arrival city
            if new_duration == math.inf: #if travel not possible return infinity
                return math.inf
            travel_duration += new_duration #adding everything together, the now computed new travel duration to the initialiser  
        return travel_duration #return the total travel time

    @abstractmethod
    def __str__(self) -> str:
        """
        Returns the class name and the parameters of the vehicle in parentheses.

        :return: the string representation of the vehicle.
        """
        pass #pass again as it's abstract

class CrappyCrepeCar(Vehicle):
    """
    A type of vehicle that:
        - Can go from any city to any other at a given speed.
    """

    def __init__(self, speed: int) -> None:
        """
        Creates a CrappyCrepeCar with a given speed in km/h.

        :param speed: the speed in km/h.
        """
        self.speed = speed #defining speed, it's an input

    def compute_travel_time(self, departure: City, arrival: City) -> float:
        """
        Returns the travel duration of a direct trip from one city
        to another, in hours, rounded up to an integer.

        :param departure: the departure city.
        :param arrival: the arrival city.
        :return: the travel time in hours, rounded up to an integer,
                 or math.inf if the travel is not possible.
        """    
        
        distance = departure.distance(arrival) #finding distance between departure and arrival locations
        speed = self.speed #defining the CCC's speed for the formula
        time = math.ceil(distance/speed) #our time formula rounded up
        if time == None: #if the travel not possible return infinity
             return math.inf
        return time #return the calculated travel time

    def __str__(self) -> str:
        """
        Returns the class name and the parameters of the vehicle in parentheses.
        For example "CrappyCrepeCar (100 km/h)"

        :return: the string representation of the vehicle.
        """
        return(f'CrappyCrepeCar ({str(self.speed)} km/h)') #returning the string name of the CCC and its inputted speed

class DiplomacyDonutDinghy(Vehicle):
    """
    A type of vehicle that:
        - Can travel between any two cities in the same country.
        - Can travel between two cities in different countries only if they are both "primary".
        - Has different speed for the two cases.
    """

    def __init__(self, in_country_speed: int, between_primary_speed: int) -> None:
        """
        Creates a DiplomacyDonutDinghy with two given speeds in km/h:
            - one speed for two cities in the same country.
            - one speed between two primary cities.

        :param in_country_speed: the speed within one country.
        :param between_primary_speed: the speed between two primary cities.
        """
        self.in_country_speed = in_country_speed #defining speed for DDD when travelling within one country an input
        self.between_primary_speed = between_primary_speed #defining speed when travelling between two primary cities (different country), an input

    def compute_travel_time(self, departure: City, arrival: City) -> float:
        """
        Returns the travel duration of a direct trip from one city
        to another, in hours, rounded up to an integer.
        Returns math.inf if the travel is not possible.

        :param departure: the departure city.
        :param arrival: the arrival city.
        :return: the travel time in hours, rounded up to an integer,
                 or math.inf if the travel is not possible.
        """
        distance = departure.distance(arrival) #defining distance again
        if distance == math.inf: #return infinity if distance not possible
            return math.inf
        elif find_country_of_city(departure) == find_country_of_city(arrival): #if two cities in the same country, return the travel time it took
            time = math.ceil(distance/self.in_country_speed) #our time formula again, but using DDD's in country speed
            return time
        elif departure.city_type == 'primary' and arrival.city_type == 'primary': #else calculate the time if the departure and arrival cities are both primary (capitals of a different country)
            time = math.ceil(distance/self.between_primary_speed) #our time formula again, but using DDD's between primary speed
            return time #return the time it took from the formula
        else:
            return math.inf #if the travel not possible return infinity

    def __str__(self) -> str:
        """
        Returns the class name and the parameters of the vehicle in parentheses.
        For example "DiplomacyDonutDinghy (100 km/h | 200 km/h)"

        :return: the string representation of the vehicle.
        """
        return(f'DiplomacyDonutDinghy ({str(self.in_country_speed)} km/h | {str(self.between_primary_speed)} km/h)') #returning the string name of the DDD and its two different inputted speeds

class TeleportingTarteTrolley(Vehicle):
    """
    A type of vehicle that:
        - Can travel between any two cities if the distance is less than a given maximum distance.
        - Travels in fixed time between two cities within the maximum distance.
    """

    def __init__(self, travel_time:int, max_distance: int) -> None:
        """
        Creates a TeleportingTarteTrolley with a distance limit in km.

        :param travel_time: the time it takes to travel.
        :param max_distance: the maximum distance it can travel.u 
        """
        self.travel_time = travel_time #defining TTT's travel time, an input
        self.max_distance = max_distance #defining TTT's maximum distance, an input

    def compute_travel_time(self, departure: City, arrival: City) -> float:
        """
        Returns the travel duration of a direct trip from one city
        to another, in hours, rounded up to an integer.
        Returns math.inf if the travel is not possible.

        :param departure: the departure city.
        :param arrival: the arrival city.
        :return: the travel time in hours, rounded up to an integer,
                 or math.inf if the travel is not possible.
        """

        distance = departure.distance(arrival) #defining the distance again
        if distance < self.max_distance: #if the distance is less than TTT's max travel distance possible we can return the travel time it took
            return self.travel_time
        else:
            return math.inf #else, if the travel is not possible, return infinity
    
    def __str__(self) -> str:
        """
        Returns the class name and the parameters of the vehicle in parentheses.
        For example "TeleportingTarteTrolley (5 h | 1000 km)"

        :return: the string representation of the vehicle.
        """
        return(f'TeleportingTarteTrolley ({str(self.travel_time)} h | {str(self.max_distance)} km)') #returning the string name of the TTT and its two different inputted travel time and max distance variables

def create_example_vehicles() -> list[Vehicle]:
    """
    Creates 3 examples of vehicles.

    :return: a list of 3 vehicles.
    """
    return [CrappyCrepeCar(200), DiplomacyDonutDinghy(100, 500), TeleportingTarteTrolley(3, 2000)]

if __name__ == "__main__":
    #we create some example cities
    create_example_countries()

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
            for vehicle in vehicles:
                print(f"\t{vehicle.compute_travel_time(from_city, to_city)} hours with {vehicle}.")
