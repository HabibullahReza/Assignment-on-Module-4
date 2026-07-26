# ==========================================
# Real-Time Weather & Currency Data Fetcher
# File Name: data_fetcher.py
# ==========================================

import json
import urllib.request
from datetime import datetime
import os

# Store the latest fetched data
latest_data = None


# ==========================================
# Current Weather
# ==========================================
def weather():
    global latest_data

    city = input("Enter city name: ").strip()

    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        current = data["current_condition"][0]

        temperature = current["temp_C"]
        humidity = current["humidity"]
        wind_speed = current["windspeedKmph"]
        condition = current["weatherDesc"][0]["value"]

        current_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

        print("\n------ Weather Report ------")
        print(f"City         : {city.title()}")
        print(f"Temperature  : {temperature}°C")
        print(f"Humidity     : {humidity}%")
        print(f"Wind Speed   : {wind_speed} km/h")
        print(f"Condition    : {condition}")
        print(f"Fetched At   : {current_time}")
        print("-----------------------------")

        latest_data = {
            "type": "weather",
            "city": city.title(),
            "temperature": temperature,
            "humidity": humidity,
            "wind_speed": wind_speed,
            "condition": condition,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    except Exception as e:
        print("Unable to fetch weather information.")
        print(e)


# ==========================================
# Currency Exchange
# ==========================================
def currency():
    global latest_data

    base = input("Base Currency: ").upper()
    target = input("Target Currency: ").upper()

    url = f"https://open.er-api.com/v6/latest/{base}"

    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        if target not in data["rates"]:
            print("Invalid target currency.")
            return

        rate = data["rates"][target]

        current_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

        print("\n------ Exchange Rate ------")
        print(f"1 {base} = {rate} {target}")
        print(f"Fetched At : {current_time}")
        print("---------------------------")

        latest_data = {
            "type": "currency",
            "base": base,
            "target": target,
            "rate": rate,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    except Exception as e:
        print("Unable to fetch exchange rate.")
        print(e)


# ==========================================
# Save Data to JSON
# ==========================================
def save_json():
    global latest_data

    if latest_data is None:
        print("No data available to save.")
        return

    try:
        with open("data.json", "w") as file:
            json.dump(latest_data, file, indent=4)

        print("Data saved successfully.")

    except Exception as e:
        print("Failed to save data.")
        print(e)


# ==========================================
# View Saved Data
# ==========================================
def view_json():

    if not os.path.exists("data.json"):
        print("No saved data found.")
        return

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        print("\n====== Last Saved Data ======")

        if data["type"] == "weather":

            print("Type         : Weather")
            print(f"City         : {data['city']}")
            print(f"Temperature  : {data['temperature']}°C")
            print(f"Humidity     : {data['humidity']}%")
            print(f"Wind Speed   : {data['wind_speed']} km/h")
            print(f"Condition    : {data['condition']}")
            print(f"Saved Time   : {data['time']}")

        elif data["type"] == "currency":

            print("Type         : Currency")
            print(f"Base         : {data['base']}")
            print(f"Target       : {data['target']}")
            print(f"Rate         : {data['rate']}")
            print(f"Saved Time   : {data['time']}")

        print("==============================")

    except Exception as e:
        print("Unable to read saved data.")
        print(e)


# ==========================================
# Main Menu
# ==========================================
def main_menu():

    while True:

        print("\n========== Data Fetcher ==========")
        print("1. Current Weather")
        print("2. Currency Exchange Rate")
        print("3. Save Result to JSON File")
        print("4. View Previous Saved Data")
        print("5. Exit")
        print("==================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            weather()

        elif choice == "2":
            currency()

        elif choice == "3":
            save_json()

        elif choice == "4":
            view_json()

        elif choice == "5":
            print("\nThank you for using Data Fetcher.")
            break

        else:
            print("Invalid choice! Please try again.")


# ==========================================
# Program Starts Here
# ==========================================
if __name__ == "__main__":
    main_menu()