#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests

# Define the API endpoint and your API key
api_url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "278773ebf9a63da4df48ee7ad2ca9870"

def fetch_weather(city_name):
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',  # Change to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        # Extract and display weather information
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']

        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    city_name = input("Enter a city name: ")
    fetch_weather(city_name)


# In[ ]:




