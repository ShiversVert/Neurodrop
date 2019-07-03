import serial
from tkinter import Toplevel, Spinbox, Text
import Framing_functions as Ff
import Styles as sty
from functools import partial
import sys
import glob
import time
import Pins_Arduino as pa


def serial_ports():
    """ Lists serial port names

        Entry: 
            None
        Returns:
            A list of the serial ports available on the system

        :raises EnvironmentError:
            On unsupported or unknown platforms
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def launch_arduino(Window, values, protocol, Window_main):
    """
    This function gets the parameters of the parameter window of the arduino, and uses them to establish the link between the command board and the PC
    Entry:
        Window(frame): the parent frame
        values(spinbox variable): the widget containing the port
        protocol(list): the list containing all the commands
    Returns:
        Nothing BUT activates the function Arduino_command
    """
    port=str(values.get())
    arduino=serial.Serial(port,9600)
    arduino.flush()
    line=str(arduino.readline())[2:-5]
    if not (line=="Arduino OK"):
        while not (line=="Arduino OK"):
            arduino.close()
            arduino=serial.Serial(port,9600)
            line=str(arduino.readline())[2:-5]
    Window.destroy()
    Arduino_command(protocol,arduino)

def verif_communication(text_sent,text_returned, arduino):
    """
    This function verifies that the arduino has received the right string. It also verifies that the string is well passed
    
    Entry: 
        text_sent(string): the string that is being sent
        text_returned(string): the text that is being returned by the arduino
    Returns:
        Boolean: True if communication OK, False if communication couldn't be established
    """
    if not (text_returned=='ACK '+text_sent):
        k=0
        while not (text_returned=='ACK '+text_sent):
            time.sleep(0.01)
            arduino.write(text_sent.encode())
            text_returned=str(arduino.readline())[2:-5]
            k=k+1
            if k>100:
                print("Error in communication: message sent 100 times with a wrong return")
                return EnvironmentError
    return True

def wait_connection(arduino):
    """
    Waits for the arduino to be connected to the computer

    Entry:
        arduino(serial): the serial connection to the arduino
    Returns:
        Boolean: True if communication OK, False if communication couldn't be established

    """
    connected=False
    while not connected:
        received=str(arduino.readline())[2:-5]
        connected=True
    if received=='Arduino OK':
        return True
    else:
        print("Error in initializing the Arduino")
        return False

def send_and_wait_verif(arduino, text):
    """
    This function sends a string to the arduino and makes sure it receives it correctly
    
    Entry:
        arduino(serial): the serial connection to the Arduino
        text(string): the string that is being transfered to the Arduino
    Returns:
        Boolean: True if communication OK, False if communication couldn't be established
    """
    arduino.write(text.encode())
    # print(text)
    received=str(arduino.readline())[2:-5]
    # print(received)
    if verif_communication(text,received,arduino):
        return True
    else:
        return False

def send_value(arduino, text):
    """
    This function sends the information to the arduino, waits for it to be returned by the arduino, compares the two informations, and while the two are not the same, sends them again 

    Entry:
        motor(str): the motor (either the x-axis or the z-axis, respectively named 'X' and 'Z')
        direction(int): the direction the motor has to move(1 for right/up, 2 for left/down)
        step(int): the number of steps
    Returns:
        True at the end of the process
    """
    a=send_and_wait_verif(arduino, text) 
    while not a: 
        a=send_and_wait_verif(arduino, text)
    return True

def set_pin(arduino, state, pin):
    """
    This function passes a pin to high state

    Entry:
        arduino(serial): the serial connection to the Arduino
        state(int): the state we want to put the button to (0 for LOW, 1 for HIGH)
        pin(int): the pin we want to activate
    Returns:
        True at the end of the process
    """
    send_value(arduino,'1')
    send_value(arduino, str(state))
    send_value(arduino, str(pin))
    return True

def generate_step(arduino, pin, steps, half_period, first_state):
    """
    This function generates a step signal

    Entry:
        arduino(serial): the serial connection to the Arduino
        pin(int): the pin we want to activate
        steps(int): the number of periods
        half_period(int): half of the period
        first_state(int): the ground state (0 for LOW, 1 for HIGH)
    Returns:
        True at the end of the process
    """
    send_value(arduino,'2')
    send_value(arduino, str(int(steps))+str(100+pin)[1:]+str(first_state))
    send_value(arduino, str(half_period))
    return True

# arduino=serial.Serial('/dev/cu.usbmodem14101', 9600)
# generate_step(arduino, 2,10,250,1)

def move_motor(arduino, actual_position, desired_position, motor):
    """
    This function moves a motor to a desired position (in number of steps)

    Entry: 
        arduino(serial): the serial conection to the Arduino
        actual_position(int): the actual position the motor is in
        desired_positon(int): the targetted position for the motor
        motor(int): the motor to activate, 0 for the X motor, 1 for the Z motor
    Returns:
        Boolean: True if nothing went wrong
    """
    send_value(arduino, '3')
    send_value(arduino, str(actual_position)+str(motor))
    send_value(arduino, str(desired_position))
    return True

def create_PWM(arduino, pin, value):
    """
    This function genereates a PWM signal

    Entry:
        arduino(serial): the serial connection to the Arduino
        pin(int): the pin we want to activate
        value(int): the value that has to be created by the Arduino (between 0 and 255)
    Returns:
        True at the end of the process
    """
    send_value(arduino,'4')
    send_value(arduino, str(pin))
    send_value(arduino, str(value))
    return True

def Arduino_pipet(volume, solution, arduino):
    """
    This function sends the command to the Arduino to pipet the desired amount of solution in the desired solution

    Entry: 
        volume(int): the volume of solution that we want to pipette
        solution(int): the solution in which we want to pipette
        arduino(serial): the serial connection to the Arduino
    Returns:
        Boolean: True if nothing went wrong
    """

    motor_steps=pa.motor_steps
    lower=pa.lower_move_pipette#Steps to get from high position to low position

    boolean=True
    change_vol=True
    volume_initial=5000 # TODO nL
    if volume>volume_initial: #We have to ask the pipette to pipette more than 5µL
        pin1=pa.Pip_upp #This is the pin that corresponds to the more on the pipette
        pin2=pa.Pip_dow #This is the pin that corresponds to the less on the pipette
        steps=(volume-volume_initial)/50
    elif (volume<volume_initial): #We have to ask the pipette to pipette less than 5µL
        pin1=pa.Pip_dow #This is the pin that corresponds to the less on the pipette
        pin2=pa.Pip_upp #This is the pin that corresponds to the more on the pipette
        steps=(volume_initial-volume)/50
    else: #We don't have to change the parameters of the pipette
        change_vol=False

    steps_tip=motor_steps[solution-3]#We first have to take the tip so we look how many steps there are from the reference position to the tip
    steps_sol=motor_steps[solution-1]-steps_tip

    while boolean:
        boolean=boolean and generate_step(arduino, pa.Pip_rei, 1, 100, 1)
        time.sleep(1) # Waiting for the pipette to reinitialise
        boolean=boolean and generate_step(arduino, pa.Pip_tip, 1, 100, 1)
        if change_vol: #If we have to change the volume the pipette has to pipette
            print("Changing the volume on the pipette")
            boolean=boolean and generate_step(arduino, pin1, steps, pa.tmp_btn, 1)# Press a certain number of times on the + button
            boolean=boolean and generate_step(arduino,pa.Pip_ent,1,pa.tmp_btn,1)# Press one time on the enter button
        
        #Move the plate to the tips
        print("Moving the plate")
        boolean=boolean and move_motor(arduino, 0, steps_tip, 0)
        
        #Move the pipette to take a tip
        print("Taking a tip")
        boolean=boolean and move_motor(arduino, 0, lower, 1)
        boolean=boolean and move_motor(arduino, lower, 0, 1)

        #Move the plate to the solution
        print("Moving the plate")
        boolean=boolean and move_motor(arduino, 0, steps_sol, 0)

         #Move the pipette and pipette sample
        print("Taking a sample")
        boolean=boolean and move_motor(arduino, 0, lower, 1)
        print(" Pipette a sample")
        boolean=boolean and generate_step(arduino, pa.Pip_sta, 1, 20,1)# Pipette sample
        boolean=boolean and move_motor(arduino, lower, 0, 1)

        #Move the plate to the EWOD plate
        print("Moving the plate")
        boolean=boolean and move_motor(arduino, steps_sol+steps_tip, 0, 0)

        #Move the pipette and release sample
        print("Droping the sample")
        boolean=boolean and move_motor(arduino, 0, lower, 1)
        print(" Pipette a sample")
        boolean=boolean and generate_step(arduino, pa.Pip_sta, 1, 20,1)# Pipette sample
        boolean=boolean and move_motor(arduino, lower, 0, 1)

        #Move the plate to the tips
        print ("Moving the plate")
        boolean=boolean and move_motor(arduino, 0 , steps_tip, 0)

        #Move the pipette and release tip
        print("Ejecting tip")
        print("Droping the sample")
        boolean=boolean and move_motor(arduino, 0, lower, 1)
        print(" Pipette a sample")
        boolean=boolean and generate_step(arduino, pa.Pip_tip, 1, 20,1)# Eject tip
        boolean=boolean and move_motor(arduino, lower, 0, 1)
         
        #Move the plate to the tips
        print("Coming back to initial position")
        boolean=boolean and move_motor(arduino, steps_tip , 0, 0)

        if change_vol: #If we have to change the volume the pipette has to pipette
            print("Changing the volume on the pipette")
            boolean=boolean and generate_step(arduino, pin2, steps, 10, 1)

        return boolean
    return boolean

# arduino=serial.Serial('/dev/cu.usbmodem14101',9600)
# Arduino_pipet(5000,2,arduino)

def Arduino_move(xbeg,ybeg,xend,yend,arduino): #TODO
    """
    This function sends the command to the Arduino to move the solution on the EWOD plate

    Entry: 
        arduino(serial): the serial connection to the Arduino
        xbeg(int): x coordinate of the beginning position
        ybeg(int): y coordinate of the beginning position
        xend(int): x coordinate of the ending position
        yend(int): y coordinate of the ending position
    Returns:
        Boolean: True if nothing went wrong
    """    
    boolean=send_and_wait_verif(arduino,'Mov')
    boolean=boolean and send_and_wait_verif(arduino, str(xbeg))
    boolean=boolean and send_and_wait_verif(arduino, str(ybeg))
    boolean=boolean and send_and_wait_verif(arduino, str(xend))
    boolean=boolean and send_and_wait_verif(arduino, str(yend))
    if not boolean:
        print("Problem comes from Arduino_move")
    return boolean

def Arduino_measure(nbmeasures, t_between_measures, pin,  arduino):
    """
    This function sends the command to the Arduino to pipet the desired amount of solution in the desired solution

    Entry: 
        arduino(serial): the serial connection to the Arduino
        nbmeasures(int): number of measurements to perform
        t_between_measures(int): time between two measurements
    Returns:
        Boolean: True if nothing went wrong
    """
    values=[]    
    boolean=True
    boolean=boolean and send_value(arduino,'5')
    boolean=boolean and send_value(arduino,str(pin))
    boolean=boolean and send_value(arduino, str(nbmeasures))
    boolean=boolean and send_value(arduino, str(t_between_measures))
    if not boolean:
        print("Problem comes from Arduino_measure")
        return boolean
    i=0
    while i<nbmeasures:
        received=str(arduino.readline())[2:-5]
        values.append(received+"\n")
        i=i+1
    fichier=open('Measures_performed.txt','w')
    fichier.writelines(values)
    fichier.close()
    return boolean

def Arduino_clean(arduino): #TODO
    """
    This function sends the command to the Arduino to pipet the desired amount of solution in the desired solution

    Entry: 
        volume(int): the volume of solution that we want to pipette
        solution(int): the solution in which we want to pipette
        arduino(serial): the serial connection to the Arduino
    Returns:
        Boolean: True if nothing went wrong
    """    
    boolean=send_and_wait_verif(arduino,'Cle')
    if not boolean:
        print("Problem comes from Arduino_clean")
    return boolean

def Arduino_thaw(arduino): #TODO
    """
    This function sends the command to the Arduino to pipet the desired amount of solution in the desired solution

    Entry: 
        volume(int): the volume of solution that we want to pipette
        solution(int): the solution in which we want to pipette
        arduino(serial): the serial connection to the Arduino
    Returns:
        Boolean: True if nothing went wrong
    """    
    boolean=send_and_wait_verif(arduino,'Tha')
    if not boolean:
        print("Problem comes from Arduino_thaw")
    return boolean

def Arduino_temperature(arduino, zone, temp): #TODO
    """
    This function sends the command to the Arduino to pipet the desired amount of solution in the desired solution

    Entry: 
        volume(int): the volume of solution that we want to pipette
        solution(int): the solution in which we want to pipette
        arduino(serial): the serial connection to the Arduino
    Returns:
        Boolean: True if nothing went wrong
    """    
    boolean=send_and_wait_verif(arduino,'Tha')
    boolean=boolean and send_and_wait_verif(arduino,str(zone))
    boolean=boolean and send_and_wait_verif(arduino,str(temp))
    if not boolean:
        print("Problem comes from Arduino_temperature")
    return boolean

def Apply_protocol(Window, protocol):
    """
    This function initializes the communication between the Arduino and the computer

    Entry:
        Window(Frame): the parent frame
    Returns:
        parameters(list): list of parameters (serial port)
    """
    #We start by creating the parameter window, where we will select the serial port and we will create the directory where all the datas will be stored
    Parameter_window=Toplevel(Window)
    Parameter_window.title('Neurodrop - Arduino parameters')
    Heading=Ff.Create_Heading(Parameter_window)
    #We recover all the ports present on the computer
    serial_ports_available=serial_ports()
    #We create the frames
    Arduino_parameters=Ff.Create_Frame(Parameter_window, border_thickness=5, style_border='groove', back_colour=sty.Bkg_frm_blue, col=1, line=2, nblines=3, nbcolumns=8, form='wens')
    Confirm_parameters=Ff.Create_Frame(Parameter_window, border_thickness=5, style_border='groove', back_colour=sty.Bkg_frm_blue, col=1, line=6, nblines=3, nbcolumns=8, form='wens')
    # We create the labels where the arduino port can be selected
    Ff.Create_text(Arduino_parameters, 'Selection of the parameters of the Arduino', color=sty.Clr_txt_frames, Police=sty.Font_frames_title, back_colour=sty.Bkg_frm_blue, col=1, line=1, form='wens', nbcolumns=1, nblines=1)
    Spin=Ff.Create_spinbox(Arduino_parameters, values=serial_ports_available, width=20, begin=0, end=0, step=1, col=1, line=3, form='wens', nbcolumns=1, nblines=1)
    Ff.Create_text(Confirm_parameters, 'Save parameters', color=sty.Clr_txt_frames, Police=sty.Font_frames_title, back_colour=sty.Bkg_frm_blue, col=1, line=1, form='wens', nbcolumns=1, nblines=1)
    Ff.Create_button(Confirm_parameters, 'Confirm & Apply parameters', partial(launch_arduino, Parameter_window, Spin, protocol, Window), color=sty.Clr_but_whit, activefg=sty.Bkg_button_active, Width=30, Height=2, Police='Arial 25', col=1, line=3, form='wens', nblines=1)
    #Configure the frames
    Ff.Auto_configure(Parameter_window, lines=[0,2,3,4,6,7,8], columns=[1,2,3,4,5,6,7,8], min_size_col=10, min_size_row=10,weight_col=1,weight_row=1)
    Ff.Auto_configure(Parameter_window, lines=[1,5,9], columns=[0,9], min_size_col=10, min_size_row=10,weight_col=0,weight_row=0)    
    Ff.Auto_configure(Heading, lines=[0], columns=[0,1,2,3,4,5,6,7], min_size_row=10, min_size_col=30, weight_col=1, weight_row=0)
    Ff.Auto_configure(Arduino_parameters, lines=[0,2,4], columns=[0,2], min_size_row=10, min_size_col=10, weight_col=1, weight_row=1)
    Ff.Auto_configure(Arduino_parameters, lines=[1,3], columns=[1], min_size_row=10, min_size_col=10, weight_col=0, weight_row=0)
    Ff.Auto_configure(Confirm_parameters, lines=[0,2,4], columns=[0,2], min_size_row=10, min_size_col=10, weight_col=1, weight_row=1)
    Ff.Auto_configure(Confirm_parameters, lines=[1,3], columns=[1], min_size_row=10, min_size_col=10, weight_col=0, weight_row=0)
    return Window

def Arduino_command(protocol, arduino):
    # Window_prec=None   
    for step in protocol:
        cmd=step[0]
        if cmd=='pip':
            vol=step[1]
            sol=step[2]
            Arduino_pipet(vol,sol, arduino) 
        elif cmd=='mov':
            xbeg=step[1]
            ybeg=step[2]
            xend=step[3]
            yend=step[4]
            Arduino_move(xbeg, ybeg, xend, yend, arduino)
        elif cmd=='lum':
            nbmes=step[1]
            t_inter_mes=step[2]
            Arduino_measure(nbmes,t_inter_mes,0,arduino)
        elif cmd=='cle':
            Arduino_clean(arduino)
        elif cmd=='tha':
            Arduino_thaw(arduino)
        elif cmd=='tem':
            zone=step[1]
            temp=step[2]
            Arduino_temperature(arduino,zone,temp)
        elif cmd=='wai':
            tim=step[1]
            time.sleep(tim)
        elif cmd!='position':
            return ValueError
    print("END of Protocol")
    

