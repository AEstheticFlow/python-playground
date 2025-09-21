import datetime

# ---------------- DATE OBJECTS ----------------
# Create a specific date (year, month, day)
date = datetime.date(2005, 8, 6)
print(f"Set date: {date}")
print("-" * 60)

# Get today's current date (system date)
today = datetime.date.today()
print(f"Today's date: {today}")
print("-" * 60)

# ---------------- TIME OBJECTS ----------------
# Create a specific time (hour, minute, second)
time = datetime.time(12, 30, 00)
print(f"Set time: {time}")
print("-" * 60)

# ---------------- DATETIME OBJECTS ----------------
# Get the current date and time
now = datetime.datetime.now()
print(f"Exactly now's date & time: {now}")
print("-" * 60)

# Format current date/time as a string using 'strftime'
# %H = hour(24h), %M = minute, %S = second, %m = month(01-12), %d = day, %Y = year(4 digits)
now = datetime.datetime.now().strftime("%H:%M:%S  %m-%d-%Y")  # Modifying now's formation ♠
print(f"Formated date and time: {now}")
print("-" * 60)


# ---------------- COMPARING DATES ----------------
# Create a target datetime for comparison (future/past moment)
target_datetime = datetime.datetime(2005, 8, 6, 12, 30, 00)

# Get the current datetime again for comparison
current_datetime = datetime.datetime.now()

# Compare target with current datetime
if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed, yet")
print("-" * 60)


# https://www.youtube.com/watch?v=DwBDHsdX6XQ&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=74