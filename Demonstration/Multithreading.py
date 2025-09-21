# ---------------- MULTITHREADING ---------------- #
# Multithreading = Run multiple tasks concurrently (at the same time).
# Useful for I/O-bound tasks (waiting for files, network, or user input).
# Advantage: No need to wait for one task to finish before starting another.

import threading
import time


# ---------------- TASK FUNCTIONS ----------------
def walk_dog(first, last):
    time.sleep(8)           # Simulates a slow task (8s delay)
    print(f"You finish walking {first} {last}")

def take_out_trash():
    time.sleep(2)           # Simulates a shorter task
    print("You take out the trash")

def get_mail():
    time.sleep(4)           # Simulates a medium task
    print("You get the mail")


# ---------------- THREAD CREATION ----------------
# Thread(target=func, args=(arguments,))
# Note: If only one argument, must use a trailing comma: args=("Scooby",)
chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore2 = threading.Thread(target=take_out_trash)
chore3 = threading.Thread(target=get_mail)

# Start threads (all run concurrently)
chore1.start()
chore2.start()
chore3.start()

# ---------------- THREAD SYNCHRONIZATION ----------------
# .join() waits for each thread to complete before moving on.
# Without join(), "All chores are complete!" could print before tasks finish.
chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")


# https://www.youtube.com/watch?v=STEOavXqXkQ&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=76