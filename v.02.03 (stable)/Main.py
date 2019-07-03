from tkinter import Tk,Canvas, PhotoImage, Text
from functools import partial
import Framing_functions as Ff
import Styles as sty
import Protocol as ffp
import os

# =============================================================================
# Initialisation de la fenetre
# =============================================================================

Window_main=Tk()
Window_main.title('Neurodrop - Main window')

# =============================================================================
# Creation of the labels (nomenclature: Type_name)
# =============================================================================

#Groupes
Heading=Ff.Create_Frame(Window_main, border_thickness=0, style_border='flat', back_colour='', col=0, line=0, nblines=1, nbcolumns=10, form='wens')
Protocl=Ff.Create_Frame(Window_main, border_thickness=5, style_border='groove', back_colour=sty.Bkg_frm_blue, col=1, line=2, nblines=3, nbcolumns=3, form='wens')
Measure=Ff.Create_Frame(Window_main, border_thickness=5, style_border='groove', back_colour=sty.Bkg_frm_blue, col=1, line=6, nblines=3, nbcolumns=3, form='wens')
Logofig=Ff.Create_Frame(Window_main, border_thickness=0, style_border='flat', back_colour=sty.Bkg_frm_white, col=6, line=2, nblines=3, nbcolumns=3, form='wens')
Current=Ff.Create_Frame(Window_main, border_thickness=5, style_border='groove', back_colour=sty.Bkg_frm_blue, col=6, line=6, nblines=3, nbcolumns=3, form='wens')

#Label texte
Ff.Create_text(Heading, 'Neurodrop', color=sty.Clr_txt_Neuro, Police=sty.Font_Neur, back_colour=sty.Bkg_txt_Neuro, col=0, line=0, form='wens', nbcolumns=4, nblines=1)
Ff.Create_text(Heading, 'iGEM Grenoble 2019', color=sty.Clr_txt_iGEM, Police=sty.Font_iGEM, back_colour=sty.Bkg_txt_iGEM, col=4, line=0, form='wens', nbcolumns=4, nblines=1)
Ff.Create_text(Heading, sty.nb_version, color=sty.Clr_txt_vers, Police=sty.Font_vers, back_colour=sty.Bkg_txt_vers, col=8, line=0, form='wens', nbcolumns=2, nblines=1)
Ff.Create_text(Protocl, 'Measurement Protocol', color=sty.Clr_txt_frames, Police=sty.Font_frames_title, back_colour=sty.Bkg_frm_blue, col=1, line=1, form='wens', nbcolumns=1, nblines=1)
Ff.Create_text(Measure, 'Apply Protocol', color=sty.Clr_txt_frames, Police=sty.Font_frames_title, back_colour=sty.Bkg_frm_blue, col=1, line=1, form='wens', nbcolumns=1, nblines=1)
Ff.Create_text(Current, 'Selected Protocol', color=sty.Clr_txt_frames, Police=sty.Font_frames_title, back_colour=sty.Bkg_frm_blue, col=1, line=1, form='wens', nbcolumns=1, nblines=1)
ProtocolSelected=Ff.Create_text(Current, 'None Selected', color=sty.Clr_txt_frames,Police=sty.Font_button,back_colour=sty.Bkg_frm_blue,col=1,line=3, form='wens', nbcolumns=1, nblines=1)
ProtocolLine=Text(Current, fg=sty.Clr_txt_frames,font=sty.Font_filepath,bg=sty.Bkg_frm_blue, width=50, height=4)
ProtocolLine.grid(column=1,row=5, sticky='wens', columnspan=1, rowspan=1)
#Label boutons
Ff.Create_button(Protocl, 'Create a new Protocol', partial(ffp.CreateNewProtocol, Window_main), color=sty.Clr_but_whit, activefg=sty.Bkg_button_active, Width=30, Height=2, Police='Arial 25', col=1, line=3, form='wens', nblines=1)
Ff.Create_button(Protocl, 'Modify an existing Protocol', partial(ffp.ModifyProtocol, Window_main), color=sty.Clr_but_whit, activefg=sty.Bkg_button_active, Width=30, Height=2, Police='Arial 25', col=1, line=5, form='wens', nblines=1)
Ff.Create_button(Measure, 'Load an existing Protocol', partial(ffp.OpenMeasureProtocol, Window_main, ProtocolSelected, ProtocolLine), color=sty.Clr_but_whit, activefg=sty.Bkg_button_active, Width=30, Height=2, Police='Arial 25', col=1, line=3, form='wens', nblines=1)
Ff.Create_button(Measure, 'Begin Measure', partial(ffp.BeginMeasurement, Window_main, ProtocolLine), color=sty.Clr_but_begin, activefg=sty.Bkg_button_active, Width=30, Height=2, Police=sty.Font_frames_begin, col=1, line=5, form='wens', nblines=1)

#Label Image
image=PhotoImage(file=os.getcwd()+"/Logo.png")
height=image.height()+10
width=image.width()+10
Image_neurodrop=Canvas(Logofig,width=width,height=height)
Image_neurodrop.create_image(int(width/2),int(height/2),image=image)
Image_neurodrop.grid(column=2,row=1,sticky='wens')

# =============================================================================
# Réglage des cellules de la grille
# =============================================================================

Ff.Auto_configure(Window_main, lines=[1,5,9], columns=[0,4,5,9], min_size_row=10, min_size_col=10, weight_col=1, weight_row=1)
Ff.Auto_configure(Window_main, lines=[0,2,3,4,6,7,8], columns=[1,2,3], min_size_row=10, min_size_col=10, weight_col=1, weight_row=0)
Ff.Auto_configure(Heading, lines=[0], columns=[0,1,2,3,4,5,6,7], min_size_row=10, min_size_col=30, weight_col=1, weight_row=0)
Ff.Auto_configure(Protocl, lines=[0,2,6], columns=[0,2], min_size_row=10, min_size_col=10, weight_col=1, weight_row=1)
Ff.Auto_configure(Protocl, lines=[1,3,4,5], columns=[1], min_size_row=10, min_size_col=10, weight_col=0, weight_row=0)
Ff.Auto_configure(Measure, lines=[0,2,6], columns=[0,2], min_size_row=10, min_size_col=10, weight_col=1, weight_row=1)
Ff.Auto_configure(Measure, lines=[1,3,4,5], columns=[1], min_size_row=10, min_size_col=10, weight_col=0, weight_row=0)
Ff.Auto_configure(Logofig, lines=[0,2], columns=[0,2], min_size_row=10, min_size_col=10, weight_col=1, weight_row=1)
Ff.Auto_configure(Logofig, lines=[1], columns=[1], min_size_row=10, min_size_col=10, weight_col=0, weight_row=0)
Ff.Auto_configure(Current, lines=[0,2,4], columns=[0,2], min_size_row=10, min_size_col=10, weight_col=1, weight_row=1)
Ff.Auto_configure(Current, lines=[1,3], columns=[1], min_size_row=10, min_size_col=10, weight_col=0, weight_row=0)

Window_main.mainloop()

