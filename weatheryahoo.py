## @author Simranjit Singh
##import weather and its unit from weather api that is installed
from weather import Weather, Unit
weather = Weather(unit=Unit.CELSIUS)
while True:
    
##    used try and except block to manage exception
    try:
        city_name=input("Please enter the city name: ")
        if city_name=="":
        
##      if user input is empty ,code exit
            break
        location_name = weather.lookup_by_location(city_name)
##        used lookup_by_location and stored its value in location_name
        def data_assigner(location_name):
            attr = dict(
                sunrise=location_name.astronomy.sunrise,
##                here location_name.astronomy is fetched and
##                assigned to sunrise ,likewise other values
##                are assigned to keys
                sunset=location_name.astronomy.sunset,
                humidity=location_name.atmosphere.humidity,
                pressure=location_name.atmosphere.pressure,
                rising=location_name.atmosphere.rising,
                temperature=location_name.condition.temp,
                condition=location_name.condition.text,
                description=location_name.description,
                language=location_name.language,
                update_date=location_name.last_build_date,
                latitude=location_name.latitude,
                longitude=location_name.longitude,
                city=location_name.location.city,
                country=location_name.location.country,
                region=location_name.location.region,
                pressure_unit=location_name.units.pressure,
                speed_unit=location_name.units.speed,
                distance_unit=location_name.units.distance,
                temperature_unit=location_name.units.temperature,
                wind_chill=location_name.wind.chill,
                wind_direction=location_name.wind.direction,
                wind_speed=location_name.wind.speed,
                title=location_name.title
            )
            return attr
        
##        in above function we are assigning attributes to variables and
##        storing them in terms of keys and values in dictionary. This function takes
##        location name as parameter and returns attr which is dictionary
        
        
        def print_attribute(attr):
            print("")
            print("------------------------------------------")
            print("Date:",attr['update_date'])
            print("{},{},{}".format(attr['city'],attr['region'],attr['country']))
##            .format() converts in nicer string format
            print("Title:",attr['title'])
            print("Temperature: {}°{} Weather Condition: {}".format(attr['temperature'],attr['temperature_unit'],attr['condition']))
            print("Sunrise : {}  Sunset : {}".format(attr['sunrise'],attr['sunset']))
            print("Humidity : {}% Pressure : {}{} Rising: {}".format(attr['humidity'],attr['pressure'],attr['pressure_unit'],attr['rising']))
            print("Language used : {}".format(attr['language']))
            print("Latitude : {}  Longitude : {}".format(attr['latitude'],attr['longitude']))
            print("Wind : Chill {}°  Direction {}° Speed {}{}".format(attr['wind_chill'],attr['wind_direction'],attr['wind_speed'],attr['speed_unit']))

##        in above function values of keys of dictionary generated in previous function is printed  



        def getting_forecast(location_name):

            forecast_list = location_name.forecast
            for forecast_data in forecast_list:
                print("Date :",forecast_data.day,forecast_data.date)
                print("Weather Description :",forecast_data.text)
                print("Maximum Temperature :{}°C".format(forecast_data.high))
                print("Minimum Temperature :{}°C".format(forecast_data.low))
                print("------------------------------------------")
##            In this function forecast of upcoming days is stored in list and then
##            list is iterated using for loop and results is printed
            
        print_attribute(data_assigner(location_name))
        getting_forecast(location_name,date)
##        functions defined above is called ,output generate by data_assigner(location_name)
##        is passed in print_attribute so it is called like this
##        print_attribute(data_assigner(location_name)) and getting forecast is also called 
        while True:
            answer = input("Do you want to see weather forecast of another city? (y/n): ")
            if answer in ('y', 'n'):
                break
            print ("Invalid input.")
        if answer == 'y':
            continue
        else:
            print ("Goodbye")
            break
##        In above while loop we used to ask user to continue or leave
##        and give invalid input if user clicks any other alphabet except y and n
    except AttributeError:
        print("Invalid city name")
        print("----------------------------")
##        catching exception here

