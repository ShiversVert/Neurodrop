import Protocol as Prot
import os
from tkinter import Spinbox, Toplevel, IntVar, Entry, Scale, Radiobutton, StringVar
from tkinter.filedialog import asksaveasfile
from Framing_functions import Create_Frame, Create_text, Create_button, Auto_configure, Create_Heading, Create_entry
from Styles import Clr_but_begin, Clr_but_whit, Clr_txt_position, Clr_txt_close, Clr_txt_frames, Clr_txt_protocol, Clr_txt_iGEM, Clr_txt_Neuro,Clr_txt_vers, Bkg_button_active, Bkg_txt_protocol, Bkg_frm_blue, Bkg_frm_white, Bkg_txt_position, Bkg_txt_iGEM, Bkg_txt_Neuro, Bkg_txt_vers, Font_button, Font_command, Font_frames_begin, Font_frames_title, Font_iGEM, Font_Neur, Font_vers, nb_version
from functools import partial


def get_value_2(Window, entry1,entry2, protocole, ProtoWindow):
    """
    This program gets 2 values from a label.
    
    Entry:
        Window(Frame): the protocol window
        entry1(Label variable): the first value to get
        entry2(Label variable): the second value to get
        protocole(list): the list of the protocole
        ProtoWindow(Frame): the protocol frame
    """
    pos=protocole.index(['position'])
    protocole[pos-1]=[protocole[pos-1][0],entry1.get(), entry2.get()]
    Prot.EcrireProtocoleFichier(protocole,'temp.txt')
    Prot.AfficherProtocol(ProtoWindow,protocole)
    Window.destroy()

def get_value_4(Window, entry1, entry2, entry3, entry4, protocole, ProtoWindow):
    """
    This program gets 4 values from a label.
    
    Entry:
        Window(Frame): the protocol window
        entry1(Label variable): the first value to get
        entry2(Label variable): the second value to get
        entry3(Label variable): the third value to get
        entry4(Label variable): the fourth value to get
        protocole(list): the list of the protocole
        ProtoWindow(Frame): the protocol frame
    """
    pos=protocole.index(['position'])
    protocole[pos-1]=[protocole[pos-1][0],entry1.get(), entry2.get(), entry3.get(), entry4.get()]
    Prot.EcrireProtocoleFichier(protocole,'temp.txt')
    Prot.AfficherProtocol(ProtoWindow,protocole)
    Window.destroy()

def get_values_matrix(Window, x, y, temp_file, ProtoWindow):
    """
    This program gets 2 positions from a matrix of labels (it is called 2 times each to add one position).
    
    Entry:
        Window(Frame): the protocol window
        x: the first value to get
        y(Label variable): the second value to get
        temp_file(string): the name of the file
        ProtoWindow(Frame): the protocol frame
    """
    protocole=Prot.ReadProtocolFile(temp_file)
    pos=protocole.index(['position'])
    protocole[pos-1]=protocole[pos-1]+[x,y]
    Prot.EcrireProtocoleFichier(protocole,'temp.txt')
    if len(protocole[pos-1])==5:
        Prot.AfficherProtocol(ProtoWindow,protocole)
        Window.destroy()

