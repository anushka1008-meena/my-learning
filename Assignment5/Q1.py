# Study the open weather API show more data in your API calling program

import requests

def weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=61d6d0d3cf5b71cb1679e80b029d8865&units-metric"  # added &units = metric in this url
    try:
        response = requests.get(url)

        response.raise_for_status() # if any error generated then it send us to accept mode
        data = response.json()      # json data now comes in variable
        city_name = data['name']

        temp = data['main']['temp']
        min_temp = data['main']['temp_min']  
        max_temp = data['main']['temp_max']

        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        visibility = data['visibility']

        print("city:",city_name)

        print("Temperature:",temp,"°C")
        print("Minimum temp:",min_temp,"°C")
        print("Maximum temp:",max_temp,"°C")

        print("Humidity:",humidity,"%")
        print("Pressure:",pressure,"hPa")
        print("Wind Speed:",wind_speed,"m/s")
        print("Visibility:",visibility,"meters")


    except requests.exceptions.RequestException as e:
        print(e) 

city = input('enter city name:')
weather_data(city)            # form this we got data of temperature from the url 