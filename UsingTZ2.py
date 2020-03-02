import pytz
from datetime import datetime

naive_local_time = datetime.now()
naive_utc_time = datetime.utcnow()

print(f"Naive local time: {naive_local_time}")
print(f"Naive UTC time: {naive_utc_time}")
print()

aware_local_time = pytz.utc.localize(naive_utc_time).astimezone()
aware_utc_time = pytz.utc.localize(naive_utc_time)

print(f"Aware local time: {aware_local_time}")
print(f"Aware UTC time: {aware_utc_time}")
