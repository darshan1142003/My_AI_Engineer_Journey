import requests

cities = {
    "mumbai": (19.0760, 72.8777),
    "pune": (18.5204, 73.8567),
    "delhi": (28.6139, 77.2090),
    "bangalore": (12.9716, 77.5946),
    "chennai": (13.0827, 80.2707),
    "jalgaon": (21.0077, 75.5626)
}

city = input("enter city name:").lower()

if city not in cities:
    print("Sorry, City not found")
    print("Available Cities",",".join(cities.keys()))

else:
    latitude, longitude = cities[city]

    url = (f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        f"&current_weather=true")

    try:
        response = requests.get(url)    

        if response.status_code == 200:
            data= response.json()
            weather = data["current_weather"]

            temperature = weather["temperature"]
            wind_speed = weather["windspeed"]
            weather_code = weather["weathercode"]

            print("\n🌤 Weather Report")
            print("------------------------")
            print("City:", city.capitalize())
            print("Temperature:", temperature, "°C")
            print("Wind Speed:", wind_speed, "km/h")
            print("Weather Code:", weather_code)

        else:
            print("Failed to fetch weather data.")
            print("Status Code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Network error:", e)        
    