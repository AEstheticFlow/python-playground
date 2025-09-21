import time

my_time = int(input("Enter the time in seconds: ") )

for x in range(my_time, 0, -1):
    seconds = x % 60            # To only contain the seconds
    minutes = (x // 60) % 60    # (//) does integer division instead of wraping it in int()
    hours = x // 3600           # Same, could've also typed: int(x / 3600), but this's better
       
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")


# https://www.youtube.com/watch?v=KseiSR0MCTI