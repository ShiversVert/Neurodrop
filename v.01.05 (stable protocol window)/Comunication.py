import serial
from tkinter import Toplevel
from Framing_functions import Create_Heading


def Arduino_init(Window):
    """
    This function initializes the communication between the Arduino and the computer
    """
    #We start by creating the parameter window, where we will select the serial port and we will create the directory where all the datas will be stored
    Parameter_window=Toplevel(Window)
    Create_Heading(Parameter_window)
    
    ser = serial.Serial('/dev/cu.usbmodem14101', 9600)
    return 1

def Arduino_pipet(volume, solution):
    return 1

def Arduino_drop():
    return 1

def Arduino_move(xbeg,ybeg,xend,yend):
    return 1

def Arduino_measure(nbmeasures, t_between_measures):
    return 1

def Arduino_clean():
    return 1

def Arduino_thaw():
    return 1

def Apply_protocol(Window,protocol):
    Arduino_init(Window)
    for step in protocol:
        cmd=step[0]
        if cmd=='pip':
            vol=step[1]
            sol=step[2]
            Arduino_pipet(vol,sol)
        elif cmd=='dep':
            Arduino_drop()
        elif cmd=='mov':
            xbeg=step[1]
            ybeg=step[2]
            xend=step[3]
            yend=step[4]
            Arduino_move(xbeg, ybeg, xend, yend)
        elif cmd=='lum':
            nbmes=step[1]
            t_inter_mes=step[2]
            Arduino_measure(nbmes,t_inter_mes)
        elif cmd=='cle':
            Arduino_clean()
        elif cmd=='tha':
            Arduino_thaw
        elif cmd!='position':
            ValueError
        nbline=nbline+1
    return Window