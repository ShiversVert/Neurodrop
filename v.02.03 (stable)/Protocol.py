from tkinter import Tk, Toplevel, Text, Scrollbar, Y
from tkinter.filedialog import askopenfilename
from Framing_functions import Create_Frame, Create_text, Create_button, Auto_configure, Create_Heading, Create_menu_button
import Styles as sty
import fProtocol as fb
from functools import partial
import os
import Comunication as com

def AfficherProtocol(Window, protocol):
    """
    This function generates a list of steps in the protocol. It's primary use is to show in the right window the steps that are currently in the protocol
    
    Entry:
        Window(Frame): the parent frame
        protocol(list): the list of protocols
    """
    Create_text(Window, 'Protocol:',color=sty.Clr_txt_frames, Police=sty.Font_frames_title, back_colour=sty.Bkg_frm_blue,col=1,line=1)
    nbline=3
    for step in protocol:
        cmd=step[0]
        if cmd=='pip':
            vol=step[1]
            sol=step[2]
            Create_text(Window,'',color=sty.Clr_txt_protocol, Police=sty.Font_command, back_colour=sty.Bkg_txt_protocol, col=1, line=nbline, form='wens')
            Create_text(Window, str(nbline-2)+' - Pipet '+str(float(vol)/1000)+'µL in solution '+str(sol),color=sty.Clr_txt_protocol, Police=sty.Font_command, back_colour=sty.Bkg_txt_protocol, col=1, line=nbline, form='wns')
        elif cmd=='dep':
            Create_text(Window,'',color=sty.Clr_txt_protocol, Police=sty.Font_command, back_colour=sty.Bkg_txt_protocol, col=1, line=nbline, form='wens')
            Create_text(Window, str(nbline-2)+' - Leave the pipetted solution on the EWOD plate',color=sty.Clr_txt_protocol, Police=sty.Font_command, back_colour=sty.Bkg_txt_protocol, col=1, line=nbline, form='wns')
        elif cmd=='mov':
            xbeg=step[1]
            ybeg=step[2]
            xend=step[3]
            yend=step[4]
            Create_text(Window,'',color=sty.Clr_txt_protocol, Police=sty.Font_command, back_colour=sty.Bkg_txt_protocol, col=1, line=nbline, form='wens')
            Create_text(Window, str(nbline-2)+' - Move the droplet from ('+str(xbeg)+','+str(ybeg)+') to ('+str(xend)+','+str(yend)+')',color=sty.Clr_txt_protocol, Police=sty.Font_command, back_colour=sty.Bkg_txt_protocol, col=1, line=nbline, form='wns')
        elif cmd=='lum':
            nbmes=step[1]
            t_inter_mes=step[2]
            Create_text(Window,'',color=sty.Clr_txt_protocol, Police=sty.Font_command, back_colour=sty.Bkg_txt_protocol, col=1, line=nbline, form='wens')
            Create_text(Window, str(nbline-2)+' - Do '+str(nbmes)+' measures of luminescence, waiting '+str(t_inter_mes)+' ms between each' ,color=sty.Clr_txt_protocol, Police=sty.Font_command, back_colour=sty.Bkg_txt_protocol, col=1, line=nbline, form='wns')
        elif cmd=='cle':
            Create_text(Window,'',color=sty.Clr_txt_protocol, Police=sty.Font_command, back_colour=sty.Bkg_txt_protocol, col=1, line=nbline, form='wens')
            Create_text(Window, str(nbline-2)+' - Clean the EWOD plate',color=sty.Clr_txt_protocol, Police=sty.Font_command, back_colour=sty.Bkg_txt_protocol, col=1, line=nbline, form='wns')
        elif cmd=='tha':
            Create_text(Window,'',color=sty.Clr_txt_protocol, Police=sty.Font_command, back_colour=sty.Bkg_txt_protocol, col=1, line=nbline, form='wens')
            Create_text(Window, str(nbline-2)+' - Thaw the solutions',color=sty.Clr_txt_protocol, Police=sty.Font_command, back_colour=sty.Bkg_txt_protocol, col=1, line=nbline, form='wns')
        elif cmd=='tem':
            zone=step[1]
            temperature=step[2]
            Create_text(Window,'',color=sty.Clr_txt_protocol, Police=sty.Font_command, back_colour=sty.Bkg_txt_protocol, col=1, line=nbline, form='wens')
            Create_text(Window, str(nbline-2)+' - Put zone '+str(zone)+' to '+str(temperature)+' degrees Celsius' ,color=sty.Clr_txt_protocol, Police=sty.Font_command, back_colour=sty.Bkg_txt_protocol, col=1, line=nbline, form='wns')
        elif cmd=='wai':
            tim=step[1]
            Create_text(Window,'',color=sty.Clr_txt_protocol, Police=sty.Font_command, back_colour=sty.Bkg_txt_protocol, col=1, line=nbline, form='wens')
            Create_text(Window, str(nbline-2)+' - Wait '+str(tim)+'s' ,color=sty.Clr_txt_protocol, Police=sty.Font_command, back_colour=sty.Bkg_txt_protocol, col=1, line=nbline, form='wns')
        elif cmd=='position':
            Create_text(Window,'',color=sty.Clr_txt_position, Police=sty.Font_command, back_colour=sty.Bkg_txt_position, col=1, line=nbline, form='wens')
            Create_text(Window, str(nbline-2)+' - ACTUAL POSITION',color=sty.Clr_txt_position, Police=sty.Font_command, back_colour=sty.Bkg_txt_position, col=1, line=nbline, form='wns')
        else:
            ValueError
        nbline=nbline+1
    return Window

