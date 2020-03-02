import time

print(f"The Epoch on this system starts at {time.strftime('%A %B %d, %Y - %I:%M:%S %p', time.gmtime(0))}")
print(f"The current timezone is {time.tzname[0]} with an offset of {time.timezone}")

if time.daylight != 0:
    print("\tDaylight saving time is in effect for this location")
else:
    print("\tDaylight saving time is not in effect for this location.")

print(f"Local time is {time.strftime('%A %B %d, %Y - %I:%M:%S %p', time.localtime())}")
print(f"UTC time is {time.strftime('%A %B %d, %Y - %I:%M:%S %p', time.gmtime())}")

