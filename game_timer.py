# remember to use python 2

import os
from playsound import playsound
from time import sleep

# set turn times here
TURN_TIME = 5
TIME_BETWEEN_TURNS = 1

frequency_start = 1000 # Hertz
frequency_stop = 500 # Hertz
duration  = 5000 # milliseconds

ready_go = "./go.wav"
buzzer_x = "./buzzer_x.wav"

while True:
    playsound(ready_go) # start turn
    sleep(TURN_TIME) 
    playsound(buzzer_x) # end turn
    sleep(TIME_BETWEEN_TURNS) 