def pipet(Window, ProtoWindow, temp_file):
    """
    This program adds the pipeting instruction.
    
    Entry:
        Window(Frame): the protocol window
        ProtoWindow(Frame): the protocol frame
        temp_file(string): the name of the file
    """
    protocole=Prot.ReadProtocolFile(temp_file)
    pos=protocole.index(['position'])
    a=protocole[:pos]
    if a==[]:
        a=[['pip']]
    else:
        a=a+[['pip']]
    b=protocole[pos:]
    #Create the new window
    Window_option=Toplevel(Window)
    Window_option.title('Neurodrop - Pipette calibration')
    #Create the heading of the new window
    Heading=Create_Heading(Window_option)   
    #Create the choices of solutions and the slider for the volume
    Solution=Create_Frame(Window_option, border_thickness=5, style_border='groove', back_colour=Bkg_frm_blue, col=1, line=2, nblines=2, nbcolumns=8, form='wens')
    Create_text(Solution, 'Choose the solution', color=Clr_txt_frames, Police=Font_frames_title, back_colour=Bkg_frm_blue, col=1, line=1, form='wens', nbcolumns=3, nblines=1)
    var=IntVar()
    for i in [1,2,3]:
        R = Radiobutton(Solution, text="Solution "+str(i), variable=var, value=i, bg=Bkg_frm_blue)
        R.grid(column=i,row=3, columnspan=1, rowspan=1, sticky='we')

    scale=IntVar()
    Volume=Create_Frame(Window_option, border_thickness=5, style_border='groove', back_colour=Bkg_frm_blue, col=1, line=5, nblines=2, nbcolumns=8, form='wens')
    Create_text(Volume, 'Choose the volume (in µL)', color=Clr_txt_frames, Police=Font_frames_title, back_colour=Bkg_frm_blue, col=1, line=1, form='wens', nbcolumns=1, nblines=1)
    volscale = Scale(Volume, from_=1, to=20, variable=scale, showvalue=True, label='µL',orient='horizontal', bg=Bkg_frm_blue, length=30)
    volscale.grid(column=1,row=3, columnspan=1, rowspan=1, sticky='we')    

    Confirm=Create_Frame(Window_option, border_thickness=5, style_border='groove', back_colour=Bkg_frm_blue, col=1, line=8, nblines=1, nbcolumns=8, form='wens')
    Create_text(Confirm, 'Save parameters', color=Clr_txt_frames, Police=Font_frames_title, back_colour=Bkg_frm_blue, col=1, line=1, form='wens', nbcolumns=1, nblines=1)
    Create_button(Confirm,'OK', partial(get_value_2,Window_option, scale,var,a+b, ProtoWindow)).grid(column=1,row=3, columnspan=1, rowspan=1, sticky='wens')
    
    #Configure the window
    W=[Window_option, Window_option, Heading, Solution, Solution, Volume, Volume, Confirm, Confirm]
    Lines=[[0,2,3,4,6,7,8], [1,5,9], [0], [0,2,4], [1,3], [0,2,4], [1,3], [0,2,4], [1,3]]
    Columns=[[1,2,3,4,5,6,7,8], [0,9], [0,1,2,3,4,5,6,7], [0,4], [1,2,3], [0,2],[1], [0,2],[1]]
    WC=[0,1,1,1,0,1,0,1,0]
    WL=[0,1,0,1,0,1,0,1,0]
    for i in range(len(W)):
        Auto_configure(W[i],lines=Lines[i],columns=Columns[i],min_size_col=10,min_size_row=10,weight_col=WC[i],weight_row=WL[i])

    return 1

def dropEWOD(Window, ProtoWindow, temp_file):
    """
    This program adds the pipeting instruction.
    
    Entry:
        Window(Frame): the protocol window
        ProtoWindow(Frame): the protocol frame
        temp_file(string): the name of the file
    """
    protocole=Prot.ReadProtocolFile(temp_file)
    pos=protocole.index(['position'])
    a=protocole[:pos]
    if a==[]:
        a=[['dep']]
    else:
        a=a+[['dep']]
    b=protocole[pos:]
    protocole=a+b
    Prot.EcrireProtocoleFichier(protocole,'temp.txt')
    Prot.AfficherProtocol(ProtoWindow,protocole)
    return 1

def move(Window, ProtoWindow, temp_file):
    """
    This program adds the pipeting instruction.
    
    Entry:
        Window(Frame): the protocol window
        ProtoWindow(Frame): the protocol frame
        temp_file(string): the name of the file
    """
    protocole=Prot.ReadProtocolFile(temp_file)
    pos=protocole.index(['position'])
    a=protocole[:pos]
    if a==[]:
        a=[['mov']]
    else:
        a=a+[['mov']]
    b=protocole[pos:]
    Prot.EcrireProtocoleFichier(a+b,'temp.txt')
    #Create the new window
    Window_option=Toplevel(Window)
    Window_option.title('Neurodrop - Movement calibration')
    #Create the heading of the new window
    Heading=Create_Heading(Window_option)   
    #Create the button matrix to choose the displacement
    Matrix=Create_Frame(Window_option, border_thickness=5, style_border='groove', back_colour=Bkg_frm_blue, col=1, line=2, nblines=7, nbcolumns=8, form='wens')
    Pds_per_line=[10,10,10,10,10,10,10,10]
    Create_text(Matrix, 'Select the departure and the arriving pads', color=Clr_txt_frames, Police=Font_frames_title, back_colour=Bkg_frm_blue, col=1, line=1, form='wens', nbcolumns=max(Pds_per_line), nblines=1)
    for k in range(len(Pds_per_line)):
        for nb in range(Pds_per_line[k]):
            for i in range(nb):
                Create_button(Matrix, '', partial(get_values_matrix,Window_option,i,k,temp_file, ProtoWindow), color='#000000', activefg='#318ce7', Width=1, Height=1, Police='Arial 20', col=1+i, line=3+k, form='wens', nblines=1)
    
    #Configure the window
    W=[Window_option, Window_option, Heading, Matrix,Matrix]
    Lines=[[0,2,3,4,5,6,7,8], [1,9], [0], [0,2,4], [1,3], [0,2,len(Pds_per_line)], [1]+[i for i in range(3,2+len(Pds_per_line))]]
    Columns=[[1,2,3,4,5,6,7,8], [0,9], [0,1,2,3,4,5,6,7], [0,4], [1]+[i for i in range(max(Pds_per_line))], [0,max(Pds_per_line)]]
    WC=[0,1,1,1,0,1,0]
    WL=[0,1,0,1,0,1,0]
    for i in range(len(W)):
        Auto_configure(W[i],lines=Lines[i],columns=Columns[i],min_size_col=10,min_size_row=10,weight_col=WC[i],weight_row=WL[i])

