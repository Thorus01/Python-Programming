"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains the class Country.

@file country.py
"""
from tabulate import tabulate
from city import City, create_example_cities

class Country():
    """
    Represents a country.
    """

    name_to_countries = dict() # a dict that associates country names to instances.

    def __init__(self, name: str, iso3: str) -> None:
        """
        Creates an instance with a country name and a country ISO code with 3 characters.

        :param country_name: The name of the country
        :param country_iso3: The unique 3-letter identifier of this country
	    :return: None
        """
        self.name = name
        self.iso3 = iso3
        self.cities = [] #create an empty list to store the cities in
        Country.name_to_countries.update({name:self}) #populate the dictionary 

    def add_city(self, city: City) -> None:
        """
        Adds a city to the country.

        :param city: The city to add to this country
        :return: None
        """
        self.cities.append(city) #begin adding cities into that empty list

    def get_cities(self, city_type: list[str] = None) -> list[City]:
        """
        Returns a list of cities of this country.

        The argument city_type can be given to specify a subset of
        the city types that must be returned.
        Cities that do not correspond to these city types are not returned.
        If None is given, all cities are returned.

        :param city_type: None, or a list of strings, each of which describes the type of city.
        :return: a list of cities in this country that have the specified city types.
        """
        new_city_list = [] #new list of cities created for a specific country, stores cities that match the specific city types
        if city_type is None:
            return self.cities #None is given thus all cities returned
        else:
            for i in range(len(self.cities)): #iterating through the cities list
                if self.cities[i].city_type in city_type: #if the iterator in city_type matches add it into the new list
                    new_city_list.append(self.cities[i])
            return new_city_list #return the new list of cities

    def print_cities(self) -> None:
        """
        Prints a table of the cities in the country, from most populous at the top
        to least populous. Use the tabulate module to print the table, with row headers:
        "Order", "Name", "Coordinates", "City type", "Population", "City ID".
        Order should start at 0 for the most populous city, and increase by 1 for each city.
        """

        def sort_cities(city):
            return(city.population) #new function here helps sort the list of cities
        
        table_items = [["Order", "Name", "Coordinates", "City type", "Population", "City ID"]]
        #hardcode the headers into the first row of the table
    
        sorted_cities = sorted(self.cities, key=sort_cities, reverse = True) #sorts the self.cities list, the key is set to sort_cities and reverse is True to allow population to sort in descending order
        for i in range(len(sorted_cities)): #iterate through the sorted list of cities
            city = sorted_cities[i]
            table_items.append([i, city.name, city.coordinates, city.city_type, city.population, city.city_id]) #begin adding the sorted cities as a new row in table items in line with the table headers' order
        print('Cities of ' + self.name)
        print(tabulate(table_items)) #print the Cities of '...' and the table

    def __str__(self) -> str:
        """
        Returns the name of the country.
        """
        return(self.name) #return name of country

def add_city_to_country(city: City, country_name: str, country_iso3: str) -> None:
    """
    Adds a City to a country.
    If the country does not exist, create it.

    :param country_name: The name of the country
    :param country_iso3: The unique 3-letter identifier of this country
    :return: None
    """
    
    if country_name in Country.name_to_countries:
        country = Country.name_to_countries[country_name] #checks if Country exists, if it does store it 
    else:
        country = Country(country_name, country_iso3) #if it doesn't create new country object created and iso3
    country.add_city(city) #add this new specific city to country
    
def find_country_of_city(city: City) -> Country:
    """
    Returns the Country this city belongs to.
    We assume there is exactly one country containing this city.

    :param city: The city.
    :return: The country where the city is.
    """
    for i in Country.name_to_countries.values(): #iterate through the Country name dictionary
        if city in i.cities: #if the city is found in the Country's cities' list, return it (the iterator)
            return i

def create_example_countries() -> None:
    """
    Creates a few countries for testing purposes.
    Adds some cities to it.
    """
    create_example_cities()
    malaysia = Country("Malaysia", "MAS")
    kuala_lumpur = City.name_to_cities["Kuala Lumpur"][0]
    malaysia.add_city(kuala_lumpur)

    for city_name in ["Melbourne", "Canberra", "Sydney"]:
        add_city_to_country(City.name_to_cities[city_name][0], "Australia", "AUS")

def test_example_countries() -> None:
    """
    Assuming the correct countries have been created, runs a small test.
    """
    Country.name_to_countries["Australia"].print_cities()


if __name__ == "__main__":
    create_example_countries()
    test_example_countries()
