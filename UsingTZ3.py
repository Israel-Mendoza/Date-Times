import pytz
from datetime import datetime

mx_timezones = pytz.country_timezones("MX")

mx_city_tz_obj = pytz.timezone("America/Mexico_City")
print(f"'mx_city_tz_obj': {type(mx_city_tz_obj)} {mx_city_tz_obj}")

aware_local_time = mx_city_tz_obj.localize(datetime.now())
print(f"'aware_local_time': {aware_local_time}")
print(f"'aware_local_time' tz_info: {aware_local_time.tzinfo}")
print()


# Naive comparison

naive_local_time = datetime.now()

print(f"'naive_local_time': {naive_local_time}")
print(f"'naive_local_time' tz_info: {naive_local_time.tzinfo}")