def measure(Window, ProtoWindow, temp_file):
    """
    This program adds the pipeting instruction.
    
    Entry:
        Window(Frame): the protocol window
        ProtoWindow(Frame): the protocol frame
        temp_file(string): the name of the file
    """
    protocole=Prot.ReadProtocolFile(temp_file)
    pos=protocole.index(['position'])
    a=protocole[:pos]
    if a==[]:
        a=[['lum']]
    else:
        a=a+[['lum']]
    b=protocole[pos:]
    #Create the new window
    Window_option=Toplevel(Window)
    Window_option.title('Neurodrop - Measurement calibration')
    #Create the heading of the new window
    Heading=Create_Heading(Window_option)   
    #Create the choices of solutions and the slider for the volume
    Nb_measurements=Create_Frame(Window_option, border_thickness=5, style_border='groove', back_colour=Bkg_frm_blue, col=1, line=2, nblines=2, nbcolumns=8, form='wens')
    Create_text(Nb_measurements, 'Enter the number of measurements to perform', color=Clr_txt_frames, Police=Font_frames_title, back_colour=Bkg_frm_blue, col=1, line=1, form='wens', nbcolumns=3, nblines=1)
    nb_mes=StringVar()
    Create_entry(Nb_measurements, nb_mes, Width=30, Police='Arial 25', col=1, line=3, form='wens', nblines=1)

    Time_inter=Create_Frame(Window_option, border_thickness=5, style_border='groove', back_colour=Bkg_frm_blue, col=1, line=5, nblines=2, nbcolumns=8, form='wens')
    Create_text(Time_inter, 'Enter the time between each measurements (in ms)', color=Clr_txt_frames, Police=Font_frames_title, back_colour=Bkg_frm_blue, col=1, line=1, form='wens', nbcolumns=3, nblines=1)
    tme_mes=StringVar()
    Create_entry(Time_inter, tme_mes, Width=30, Police='Arial 25', col=1, line=3, form='wens', nblines=1)

    Confirm=Create_Frame(Window_option, border_thickness=5, style_border='groove', back_colour=Bkg_frm_blue, col=1, line=8, nblines=1, nbcolumns=8, form='wens')
    Create_text(Confirm, 'Save parameters', color=Clr_txt_frames, Police=Font_frames_title, back_colour=Bkg_frm_blue, col=1, line=1, form='wens', nbcolumns=1, nblines=1)
    Create_button(Confirm,'OK', partial(get_value_2,Window_option, nb_mes, tme_mes, a+b, ProtoWindow)).grid(column=1,row=3, columnspan=1, rowspan=1, sticky='wens')
    
    #Configure the window
    W=[Window_option, Window_option, Heading, Nb_measurements, Nb_measurements, Time_inter, Time_inter, Confirm, Confirm]
    Lines=[[0,2,3,4,6,7,8], [1,5,9], [0], [0,2,4], [1,3], [0,2,4], [1,3], [0,2,4], [1,3]]
    Columns=[[1,2,3,4,5,6,7,8], [0,9], [0,1,2,3,4,5,6,7], [0,4], [1,2,3], [0,2],[1], [0,2],[1]]
    WC=[0,1,1,1,0,1,0,1,0]
    WL=[0,1,0,1,0,1,0,1,0]
    for i in range(len(W)):
        Auto_configure(W[i],lines=Lines[i],columns=Columns[i],min_size_col=10,min_size_row=10,weight_col=WC[i],weight_row=WL[i])

    return 1

