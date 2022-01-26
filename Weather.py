import requests

API_KEY = "aea7a3453a0a84878110b0ca6592c504"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    temperature_feel = round(data['main']['feels_like'] - 273.15, 2)
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    visibility = data['visibility']
    wind_speed = humidity = data['wind']['speed']
    print('-----------------------------------')
    print('Weather in', city, 'is:', weather)
    print('-----------------------------------')
    print('Temperature in',city, 'is:', temperature, 'degree celsius')
    print('-----------------------------------')
    print('Wind speed in', city, 'is:', wind_speed, 'm/s')
    print('-----------------------------------')
    print('Temperature feels like in', city, 'is:', temperature_feel, 'degree celsius')
    print('-----------------------------------')
    print('Pressure in', city, 'is:', pressure, 'MPa')
    print('-----------------------------------')
    print('Humidity in', city, 'is:', humidity, '%')
    print('-----------------------------------')
    print('Visibility in', city, 'is:', visibility, 'm')
    print('-----------------------------------')


else:
    print("An error occurred.")