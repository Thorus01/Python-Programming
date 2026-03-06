"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains the class Itinerary.

@file itinerary.py
"""
import math
from city import City, create_example_cities, get_cities_by_name

class Itinerary():
    """
    A sequence of cities.
    """

    def __init__(self, cities: list[City]) -> None:
        """
        Creates an itinerary with the provided sequence of cities,
        conserving order.
        :param cities: a sequence of cities, possibly empty.
        :return: None
        """
        self.cities = cities[:]

    def total_distance(self) -> int:
        """
        Returns the total distance (in km) of the itinerary, which is
        the sum of the distances between successive cities.
        :return: the total distance.
        """
        total = 0   #total distance
        for i in range(len(self.cities)-1): #iterates through each city except the last one as this causes an invalid index issue
            next_city = i+1
            total += self.cities[i].distance(self.cities[next_city])    #adds the distance between the current and next city
        return total

    def append_city(self, city: City) -> None:
        """
        Adds a city at the end of the sequence of cities to visit.
        :param city: the city to append
        :return: None.
        """
        self.cities.append(city) #appends the argument city to the list of cities

    def min_distance_insert_city(self, city: City) -> None:
        """
        Inserts a city in the itinerary so that the resulting
        total distance of the itinerary is minimised.
        :param city: the city to insert
        :return: None.
        """

        shortest_distance = 0

        for i in range(len(self.cities)):
            testlist = self.cities[:]
            testlist.insert(i, city)

            total = 0   #total distance
            for j in range(len(testlist)-1): #iterates through each city except the last one as this causes an invalid index issue
                next_city = j+1
                total += testlist[j].distance(testlist[next_city])    #adds the distance between the current and next city
            
            if shortest_distance == 0 or total < shortest_distance:
                shortest_distance = total
                shortest_distance_index = i

        self.cities.insert(shortest_distance_index, city)

    def __str__(self) -> str:
        """
        Returns the sequence of cities and the distance in parentheses
        For example, "Melbourne -> Kuala Lumpur (6368 km)"

        :return: a string representing the itinerary.
        """
        itinerary_list = [] #new empty list to add to
        for i in range(len(self.cities)):   #iterates through each city
            itinerary_list.append(self.cities[i].name) #gets the name of each city and appends it to the list
            
        return f"{' -> '.join(itinerary_list)} ({self.total_distance()} km)"    #returns the list of cities with arrows in between and the total distance

if __name__ == "__main__":
    create_example_cities()
    test_itin = Itinerary([get_cities_by_name("Melbourne")[0],
                           get_cities_by_name("Kuala Lumpur")[0]])
    print(test_itin)

    #we try adding a city
    test_itin.append_city(get_cities_by_name("Baoding")[0])
    print(test_itin)

    #we try inserting a city
    test_itin.min_distance_insert_city(get_cities_by_name("Sydney")[0])
    print(test_itin)

    #we try inserting another city
    test_itin.min_distance_insert_city(get_cities_by_name("Canberra")[0])
    print(test_itin)

