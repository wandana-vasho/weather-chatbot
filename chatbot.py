import requests

API_KEY = "your API key here"  # Replace with your real key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"The weather in {city} is {weather} with {temp}°C."
    else:
        return f"Could not find weather data for {city}."

# Chatbot loop
print("Hello! I am WeatherBot ☁️. Type 'exit' to quit.")
while True:
    user_input = input("Enter a city: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    print(get_weather(user_input))