def clean(Window, ProtoWindow, temp_file):
    """
    This program adds the pipeting instruction.
    
    Entry:
        Window(Frame): the protocol window
        ProtoWindow(Frame): the protocol frame
        temp_file(string): the name of the file
    """
    protocole=Prot.ReadProtocolFile(temp_file)
    pos=protocole.index(['position'])
    print(protocole)
    a=protocole[:pos]
    if a==[]:
        a=[['cle']]
    else:
        a=a+[['cle']]
    b=protocole[pos:]
    protocole=a+b
    Prot.EcrireProtocoleFichier(protocole,'temp.txt')
    Prot.AfficherProtocol(ProtoWindow,protocole)
    return 1

def thaw(Window, ProtoWindow, temp_file):
    """
    This program adds the pipeting instruction.
    
    Entry:
        Window(Frame): the protocol window
        ProtoWindow(Frame): the protocol frame
        temp_file(string): the name of the file
    """
    protocole=Prot.ReadProtocolFile(temp_file)
    pos=protocole.index(['position'])
    a=protocole[:pos]
    if a==[]:
        a=[['tha']]
    else:
        a=a+[['tha']]
    b=protocole[pos:]
    protocole=a+b
    Prot.EcrireProtocoleFichier(protocole,'temp.txt')
    Prot.AfficherProtocol(ProtoWindow,protocole)
    return 1

def PosUp(Window, ProtoWindow, temp_file):
    """
    This program adds the pipeting instruction.
    
    Entry:
        Window(Frame): the protocol window
        ProtoWindow(Frame): the protocol frame
        temp_file(string): the name of the file
    """
    protocole=Prot.ReadProtocolFile(temp_file)
    pos=protocole.index(['position'])
    sze=len(protocole)
    a=protocole[:pos-1]
    b=[protocole[pos-1]]
    if pos<sze:
        c=protocole[pos+1:]
    else:
        c=[]
    protocole=a+[['position']]+b+c
    Prot.EcrireProtocoleFichier(protocole,'temp.txt')
    Prot.AfficherProtocol(ProtoWindow,protocole)
    return 1

def PosDown(Window, ProtoWindow, temp_file):
    """
    This program adds the pipeting instruction.
    
    Entry:
        Window(Frame): the protocol window
        ProtoWindow(Frame): the protocol frame
        temp_file(string): the name of the file
    """
    protocole=Prot.ReadProtocolFile(temp_file)
    pos=protocole.index(['position'])
    sze=len(protocole)
    a=protocole[:pos]
    if pos<sze:
        b=[protocole[pos+1]]
        c=protocole[pos+2:]
    else:
        b=[]
        c=[]
    protocole=a+b+[['position']]+c
    print(protocole)
    Prot.EcrireProtocoleFichier(protocole,'temp.txt')
    Prot.AfficherProtocol(ProtoWindow,protocole)
    return 1

def Save(Window, ProtoWindow, temp_file):
    """
    This program adds the pipeting instruction.
    
    Entry:
        Window(Frame): the protocol window
        ProtoWindow(Frame): the protocol frame
        temp_file(string): the name of the file
    """
    protocole=Prot.ReadProtocolFile(temp_file)
    os.remove(temp_file)
    pos=protocole.index(['position'])
    protocole=protocole[:pos]+protocole[pos+1:]
    filename=asksaveasfile(title="Save the protocol as",filetypes=[('txt files','.txt'),('all files','.*')])
    filename=str(filename)
    filename=filename.split("'")
    filename=filename[1]
    Prot.EcrireProtocoleFichier(protocole,filename)
    Window.destroy()
    return 1

def Delete(Window, ProtoWindow, temp_file):
    """
    This program adds the pipeting instruction.
    
    Entry:
        Window(Frame): the protocol window
        ProtoWindow(Frame): the protocol frame
        temp_file(string): the name of the file
    """
    protocole=Prot.ReadProtocolFile(temp_file)
    os.remove(temp_file)
    pos=protocole.index(['position'])
    if pos>1:
        a=protocole[:pos-1]
    else:
        a=[]
    b=protocole[pos:]
    protocole=a+b
    Prot.EcrireProtocoleFichier(protocole,'temp.txt')
    ProtoWindow=Prot.AfficherProtocol(ProtoWindow,protocole)
    return 1