def ReadProtocolFile(file):
    """
    This function reads a file and returns the list 
    
    Entry:
        Window(Frame): the parent frame
        protocol(list): the list of protocols
    """
    protocol_file=open(file,'r')
    protocol=protocol_file.readlines()
    if not protocol:
        protocol=[]
    for i in range(len(protocol)):
        protocol[i]=protocol[i][:-1]
        protocol[i]=protocol[i].replace("'","")
        protocol[i]=protocol[i].split(',')
        if len(protocol[i])>1:
            for k in range(1,len(protocol[i])):
                protocol[i][k]=int(protocol[i][k])
    if not(['position'] in protocol):
        protocol.append(['position'])
    return protocol

def EcrireProtocoleFichier(proto,file):
    """
    This function writes a protocol in a file
    
    Entry:
        file(string): the string of the path of the file
        proto(list): the list of protocols
    """
    protocol_file=open(file,'w')
    li=[]
    for step in range(len(proto)):
        temp=proto[step][0]
        if len(proto[step])>1:
            for k in range(1,len(proto[step])):
                temp=temp+","+str(proto[step][k])
        li.append(temp)
        li.append("\n")
    protocol_file.writelines(li)
    protocol_file.close()
    return 1

def ProtocolWindow(Window, file_proto):
    """
    This function opens a secondary window to create or modify the measurement protocol.
    
    Entry:
        Window(Frame): the parent window
        proto(list): the list of actions
    Returns:
        protocol(list): the list of actions in the protocol
    """
    #Create the new window
    Window_protocol=Toplevel(Window)
    Window_protocol.title('Neurodrop - Protocol Window')
    #Create the list from the protocol file
    if (file_proto!=None):
        proto=ReadProtocolFile(file_proto)
    else:
        proto=[["position"]]
    EcrireProtocoleFichier(proto,'temp.txt')
    #Create the heading of the new window
    Heading=Create_Heading(Window_protocol)    
    #Create the two main frames of the window
    Comands=Create_Frame(Window_protocol, border_thickness=5, style_border='groove', back_colour=sty.Bkg_frm_blue, col=1, line=2, nblines=3, nbcolumns=3, form='wens')
    Protocol=Create_Frame(Window_protocol, border_thickness=5, style_border='groove', back_colour=sty.Bkg_frm_blue, col=6, line=2, nblines=7, nbcolumns=3, form='we')
    Position=Create_Frame(Window_protocol, border_thickness=5, style_border='groove', back_colour=sty.Bkg_frm_blue, col=1, line=6, nblines=3, nbcolumns=3, form='wens')
    #Create the command frame
    Create_text(Comands, 'Comands', color=sty.Clr_txt_frames, Police=sty.Font_frames_title, back_colour=sty.Bkg_frm_blue, col=1, line=1, form='wens', nbcolumns=1, nblines=1)
    buttons=['Pipet a solution', 'Move the droplet on the EWOD plate', 'Measure the luminescence', 'Clean the EWOD plate', 'Thaw the solutions', 'Define temperature', 'Wait']
    functions=[partial(fb.pipet, Window_protocol, Protocol,'temp.txt'),partial(fb.move, Window_protocol,Protocol,'temp.txt'), partial(fb.measure, Window_protocol,Protocol, 'temp.txt'), partial(fb.clean, Window_protocol,Protocol, 'temp.txt'), partial(fb.thaw, Window_protocol,Protocol, 'temp.txt'), partial(fb.temperature, Window_protocol,Protocol, 'temp.txt'),partial(fb.wait, Window_protocol,Protocol, 'temp.txt')]
    Create_menu_button(Comands,buttons, functions,1,3)
    #Create the position frame
    Create_text(Position, 'Position', color=sty.Clr_txt_frames, Police=sty.Font_frames_title, back_colour=sty.Bkg_frm_blue, col=1, line=1, form='wens', nbcolumns=2, nblines=1)
    Create_button(Position, 'Move up', partial(fb.PosUp, Window_protocol,Protocol, 'temp.txt'), color='#000000', activefg=sty.Bkg_button_active, Width=15, Height=2, Police=sty.Font_command, col=1, line=3, form='wens', nblines=1)
    Create_button(Position, 'Move down', partial(fb.PosDown, Window_protocol,Protocol, 'temp.txt'), color='#000000', activefg=sty.Bkg_button_active, Width=15, Height=2, Police=sty.Font_command, col=1, line=4, form='wens', nblines=1)
    Create_button(Position, 'Save', partial(fb.Save, Window_protocol,Protocol, 'temp.txt'), color='#000000', activefg=sty.Bkg_button_active, Width=15, Height=2, Police=sty.Font_command, col=2, line=3, form='wens', nblines=1)
    Create_button(Position, 'Delete last line', partial(fb.Delete, Window_protocol,Protocol, 'temp.txt'), color='#000000', activefg=sty.Bkg_button_active, Width=15, Height=2, Police=sty.Font_command, col=2, line=4, form='wens', nblines=1)
    #Create the protocol frame
    Protocol=AfficherProtocol(Protocol, proto)
    #Configure the frames
    Auto_configure(Window_protocol, lines=[1,5,9], columns=[0,4,5,9], min_size_row=10, min_size_col=10, weight_col=1, weight_row=1)
    Auto_configure(Window_protocol, lines=[2,3,4,6,7,8], columns=[1,2,3], min_size_row=10, min_size_col=30, weight_col=0, weight_row=0)
    Auto_configure(Window_protocol, lines=[2,3,4,5,6,7,8], columns=[6,7,8], min_size_row=10, min_size_col=170, weight_col=0, weight_row=0)
    Auto_configure(Heading, lines=[0], columns=[0,1,2,3,4,5,6,7], min_size_row=10, min_size_col=30, weight_col=1, weight_row=0)
    Auto_configure(Comands, lines=[0,2,10], columns=[0,2], min_size_row=10, min_size_col=10, weight_col=1, weight_row=1)
    Auto_configure(Comands, lines=[1,3,4,5,6,7,8,9], columns=[1], min_size_row=10, min_size_col=10, weight_col=0, weight_row=0)
    Auto_configure(Position, lines=[0,2,5], columns=[0,3], min_size_row=10, min_size_col=10, weight_col=1, weight_row=1)
    Auto_configure(Position, lines=[1,3,4], columns=[1,2], min_size_row=10, min_size_col=10, weight_col=0, weight_row=0)
    Auto_configure(Protocol, lines=[0,2], columns=[0,2], min_size_row=10, min_size_col=10, weight_col=1, weight_row=1)
    Auto_configure(Protocol, lines=[], columns=[1], min_size_row=10, min_size_col=10, weight_col=0, weight_row=0)
    return proto

