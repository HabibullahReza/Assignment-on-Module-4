# ==========================================
# Real Time Weather & Currency Data Fetcher
# Student Project
# ==========================================

import json
import urllib.request
from datetime import datetime
import os


# Last fetched data store করার জন্য
last_result = None


# -----------------------------
# Get Weather Information
# -----------------------------
def get_weather():

    global last_result

    city = input("Enter city name: ")

    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = urllib.request.urlopen(url)
        weather_data = json.loads(response.read())

        current = weather_data["current_condition"][0]

        temp = current["temp_C"]
        humidity = current["humidity"]
        wind = current["windspeedKmph"]
        condition = current["weatherDesc"][0]["value"]

        time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

        print("\n------ Weather Report ------")
        print("City:", city.title())
        print("Temperature:", temp + "°C")
        print("Humidity:", humidity + "%")
        print("Wind Speed:", wind + " km/h")
        print("Condition:", condition)
        print("Fetched Time:", time)
        print("----------------------------")


        last_result = {
            "type": "weather",
            "city": city.title(),
            "temperature": temp,
            "humidity": humidity,
            "wind_speed": wind,
            "condition": condition,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }


    except:
        print("Weather data পাওয়া যাচ্ছে না।")


# -----------------------------
# Get Currency Rate
# -----------------------------
def get_currency():

    global last_result

    base = input("Base Currency: ").upper()
    target = input("Target Currency: ").upper()


    url = f"https://open.er-api.com/v6/latest/{base}"


    try:

        response = urllib.request.urlopen(url)
        currency_data = json.loads(response.read())


        rate = currency_data["rates"][target]

        time = datetime.now().strftime("%d-%m-%Y %I:%M %p")


        print("\n------ Currency Rate ------")
        print(f"1 {base} = {rate} {target}")
        print("Fetched Time:", time)
        print("---------------------------")


        last_result = {
            "type": "currency",
            "base": base,
            "target": target,
            "rate": rate,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }


    except:
        print("Currency data পাওয়া যাচ্ছে না।")


# -----------------------------
# Save Data
# -----------------------------
def save_data():

    if last_result is None:
        print("কোনো data পাওয়া যায়নি।")
        return


    with open("data.json", "w") as file:

        json.dump(last_result, file, indent=4)


    print("Data saved successfully.")



# -----------------------------
# View Saved Data
# -----------------------------
def view_data():


    if not os.path.exists("data.json"):

        print("No previous data found.")
        return



    with open("data.json", "r") as file:

        data = json.load(file)



    print("\n====== Previous Saved Data ======")


    if data["type"] == "weather":

        print("Type:", "Weather")
        print("City:", data["city"])
        print("Temperature:", data["temperature"] + "°C")
        print("Humidity:", data["humidity"] + "%")
        print("Condition:", data["condition"])
        print("Saved Time:", data["time"])


    else:

        print("Type:", "Currency")
        print("Base:", data["base"])
        print("Target:", data["target"])
        print("Rate:", data["rate"])
        print("Saved Time:", data["time"])


    print("=================================")



# -----------------------------
# Main Menu
# -----------------------------
def menu():

    while True:


        print("\n========== Data Fetcher ==========")
        print("1. Current Weather")
        print("2. Currency Exchange Rate")
        print("3. Save Result")
        print("4. View Previous Data")
        print("5. Exit")
        print("==================================")


        choice = input("Choose option: ")



        if choice == "1":

            get_weather()


        elif choice == "2":

            get_currency()


        elif choice == "3":

            save_data()


        elif choice == "4":

            view_data()


        elif choice == "5":

            print("Program closed.")
            break


        else:

            print("Wrong choice. Try again.")



# Program Start

menu()
