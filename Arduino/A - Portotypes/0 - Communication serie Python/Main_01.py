import serial
import os
from datetime import datetime
import time

## File gestion

# Here we create a string with the date and time of the measure, this will be used to specify the name of the file where the data will be stored
now=datetime.now()
k=now.strftime("%b_%d_%H_%M_%S") 

#Here we change the location of the program so that we write the data in the right file
os.chdir("/Users/pierrebouvet/Documents/01 - Phelma/iGEM/07 - Programmes")

#Here we create the name of the file and we open it
name="Data"+k+".txt"
file=open(name,"w")
 
## Collection of data 

#Here we initialize the serial port of the Arduino. This adress can be found in the Tools part of the Arduino program
ser = serial.Serial('/dev/cu.usbmodem14101', 9600)

for i in range(1,100):
    line = ser.readline() #We extract the line of data that has been returned by the Arduino
    value = str(line); #We convert the line into a string
    file.write(value); #We write the data into the data file
    file.write("\n"); #We add this to have each new data on a new line
    time.sleep(0.1) #Here we wait for the Arduino to send another value THIS PART HAS TO BE REWRITTEN SO THAT IT EQUALS THE ONE OF THE ARDUINO

print("End") #Here we print this line to say that we have all the datas 
file.close()

## Treatment of data

with open(name,"r") as file: 
    text=file.readlines() 
i=0 
while i < len(text): 
    print(i)
    text[i]=text[i].replace('b',"")
    text[i]=text[i].replace('\'',"")
    text[i]=text[i].replace('\\r\\n',"")
    #text[i]=text[i].split(";") #TO USE ONLY IF TREATMENT OF text IN THE REST OF PROGRAM -> AFFECTS THE WRITING OF THE FILE
    i=i+1
        
with open("file","w") as file: 
    file.writelines(text)


