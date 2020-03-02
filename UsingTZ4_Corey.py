import pytz
from datetime import datetime

# Creating a dt object tz aware with a given time
dt = datetime(2020, 3, 1, 3, 0, 0, tzinfo=pytz.UTC)
print(dt)

# Creating a dt object tz aware with the current time
dt_utc_now = datetime.now(tz=pytz.UTC)
print(dt_utc_now)

# Converting a tz aware object to a desired tz
dt_mx = dt.astimezone(pytz.timezone("America/Mexico_City"))
print(dt_mx)

# Converting a tz naive dt object to a tz aware

bd = datetime(1992, 4, 9, 15, 54, 0) # Naive dt object
print(bd)

bd = bd.replace(tzinfo=pytz.utc)    # Replacing the naive object with an aware one
print(bd)

my_bd = bd.astimezone(tz=pytz.timezone("America/Mexico_City"))
print(my_bd)
