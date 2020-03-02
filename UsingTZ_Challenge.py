# Playing with date times and time zones


import pytz
from datetime import datetime

tz_codes = {
    1: "America/Los_Angeles",
    2: "America/Mexico_City",
    3: "America/New_York",
    4: "Europe/Paris",
    5: "Europe/Istanbul",
    6: "Europe/Moscow",
    7: "Asia/Kolkata",
    8: "Asia/Seoul",
    9: "Asia/Tokyo"
}

places = {
    0: "Exit",
    1: "Los Angeles",
    2: "Mexico City",
    3: "New York",
    4: "Paris",
    5: "Istambul",
    6: "Moscow",
    7: "Kolkata",
    8: "Seoul",
    9: "Tokyo"
}


def display_options(places_list: dict):
    for option, place in places.items():
        if option == 0:
            continue
        print(f"\t{option}. {place}")


def display_time(desired_location: int):
    tz_code = tz_codes[desired_location]
    current_utc = datetime.now(tz=pytz.utc)
    local_time = current_utc.astimezone(pytz.timezone("America/Mexico_City"))
    desired_time = current_utc.astimezone(pytz.timezone(tz_code))
    print(f"\nCurrent UTC time: {current_utc.strftime('%A %B %d, %Y  %I:%M:%S %p')}")
    print(f"Current local time: {local_time.strftime('%A %B %d, %Y  %I:%M:%S %p')}")
    print(f"Current time in {places[desired_location]}: {desired_time.strftime('%A %B %d, %Y  %I:%M:%S %p')}\n")


while True:
    print("Available options: ")
    display_options(places)
    message = "Enter desired location: "
    location = input(message)
    for index, city in places.items():
        if location.lower() in city.lower():
            location = index
            break
    else:
        try:
            location = int(location)
        except ValueError:
            print("That was not a valid option! Try again...")
            continue
    if location == 0:
        print("\nGoodbye!\n")
        break
    display_time(location)
