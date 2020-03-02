import pytz
from datetime import datetime

country = "America/Tijuana"

tz_to_display = pytz.timezone(country)
local_time = datetime.now(tz=tz_to_display)

print(type(tz_to_display))

print(f"The time in {country} is {local_time.strftime('%A %B %d, %Y -- %I:%M:%S %p')}")
print(f"UTC time is {datetime.utcnow().strftime('%A %B %d, %Y -- %I:%M:%S %p')}")

for tz in pytz.all_timezones:
    print(tz)

for key in pytz.country_names:
    print(f"{key}: {pytz.country_names[key]}")
    if key in pytz.country_timezones:
        for time_zone in pytz.country_timezones[key]:
            tz_to_display = pytz.timezone(time_zone)
            local_time = datetime.now(tz=tz_to_display)
            print(f"\t{time_zone} ==> {local_time.strftime('%A %B %d, %Y -- %I:%M:%S %p')}")
