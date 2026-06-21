import requests
import json

API_KEY = "f6c3916b72b9061e7e0878ebdfc2b1c8"

def get_weather(city):
    """this function retrieves the wheather and display it """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()

            # Save search history
            with open("history.txt", "a") as file:
                file.write(f"{data['name']}\n")

            # Save latest weather data
            with open("weather_data.json", "w") as file:
                json.dump(data, file, indent=4)

            print("\n" + "=" * 40)
            print("WEATHER REPORT")
            print("=" * 40)

            print(f"City: {data['name']}")
            print(f"Country: {data['sys']['country']}")
            print(f"Temperature: {data['main']['temp']} °C")
            print(f"Feels Like: {data['main']['feels_like']} °C")
            print(f"Weather: {data['weather'][0]['description']}")
            print(f"Humidity: {data['main']['humidity']} %")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
            print(f"Pressure: {data['main']['pressure']} hPa")
            print(f"Visibility: {data['visibility']/1000} km")

            print("=" * 40)

        elif response.status_code == 404:
            print("City not found.")

        else:
            print(f"Error: {response.status_code}")

    except requests.exceptions.RequestException:
        print("Unable to connect to the weather service.")

def view_history():
    """this funtion displays the search history of the weather app"""
    try:
        with open("history.txt", "r") as file:
            print("\n===== SEARCH HISTORY =====")
            print(file.read())
    except FileNotFoundError:
        print("No search history found.")

while True:
    print("\n===== WEATHER APP =====")
    print("1. Search Weather")
    print("2. View Search History")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        city = input("Enter city name: ")
        get_weather(city)

    elif choice == "2":
        view_history()

    elif choice == "3":
        print("Thank you for using the Weather App!")
        break

    else:
        print("Invalid choice. Please try again.")