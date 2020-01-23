import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(20,IO.IN) #GPIO 20 -> Bal infra erzekelo
IO.setup(26,IO.IN) #GPIO 26 -> Jobb infra erzeklo

IO.setup(8,IO.OUT) #GPIO 8 -> Jobb motor terminal A
IO.setup(7,IO.OUT) #GPIO 7 -> Jobb motor terminal B

IO.setup(9,IO.OUT) #GPIO 9 -> Bal motor terminal A
IO.setup(10,IO.OUT) #GPIO 10 -> Bal motor terminal B

while 1:

    if(IO.input(20)==True and IO.input(26)==True): #mindketto motor all    
        IO.output(8,True) #1A+
        IO.output(7,True) #1B-

        IO.output(9,True) #2A+
        IO.output(10,True) #2B-

    elif(IO.input(2)==False and IO.input(3)==True): #jobbra fordul 
        IO.output(4,False) #1A+
        IO.output(14,True) #1B-

        IO.output(17,True) #2A+
        IO.output(18,False) #2B-

    elif(IO.input(2)==True and IO.input(3)==False): #Balra fordul
        IO.output(4,True) #1A+
        IO.output(14,False) #1B-

        IO.output(17,False) #2A+
        IO.output(18,True) #2B-

    else:  #megy elore
        IO.output(4,True) #1A+
        IO.output(14,False) #1B-

        IO.output(17,True) #2A+
        IO.output(18,False) #2B-