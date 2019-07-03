from tkinter import Label,Button,Frame, Spinbox, StringVar, Entry
from Styles import Clr_but_begin, Clr_but_whit, Clr_txt_close, Clr_txt_frames, Clr_txt_iGEM, Clr_txt_Neuro,Clr_txt_vers, Bkg_button_active, Bkg_frm_blue, Bkg_frm_white, Bkg_txt_iGEM, Bkg_txt_Neuro, Bkg_txt_vers, Font_button, Font_command, Font_frames_begin, Font_frames_title, Font_iGEM, Font_Neur, Font_vers, nb_version


def Create_Frame(Window, border_thickness=5, style_border='raised', back_colour='', col=0, line=0, nblines=1, nbcolumns=1, form='wens'):
    """
    This function creates a frame with the tkinter library
    
    Entry:
        Window(Frame): the parent frame
        border_thickness(int): the thickness of the border
        style_border(str): the type of the border
        back_colour(str): the background of the frame
        col(int): the column of the frame
        line(int): the line of the frame
        nblines(int): the number of lines on which the frame is (>0)
        nbcolumns(int): the number of columns on which the frame is (>0)
        form(str): the sticky parameter (a string containing some or all of the letters w,e,n,s)
    Returns:
        The frame with all of the parameters stated above
    
    Nota: Parameters are by default the ones of the head of the window
    """
    #Either use raised as relief or "groove"
    #Use hexadecimal values to define the background, here the color is blue
    Frame_created=Frame(Window, bd=border_thickness, relief=style_border, background=back_colour)
    Frame_created.grid(column=col, row=line, columnspan=nbcolumns, rowspan=nblines, sticky=form)
    return Frame_created

def Create_text(Window, Text, color='#e7feff', Police='Baskerville 45 italic', back_colour="#318ce7", col=0, line=0, form='wens', nbcolumns=1, nblines=1):
    """
    This function creates a text label with the tkinter library
    
    Entry:
        Window(Frame): the parent frame
        Text(str): the text of the label
        color(str): the color of the text (we recommend hexadecimal notation)
        Police(str): the font of the text
        back_colour(str): the background of the text (we recomment hexadecimal notations)
        col(int): the column at which the button is
        line(int): th row at which the button is
        form(str): the sticky parameter (a string containing some or all of the letters w,e,n,s)
    Returns:
        The label with all of the parameters stated above
    
    Nota: Parameters are by default the ones of Neurodrop
    """
    #The parameters correspon to the Neurodrop fonts and backgrounds
    Label_text=Label(Window,text=Text,foreground=color,font=Police,background=back_colour)    
    Label_text.grid(column=col,row=line, columnspan=nbcolumns, rowspan=nblines, sticky=form)
    return Label_text

def Create_button(Window, Text, Function, color='#000000', activefg='#318ce7', Width=30, Height=2, Police='Arial 25', col=0, line=0, form='wens', nblines=1):
    """
    This function creates a button label with the tkinter library
    
    Entry:
        Window(Frame): the parent frame
        Text(str): the text of the label
        activefg(str): the color of the text when pressed
        Width(int): the width of the button
        Height(int): the height of the button
        Police(str): the font of the text
        col(int): the column at which the button is
        line(int): th row at which the button is
        form(str): the sticky parameter (a string containing some or all of the letters w,e,n,s)
        Function(function): the fuction that, when the button is pressed, is started (we recommend to use a function that is then included with 'partial')
    Returns:
        The label with all of the parameters stated above
    
    Nota: Parameters are by default the ones of Neurodrop
    """
    Label_button=Button(Window, text=Text, foreground=color, activeforeground=activefg, width=Width, height=Height, font=Police, command=Function)
    Label_button.grid(column=col,row=line,sticky=form, rowspan=nblines)
    return Label_button

def Create_entry(Window, var, Width=30, Police='Arial 25', col=0, line=0, form='wens', nblines=1):
    """
    This function creates a button label with the tkinter library
    
    Entry:
        Window(Frame): the parent frame
        Text(str): the text of the label
        activefg(str): the color of the text when pressed
        Width(int): the width of the button
        Height(int): the height of the button
        Police(str): the font of the text
        col(int): the column at which the button is
        line(int): th row at which the button is
        form(str): the sticky parameter (a string containing some or all of the letters w,e,n,s)
        Function(function): the fuction that, when the button is pressed, is started (we recommend to use a function that is then included with 'partial')
    Returns:
        The label with all of the parameters stated above
    
    Nota: Parameters are by default the ones of Neurodrop
    """
    Label_entry=Entry(Window, textvariable=var, width=Width, font=Police)
    Label_entry.grid(column=col,row=line,sticky=form, rowspan=nblines)
    return Label_entry

def Auto_configure(Window, lines=[], columns=[], min_size_row=30, min_size_col=30,weight_col=1,weight_row=1):
    """
    This function configures a frame with the tkinter library
    
    Entry:
        Window(Frame): the fram to configure
        lines(list): the list of rows we want to apply the algorithm to
        columns(list): the list of columns we want to apply the algorithm to
        min_size_row(int): the minimal size of the rows in pixels
        min_size_col(int): the minimal size of the columns in pixels
        weight_col(int): the weight of the columns when we resize the window
        weight_row(int): the weight of the lines when we resize the window
    Returns:
        The frame well configurated
    """
    for c in columns:
        Window.columnconfigure(c,minsize=min_size_col,weight=1)
    for r in lines:
        Window.rowconfigure(r,minsize=min_size_row,weight=weight_row)
    return 1
    
def Create_Heading(Window):
    """
    This function creates the Neurodrop header
    
    Entry:
        Window(Frame): the parent frame
    Returns:
        The label with all of the parameters stated above
    
    Nota: Parameters are by default the ones of Neurodrop
    """
    Heading=Create_Frame(Window, border_thickness=0, style_border='flat', back_colour='', col=0, line=0, nblines=1, nbcolumns=10, form='wens')
    Create_text(Heading, 'Neurodrop', color=Clr_txt_Neuro, Police=Font_Neur, back_colour=Bkg_txt_Neuro, col=0, line=0, form='wens', nbcolumns=4, nblines=1)
    Create_text(Heading, 'iGEM Grenoble 2019', color=Clr_txt_iGEM, Police=Font_iGEM, back_colour=Bkg_txt_iGEM, col=4, line=0, form='wens', nbcolumns=4, nblines=1)
    Create_text(Heading, nb_version, color=Clr_txt_vers, Police=Font_vers, back_colour=Bkg_txt_vers, col=8, line=0, form='wens', nbcolumns=2, nblines=1)
    return Heading
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    