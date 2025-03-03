import time

global_var = 0
# Start time
start_time = time.time()

def increment_and_print():
    global global_var  # Needed to modify global copy of global_var
    global_var += 1

while True:
    # Current time
    current_time = time.time()

    # If the difference between the current time and the start time is more than 30 seconds, break the loop
    if current_time - start_time > 30:
        break

    increment_and_print()
    print(global_var)

    # Wait for 5 seconds
    time.sleep(5)

print("Exited after 30 seconds.")
