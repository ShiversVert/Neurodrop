from tkinter import Label,Button,Frame, Spinbox, StringVar, Entry, Toplevel
import Styles as sty

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

def Create_button(Window, Text, Function, color='#000000', activefg='#318ce7', Width=30, Height=2, Police='Arial 25', col=0, line=0, form='wens', nblines=1, pady=0.1):
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
    Label_button=Button(Window, text=Text, foreground=color, activeforeground=activefg, width=Width, height=Height, font=Police, command=Function, pady=pady)
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
    Create_text(Heading, 'Neurodrop', color=sty.Clr_txt_Neuro, Police=sty.Font_Neur, back_colour=sty.Bkg_txt_Neuro, col=0, line=0, form='wens', nbcolumns=4, nblines=1)
    Create_text(Heading, 'iGEM Grenoble 2019', color=sty.Clr_txt_iGEM, Police=sty.Font_iGEM, back_colour=sty.Bkg_txt_iGEM, col=4, line=0, form='wens', nbcolumns=4, nblines=1)
    Create_text(Heading, sty.nb_version, color=sty.Clr_txt_vers, Police=sty.Font_vers, back_colour=sty.Bkg_txt_vers, col=8, line=0, form='wens', nbcolumns=2, nblines=1)
    return Heading
    
def Create_spinbox(Window, values=None, width=20, begin=0, end=0, step=1, col=0, line=0, form='wens', nbcolumns=1, nblines=1):
    """
    This function creates a Spinbox

    Entry:
        Window(Frame): the parent frame
        values(list): the values shown in the spinbox, by default it is None what means that it uses begin and end
        width(int): the size of the spinbox (in caracters)
        begin(int): if used as a spinbox of values, the starting value
        end(int): if used as a spinbox of values, the ending value
        step(int): if used as a spinbox of values, the step
        col(int): the column
        line(int): the line
        form(srt): the style
        nbcolumns(int): the number of columns
        nblines(int): the number of lines
    Returns:
        Label.Spin(Label): the spinbox well returned
    """
    if values:
        Label_Spin=Spinbox(Window, values=values, textvariable=values, width=width)
    else:
        Label_Spin=Spinbox(Window,from_=begin, to=end, increment=step, width=width)
    Label_Spin.grid(column=col,row=line,sticky=form, rowspan=nblines)
    return Label_Spin
    
def Create_Evolution_Frame(Window, step, Window_prec=None):
    """
    This function creates a secondary window with the current step being performed

    Entry:
        Window(Frame) : the parent frame
        step(str): the step being performed
    Returns:
        Window_current_step(Frame): the window of the current step
    """
    if Window_prec:
        Window_prec.destroy()
    Window_current_step=Toplevel(Window)
    Heading=Create_Heading(Window_current_step)
    Step=Create_Frame(Window_current_step, border_thickness=5, style_border='groove', back_colour=sty.Bkg_frm_blue, col=1, line=2, nblines=7, nbcolumns=8, form='wens')
    Create_text(Step, 'Current step', color=sty.Clr_txt_frames, Police=sty.Font_frames_title, back_colour=sty.Bkg_frm_blue, col=1, line=1, form='wens', nbcolumns=1, nblines=1)
    Create_text(Step, step, color=sty.Clr_txt_frames, Police=sty.Font_frames_progress, back_colour=sty.Bkg_frm_blue, col=1, line=3, form='wens', nbcolumns=1, nblines=1)
    Auto_configure(Window_current_step,lines=[1,9], columns=[0,9], min_size_row=10, min_size_col=10,weight_col=1,weight_row=1)
    Auto_configure(Window_current_step,lines=[0,2,3,4,5,6,7,8], columns=[1,2,3,4,5,6,7,8], min_size_row=10, min_size_col=10,weight_col=0,weight_row=0)    
    Auto_configure(Heading, lines=[0], columns=[0,1,2,3,4,5,6,7], min_size_row=10, min_size_col=30, weight_col=1, weight_row=0)
    Auto_configure(Step, lines=[0,2,4], columns=[0,2], min_size_row=10, min_size_col=10, weight_col=1, weight_row=1)
    Auto_configure(Step, lines=[1,3], columns=[1], min_size_row=10, min_size_col=10, weight_col=0, weight_row=0)
    return Window_current_step

def Create_menu_button(Window, buttons, functions, column, line_beg):
    """
    This function creates an array of buttons
    
    Entry: 
        Window(frame): the parent frame
        buttons(list): list with the name of the buttons
        functions(list): list with the functions to apply to each button
        column(int): the column on which the buttons are
        line_beg(int): the line at which the first button is
    Returns: 
        line_end(ind): the line at which the last button is
    """
    if not (len(buttons)==len(functions)):
        print('Create_new_button: error not the same number of functions as of buttons')
        return ValueError
    line_end=line_beg
    for i in range(len(buttons)):
        Create_button(Window, buttons[i], functions[i], color='#000000', activefg=sty.Bkg_button_active, Width=30, Height=2, Police=sty.Font_command, col=column, line=line_end, form='wens', nblines=1)
        line_end=line_end+1
    return line_end-1


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    