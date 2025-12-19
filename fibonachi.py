import math
import time
num_1 = 1
num_2 = 2
time_elapsed = 0
while time_elapsed <= 1:
    num_1 += num_2
    print (f"{num_1}, ")
    num_2 += num_1
    print (f"{num_2}, ")

while time_elapsed <= 1.1:
    time.sleep (1)
    time_elapsed += 1