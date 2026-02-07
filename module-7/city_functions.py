

def city_country(city, country, language = ' ', population = ' '):
    if population != ' ':
        if language != " ":
            name = city + ', ' + country + " - population " + str(population) + ', ' + language
            return name
        else:
            name = city + ', ' + country + " - population " + str(population)
            return name

    else:
        if language != ' ':
            name = city + ', ' + country + ', ' + language
            return name
        else:
            name = city + ', ' + country
            return name

def main():
    print(city_country("Helena", "Montana", 'English', population = 5000))
    print(city_country("Watertown", "Wisconsin"))
    print(city_country("Missoula", "Montana", population = 12300))
    print(city_country("Kalispell", "Montana", 'French'))
    #I know these aren't countries, I realized it said countries after I took most of the screenshots!

if __name__ == "__main__":
    main()
