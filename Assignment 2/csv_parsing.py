"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a parser that reads a CSV file and creates instances 
of the class City and the class Country.

@file city_country_csv_reader.py
"""
import csv
from city import City, get_cities_by_name, get_city_by_id
from country import Country, add_city_to_country

def create_cities_countries_from_csv(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.

    :param path_to_csv: The path to the CSV file.
    """
    with open(path_to_csv, "r",) as csv_file:    #opens the chosen CSV file on read mode
        csv_reader = csv.reader(csv_file)
        citylist = []   #will be populated by lists representing each city
        for row in csv_reader:  #reads the CSV file into the array
            citylist.append(row)
        
    for i in range(len(citylist)-1):    #iterates through each city
        currentcity = i+1
        for j in range(len(citylist[0])):   #iterates through each item of the city
            if citylist[0][j] == "city_ascii":
                name = citylist[currentcity][j]
            elif citylist[0][j] == "lat":
                lat = citylist[currentcity][j]
            elif citylist[0][j] == "lng":
                lng = citylist[currentcity][j]
            elif citylist[0][j] == "country":
                city_country = citylist[currentcity][j]
            elif citylist[0][j] == "iso3":
                iso3 = citylist[currentcity][j]
            elif citylist[0][j] == "capital":
                capital = citylist[currentcity][j]
            elif citylist[0][j] == "population":
                if citylist[currentcity][j] == "":
                    city_pop = 0
                else:
                    city_pop = int(citylist[currentcity][j])
            elif citylist[0][j] == "id":
                id_city = int(citylist[currentcity][j])
    
        coordinates = (float(lat), float(lng))
        City(name, coordinates, capital, city_pop, id_city)
        add_city_to_country(get_city_by_id(id_city), city_country, iso3)

if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")
    for country in Country.name_to_countries.values():
        country.print_cities()
