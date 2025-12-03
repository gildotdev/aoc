import math

dial = range(100) # 0-99
current_dial_position = 50 # starts at 50
count_times_at_zero = 0 # none at start

# for stop in dial:
#     print(stop)

def to_base_100(n):
    if n == 0:
        return "0"
    return n % 100

def move(direction, number):
    global current_dial_position
    global current_dial_position
    global count_times_at_zero
    global dial
    
    if direction == "L":
        current_dial_position = current_dial_position - number
    if direction == "R":
        current_dial_position = current_dial_position + number

    current_dial_position = to_base_100(current_dial_position)

    if current_dial_position == 0:
        count_times_at_zero += 1
    


move("L", 100)

print(current_dial_position, count_times_at_zero)

move("R", 50)

print(current_dial_position, count_times_at_zero)