def CreateNewProtocol(Window):
    """
    This program opens a secondary window to create a new protocol of measure.
    
    Entry:
        Window(Frame): the parent window
        protocol(list): the list of actions
    Returns:
        protocol(list): the list of actions in the protocol
    """
    protocol=ProtocolWindow(Window,None)
    return protocol

def OpenMeasureProtocol(Window, ProtocolSelected, ProtocolLine):
    """
    This function opens a measure protocol
    
    Entry:
        Window(Frame): the parent frame
        ProtocolSelected(Frame): the frame that contains the selected protocol
        protocol_chosen(list): the protocol that has been chosen, as a list
    """
    filepath = askopenfilename(title="Open a protocol",filetypes=[('txt files','.txt'),('all files','.*')])
    ProtocolSelected.config(text='Selected')
    ProtocolLine.delete('1.0', 'end')
    ProtocolLine.insert('insert',filepath)
    return 1

def ModifyProtocol(Window):
    """
    This function allows the user to open and modify a protocol
    
    Entry:
        Window(Frame): the parent frame
    """
    filepath = askopenfilename(title="Open a protocol",filetypes=[('txt files','.txt'),('all files','.*')])
    protocol=ProtocolWindow(Window,filepath)
    return protocol

def BeginMeasurement(Window, ProtocolLine):
    """
    This function reads the protocol and sends the commands to the control board (Arduino)
    
    Entry:
        Window(Frame): the parent frame
        ProtocolLine(Frame): the frame that contains the path
    """
    #We recover the path printed on the main window
    path=ProtocolLine.get(1.0,'end')[:-1]
    protocol=ReadProtocolFile(path)
    #We create the advancement window
    com.Apply_protocol(Window,protocol)

