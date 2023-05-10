#SSP manager main code
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import numpy as np
import mysql.connector
from PIL import Image,ImageTk,ImageGrab
import matplotlib.pyplot as plt
from datetime import datetime,date
from operator import add
from time import sleep
#Fonts, background color, text color Delclation
bg_default = '#0A1828'
fg_default ='#FFCE32'
def_input_fg ='black'
def_input_bg ='white'
font = 'Constantia' 
font_9 = (font,9)
font_12 = (font,12)
font_14 = (font,14)
font_16 = (font,16)
font_16_bold = (font,16,'bold')
heading_font = ('Russo One', 22)
enter_font = ('Lato',14)
#Time Date varialbes and string formatting
today = str(date.today())
date_time = str(datetime.now())
date_time = date_time.replace(':','-')
print(date_time)
#mysql database username and password
user_name = 'root'
passwd = 'password'

#List to store the vechile types, model and other items
vechile_type = ['2 Wheeler', '4 Wheeler']
two_wheeler_brands=['Hero Motors','Yamaha','Royal Enfield']
four_wheeler_brands=['Tata Motors']
accessories_collection = ['Engine Oil','Liquid cooler']
model_list = ['achiver','splendor','mastro','bullet','thunderbird','rx100','fazer','ray']
model_items = [8, 10, 7, 8, 9, 8, 8, 6]
#Hero Motors brand: spares in list and dictionary to store price (1D)
achiver_list = ['Airfilter','Switches set','Bearing','Break shoes','Carburattor','Chainsprkt','Cylinder','Relay']
achiver_dict = {'Airfilter':312,'Switches set':160,'Bearing':110,'Break shoes':236,'Carburattor':4253,'Chainsprkt':810,'Cylinder':1260,'Relay':130}
achiver_stock = []
splendor_list = ['Airfilter','Bearing','Break shoes','Cables','Carburattor','Chainsprkt','Cylinder','Dome Kit','Relay','Fule injuctor']
splendor_dict = {'Airfilter':312,'Bearing':110,'Break shoes':236,'Cables':355,'Carburattor':4953,'Chainsprkt':810,'Cylinder':1260,'Dome Kit':785,'Relay':130,'Fule injuctor':307}
splendor_stock = []
mastro_list = ['Airfilter','Break shoes','Cables','Carburattor','Dome Kit','Relay','Fule injuctor']
mastro_dict = {'Airfilter':312,'Break shoes':236,'Cables':355,'Carburattor':3853,'Dome Kit':785,'Relay':130,'Fule injuctor':307}
mastro_stock = []
#Royal Enfield brand: spares in list and dictionary to store price (1D)
bullet_list = ['Airfilter','Switches set','Headlight Dom','Clutch plate','Lock kit','Chainsprkt','Wiring hornes','Ignition switch']
bullet_dict = {'Airfilter':168,'Switches set':470,'Headlight Dom':496,'Clutch plate':299,'Lock kit':594,'Chainsprkt':2065,'Wiring hornes':660,'Ignition switch':785}
bullet_stock = []
thunderBird_list = ['Airfilter','Switches set','Headlight Dom','CDI','Clutch plate','Cable','Chainsprkt','Break Wires','Oil Filter']
thunderBird_dict = {'Airfilter':168,'Switches set':470,'Headlight Dom':496,'CDI':601,'Clutch plate':299,'Cable':594,'Chainsprkt':2742,'Break Wires':126,'Oil Filter':34}
thunderBird_stock = []
#Yamaha brand: spares in list and dictionary to store price (1D)
rx100_list = ['Airfilter','Switches set','Clutch plate','Break shoes','Reg Regulator','Chainsprkt','CDI', 'Dom assembly']
rx100_dict = {'Airfilter':312,'Switches set':160,'Clutch plate':250,'Break shoes':236,'Reg Regulator':180,'Chainsprkt':1205,'CDI':167,'Dom assembly':925}
rx100_stock = []
fazer_list = ['Airfilter','Switches set','Clutch plate','Break shoes','Clutch Cable','Chainsprkt','CDI', 'Dom assembly']
fazer_dict = {'Airfilter':312,'Switches set':345,'Clutch plate':290,'Break shoes':246,'Clutch Cable':183,'Chainsprkt':1072,'CDI':1276,'Dom assembly':2164}
fazer_stock = []
ray_list = ['Air Filter','Break Shoes','Wiring Harnes','Acc Cable','Clutch cable','Reg Regulator']
ray_dict = {'Air Filter':140,'Break Shoes':252,'Wiring Harnes':1436,'Acc Cable':297,'Clutch cable':261,'Reg Regulator':980}
ray_stock = []
#HeadLight, LEDs, other led and lights list and dictionary to store price (1D)
led_list = ['HS1(35W)','HS4(55W)','HS1/HS4 LED','T10','T6','H7(80W)','H7 LED','H8/9/11 LED','C6 LED','LED Strip','Tail LED','COB Strip','Fog Light','Switch ','2 Way Switch']
led_dict = {'HS1(35W)':120,'HS4(55W)':180,'HS1/HS4 LED':750,'T10':199,'T6':150,'H7(80W)':600,'H7 LED':1800,'H8/9/11 LED':1757,'C6 LED':220,'LED Strip':1760,'Tail LED':499,'COB Strip':449,'Fog Light':399,'Switch ':65,'2 Way Switch':85}

#Engine oils list and dictionary to store price (1D)
engineOil_list=['Shell 20W30','Shell 5W30','Castor 15W40','Castor 5W40', 'Shell 10W30','Shell 5W30(5L)']
engineOil_dict={'Shell 20W30':234,'Shell 5W30':245,'Castor 15W40':310,'Castor 5W40':350, 'Shell 10W30':287,'Shell 5W30(5L)':1450}
#Coolant Liquid list and dictionary to store price (1D)
coolant_list = ['4cx Antifreeze', 'Castor Radicool', 'Bosch F002H', 'Motul Inugel', 'UE Radiant(5L)']
coolant_dict = {'4cx Antifreeze':246, 'Castor Radicool':268, 'Bosch F002H':171, 'Motul Inugel':210, 'UE Radiant(5L)':1099}

#creating windown with Tkinter object
root=Tk() #main windown created with root as object
root.title('SSP Manager')
root.config(bg='lightblue')
frame=Frame(root,bg=bg_default) #frame window created inside the root window updatable for each page
frame.place(relx=0,rely=0,relheight=1,relwidth=1) #frame covers the main window
#-----------------------------#-----------------------------#-----------------------------#-----------------------------#-----------------------------
#Class to create two wheeler data in the frame called by funtion "call_by_vechile_type" from brand page    
class two_wheeler():
    #Init funtion to call default GUI elements 
    def __init__(self):
        clear_frame() #Clear pervious frame wigets
        title_label = Label(frame, text='Spare Parts Manager', font=('arial',24),fg=fg_default,bg=bg_default)
        title_label.place(relx=0.5,rely=0.05,anchor=CENTER)
        heading_label = Label(frame,text='Select Part for the model', font=('arial', 18),fg=fg_default,bg=bg_default)
        heading_label.place(relx=0.5,rely=0.13,anchor=CENTER)
        #dummy line to separate GUI for reference
        line_label_1 = Label(frame,text='    ',font=('arial',1),width=680,height=1)
        line_label_1.place(relx=0.5,rely=0.19,anchor=CENTER)
    #Class Funtion to call and display hero spares based on their model
    def hero_model(self):
        #button to move next page which display button
        bill_button= Button(frame, text='Make Bill',font=font_14,bg='#FFD700',fg='purple',activebackground='#d4af27',activeforeground='purple', command=lambda:get_items('hero'))
        bill_button.place(relx=0.9,rely=0.1,anchor=CENTER)
        #Achiver ModelLabel
        achiver_label_title = Label(frame,text='Achiver 2006 Price',font=('arial', 14),fg=fg_default,bg=bg_default)
        achiver_label_title.place(relx=0.16,rely=0.24,anchor=CENTER)
        #parts in achiver base model
        achiver_spares_label = [Label(frame, text=achiver_list[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(8)]
        j=1 #loop to create multiple lables achiver
        for achiver_label in achiver_spares_label:
            achiver_label.place(relx=0.18,rely=(0.25+(j*0.07)),anchor=E)
            j+=1
        global achiver_spares #global variable to store achiver spares values
        achiver_spares = [Entry(frame, fg=def_input_fg, bg=def_input_bg, font=enter_font, bd=2, width=2) for x in range(8)]
        j=1 #loop to create multiple entry achiver
        for achiver_entry in achiver_spares:
            achiver_entry.place(relx=0.21,rely=(0.25+(j*0.07)),anchor=CENTER)
            j+=1

        achiver_spares_cost_label = [Label(frame, text=(achiver_dict[achiver_list[x]],"/-"), fg=fg_default, bg=bg_default, font=font_14) for x in range(8)]
        j=1 #loop to create multiple lables achiver
        for achiver_cost_label in achiver_spares_cost_label:
            achiver_cost_label.place(relx=0.30,rely=(0.25+(j*0.07)),anchor=E)
            j+=1

        #Splendor Model Label
        splendor_label_title = Label(frame,text='Splendor 2010',font=('arial', 14),fg=fg_default,bg=bg_default)
        splendor_label_title.place(relx=0.5,rely=0.24,anchor=CENTER)
        #parts in Splendor base model
        splendor_spares_label = [Label(frame, text=splendor_list[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(10)]
        j=1 #loop to create multiple lables splendor
        for splendor_label in splendor_spares_label:
            splendor_label.place(relx=0.5,rely=(0.25+(j*0.07)),anchor=E)
            j+=1
        global splendor_spares #global variable to store splendor spares values
        splendor_spares = [Entry(frame, fg=def_input_fg, bg=def_input_bg, font=enter_font, bd=2, width=2) for x in range(10)]
        j=1 #loop to create multiple entry splendor
        for splendor_entry in splendor_spares:
            splendor_entry.place(relx=0.55,rely=(0.25+(j*0.07)),anchor=CENTER)
            j+=1
        splendor_spares_cost_label = [Label(frame, text=splendor_dict[splendor_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(10)]
        j=1 #loop to create multiple lables splendor
        for splendor_cost_label in splendor_spares_cost_label:
            splendor_cost_label.place(relx=0.64,rely=(0.25+(j*0.07)),anchor=E)
            j+=1

        #Mastro Model Label
        mastro_label_title = Label(frame,text='Mastro 2016',font=('arial', 14),fg=fg_default,bg=bg_default)
        mastro_label_title.place(relx=0.8,rely=0.24,anchor=CENTER)
        #parts in mastro base model
        mastro_spares_label = [Label(frame, text=mastro_list[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(7)]
        j=1 #loop to create multiple lables mastro
        for mastro_label in mastro_spares_label:
            mastro_label.place(relx=0.82,rely=(0.25+(j*0.07)),anchor=E)
            j+=1
        global mastro_spares #global variable to store mastro spares values
        mastro_spares = [Entry(frame, fg=def_input_fg, bg=def_input_bg, font=enter_font, bd=2, width=2) for x in range(7)]
        j=1 #loop to create multiple entry mastro
        for mastro_entry in mastro_spares:
            mastro_entry.place(relx=0.87,rely=(0.25+(j*0.07)),anchor=CENTER)
            j+=1
        mastro_spares_cost_label = [Label(frame, text=mastro_dict[mastro_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(7)]
        j=1 #loop to create multiple lables mastro
        for mastro_cost_label in mastro_spares_cost_label:
            mastro_cost_label.place(relx=0.96,rely=(0.25+(j*0.07)),anchor=E)
            j+=1
    #Class Funtion to call and display royal enfield spares based on their model 
    def re_model(self):
        #button to move next page which display button
        bill_button= Button(frame, text='Make Bill',font=font_14,bg='#FFD700',fg='purple',activebackground='#d4af27',activeforeground='purple', command=lambda:get_items('re'))
        bill_button.place(relx=0.9,rely=0.1,anchor=CENTER)
        #Bullter model
        bullet_label_title = Label(frame,text='Bullet base',font=('arial', 14),fg=fg_default,bg=bg_default)
        bullet_label_title.place(relx=0.3,rely=0.24,anchor=CENTER)
        #parts in bullet base model
        bullet_spares_label = [Label(frame, text=bullet_list[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(8)]
        j=1 #loop to create multiple lables bullet
        for bullet_label in bullet_spares_label:
            bullet_label.place(relx=0.33,rely=(0.25+(j*0.07)),anchor=E)
            j+=1
        global bullet_spares
        bullet_spares = [Entry(frame, fg=def_input_fg, bg=def_input_bg, font=enter_font, bd=2, width=2) for x in range(8)]
        j=1 #loop to create multiple entry bullet
        for bullet_entry in bullet_spares:
            bullet_entry.place(relx=0.38,rely=(0.25+(j*0.07)),anchor=CENTER)
            j+=1
        bullet_spares_cost_label = [Label(frame, text=bullet_dict[bullet_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(8)]
        j=1 #loop to create multiple lables bullet
        for bullet_cost_label in bullet_spares_cost_label:
            bullet_cost_label.place(relx=0.48,rely=(0.25+(j*0.07)),anchor=E)
            j+=1

        #thunderBird Model Label
        thunderBird_label_title = Label(frame,text='Thunder Bird',font=('arial', 14),fg=fg_default,bg=bg_default)
        thunderBird_label_title.place(relx=0.7,rely=0.24,anchor=CENTER)
        #parts in thunderBird base model
        thunderBird_spares_label = [Label(frame, text=thunderBird_list[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(9)]
        j=1 #loop to create multiple lables thunder bird
        for thunderBird_label in thunderBird_spares_label:
            thunderBird_label.place(relx=0.7,rely=(0.25+(j*0.07)),anchor=E)
            j+=1
        global thunderBird_spares
        thunderBird_spares = [Entry(frame, fg=def_input_fg, bg=def_input_bg, font=enter_font, bd=2, width=2) for x in range(9)]
        j=1 #loop to create multiple entry thunder bird
        for thunderBird_entry in thunderBird_spares:
            thunderBird_entry.place(relx=0.75,rely=(0.25+(j*0.07)),anchor=CENTER)
            j+=1
        thunderBird_spares_cost_label = [Label(frame, text=thunderBird_dict[thunderBird_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(9)]
        j=1 #loop to create multiple lables thunderBird
        for thunderBird_cost_label in thunderBird_spares_cost_label:
            thunderBird_cost_label.place(relx=0.85,rely=(0.25+(j*0.07)),anchor=E)
            j+=1
    #Class Funtion to call and display yamaha spares based on their model 
    def yamaha_model(self):
        #button to move next page which display button
        bill_button= Button(frame, text='Make Bill',font=font_14,bg='#FFD700',fg='purple',activebackground='#d4af27',activeforeground='purple', command=lambda:get_items('yamaha'))
        bill_button.place(relx=0.9,rely=0.1,anchor=CENTER)
        #rx100 ModelLabel
        rx100_label_title = Label(frame,text='Rx100 1990',font=('arial', 14),fg=fg_default,bg=bg_default)
        rx100_label_title.place(relx=0.155,rely=0.24,anchor=CENTER)
        #parts in rx100 base model
        rx100_spares_label = [Label(frame, text=rx100_list[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(8)]
        j=1 #loop to create multiple lables rx100
        for rx100_label in rx100_spares_label:
            rx100_label.place(relx=0.18,rely=(0.25+(j*0.07)),anchor=E)
            j+=1
        global rx100_spares
        rx100_spares = [Entry(frame, fg=def_input_fg, bg=def_input_bg, font=enter_font, bd=2, width=2) for x in range(8)]
        j=1 #loop to create multiple entry rx100
        for rx100_entry in rx100_spares:
            rx100_entry.place(relx=0.21,rely=(0.25+(j*0.07)),anchor=CENTER)
            j+=1
        rx100_spares_cost_label = [Label(frame, text=rx100_dict[rx100_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(8)]
        j=1 #loop to create multiple lables rx100
        for rx100_cost_label in rx100_spares_cost_label:
            rx100_cost_label.place(relx=0.30,rely=(0.25+(j*0.07)),anchor=E)
            j+=1

        #fazer Model Label
        fazer_label_title = Label(frame,text='Fazer 2010',font=('arial', 14),fg=fg_default,bg=bg_default)
        fazer_label_title.place(relx=0.5,rely=0.24,anchor=CENTER)
        #parts in fazer base model
        fazer_spares_label = [Label(frame, text=fazer_list[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(8)]
        j=1 #loop to create multiple lables fazer
        for fazer_label in fazer_spares_label:
            fazer_label.place(relx=0.5,rely=(0.25+(j*0.07)),anchor=E)
            j+=1
        global fazer_spares
        fazer_spares = [Entry(frame, fg=def_input_fg, bg=def_input_bg, font=enter_font, bd=2, width=2) for x in range(8)]
        j=1 #loop to create multiple entry fazer
        for fazer_entry in fazer_spares:
            fazer_entry.place(relx=0.55,rely=(0.25+(j*0.07)),anchor=CENTER)
            j+=1
        fazer_spares_cost_label = [Label(frame, text=fazer_dict[fazer_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(8)]
        j=1 #loop to create multiple lables fazer
        for fazer_cost_label in fazer_spares_cost_label:
            fazer_cost_label.place(relx=0.64,rely=(0.25+(j*0.07)),anchor=E)
            j+=1

        #ray Model Label
        ray_label_title = Label(frame,text='Ray 2017',font=('arial', 14),fg=fg_default,bg=bg_default)
        ray_label_title.place(relx=0.8,rely=0.24,anchor=CENTER)
        #parts in ray base model
        ray_spares_label = [Label(frame, text=ray_list[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(6)]
        j=1 #loop to create multiple lables ray
        for ray_label in ray_spares_label:
            ray_label.place(relx=0.84,rely=(0.25+(j*0.07)),anchor=E)
            j+=1
        global ray_spares
        ray_spares = [Entry(frame, fg=def_input_fg, bg=def_input_bg, font=enter_font, bd=2, width=2) for x in range(6)]
        j=1 #loop to create multiple entry ray
        for ray_entry in ray_spares:
            ray_entry.place(relx=0.89,rely=(0.25+(j*0.07)),anchor=CENTER)
            j+=1
        ray_spares_cost_label = [Label(frame, text=ray_dict[ray_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(6)]
        j=1 #loop to create multiple lables ray
        for ray_cost_label in ray_spares_cost_label:
            ray_cost_label.place(relx=0.98,rely=(0.25+(j*0.07)),anchor=E)
            j+=1

             
#Class to create Other items data in the frame called by funtion "call_by_vechile_type" from brand page    
class others_items():
    def  __init__(self):
        clear_frame()
        title_label = Label(frame, text='Spare Parts Manager', font=('arial',24),fg=fg_default,bg=bg_default)
        title_label.place(relx=0.5,rely=0.05,anchor=CENTER)
        heading_label = Label(frame,text='Select Part for the model', font=('arial', 18),fg=fg_default,bg=bg_default)
        heading_label.place(relx=0.5,rely=0.13,anchor=CENTER)
        #dummy line to separate GUI for reference
        line_label_1 = Label(frame,text='    ',font=('arial',1),width=680,height=1)
        line_label_1.place(relx=0.5,rely=0.19,anchor=CENTER)
    def engineOil(self):
        #button to move next page which display button
        bill_button= Button(frame, text='Make Bill',font=font_14,bg='#FFD700',fg='purple',activebackground='#d4af27',activeforeground='purple', command=lambda:get_items('engineOil'))
        bill_button.place(relx=0.9,rely=0.1,anchor=CENTER)
        #engineOil ModelLabel
        engineOil_label_title = Label(frame,text='Liquid Coolant(Each pack is of 1L Quantity)',font=('arial', 14),fg=fg_default,bg=bg_default)
        engineOil_label_title.place(relx=0.5,rely=0.24,anchor=CENTER)
        #parts in engineOil base model
        engineOil_spares_label = [Label(frame, text=engineOil_list[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(engineOil_list))]
        j=1 #loop to create multiple lables engineOil
        for engineOil_label in engineOil_spares_label:
            engineOil_label.place(relx=0.5,rely=(0.25+(j*0.07)),anchor=E)
            j+=1
        global engineOil_spares #global variable to store engineOil spares values
        engineOil_spares = [Entry(frame, fg=def_input_fg, bg=def_input_bg, font=enter_font, bd=2, width=2) for x in range(len(engineOil_list))]
        j=1 #loop to create multiple entry engineOil
        for engineOil_entry in engineOil_spares:
            engineOil_entry.place(relx=0.6,rely=(0.25+(j*0.07)),anchor=CENTER)
            j+=1
        engineOil_spares_cost_label = [Label(frame, text=engineOil_dict[engineOil_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(engineOil_list))]
        j=1 #loop to create multiple lables engineOil
        for engineOil_cost_label in engineOil_spares_cost_label:
            engineOil_cost_label.place(relx=0.7,rely=(0.25+(j*0.07)),anchor=E)
            j+=1
    def coolant(self):
        #button to move next page which display button
        bill_button= Button(frame, text='Make Bill',font=font_14,bg='#FFD700',fg='purple',activebackground='#d4af27',activeforeground='purple', command=lambda:get_items('coolant'))
        bill_button.place(relx=0.9,rely=0.1,anchor=CENTER)
        #coolant ModelLabel
        coolant_label_title = Label(frame,text='Engine Oil(Each pack is of 1L Quantity)',font=('arial', 14),fg=fg_default,bg=bg_default)
        coolant_label_title.place(relx=0.5,rely=0.24,anchor=CENTER)
        #parts in coolant base model
        coolant_spares_label = [Label(frame, text=coolant_list[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(coolant_list))]
        j=1 #loop to create multiple lables coolant
        for coolant_label in coolant_spares_label:
            coolant_label.place(relx=0.5,rely=(0.25+(j*0.07)),anchor=E)
            j+=1
        global coolant_spares #global variable to store coolant spares values
        coolant_spares = [Entry(frame, fg=def_input_fg, bg=def_input_bg, font=enter_font, bd=2, width=2) for x in range(len(coolant_list))]
        j=1 #loop to create multiple entry coolant
        for coolant_entry in coolant_spares:
            coolant_entry.place(relx=0.6,rely=(0.25+(j*0.07)),anchor=CENTER)
            j+=1

        coolant_spares_cost_label = [Label(frame, text=coolant_dict[coolant_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(coolant_list))]
        j=1 #loop to create multiple lables coolant
        for coolant_cost_label in coolant_spares_cost_label:
            coolant_cost_label.place(relx=0.7,rely=(0.25+(j*0.07)),anchor=E)
            j+=1
#Class to create four wheeler data in the frame called by funtion "call_by_vechile_type" from brand page   
class four_wheeler():
    #Init funtion to call default GUI elements 
    def __init__(self):
        clear_frame()
        title_label = Label(frame, text='Spare Parts Manager', font=('arial',24),fg=fg_default,bg=bg_default)
        title_label.place(relx=0.5,rely=0.05,anchor=CENTER)
        heading_label = Label(frame,text='Select Part for the model', font=('arial', 18),fg=fg_default,bg=bg_default)
        heading_label.place(relx=0.5,rely=0.13,anchor=CENTER)
        #dummy line to separate GUI for reference
        line_label_1 = Label(frame,text='    ',font=('arial',1),width=680,height=1)
        line_label_1.place(relx=0.5,rely=0.19,anchor=CENTER)
    #Class Funtion to call and display hero spares based on their model
    def honda_model(self):
        #button to move next page which display button
        bill_button= Button(frame, text='Make Bill',font=font_14,bg='#FFD700',fg='purple',activebackground='#d4af27',activeforeground='purple', command=lambda:get_items('hero'))
        bill_button.place(relx=0.9,rely=0.1,anchor=CENTER)
        #Achiver ModelLabel
        achiver_label_title = Label(frame,text='Achiver 2006',font=('arial', 14),fg=fg_default,bg=bg_default)
        achiver_label_title.place(relx=0.155,rely=0.24,anchor=CENTER)
        #parts in achiver base model
        achiver_spares_label = [Label(frame, text=achiver_list[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(8)]
        j=1 #loop to create multiple lables achiver
        for achiver_label in achiver_spares_label:
            achiver_label.place(relx=0.18,rely=(0.25+(j*0.07)),anchor=E)
            j+=1
        global achiver_spares #global variable to store achiver spares values
        achiver_spares = [Entry(frame, fg=def_input_fg, bg=def_input_bg, font=enter_font, bd=2, width=2) for x in range(8)]
        j=1 #loop to create multiple entry achiver
        for achiver_entry in achiver_spares:
            achiver_entry.place(relx=0.21,rely=(0.25+(j*0.07)),anchor=CENTER)
            j+=1

        achiver_spares_cost_label = [Label(frame, text=achiver_dict[achiver_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(8)]
        j=1 #loop to create multiple lables achiver
        for achiver_cost_label in achiver_spares_cost_label:
            achiver_cost_label.place(relx=0.30,rely=(0.25+(j*0.07)),anchor=E)
            j+=1

        #Splendor Model Label
        splendor_label_title = Label(frame,text='Splendor 2010',font=('arial', 14),fg=fg_default,bg=bg_default)
        splendor_label_title.place(relx=0.5,rely=0.24,anchor=CENTER)
        #parts in Splendor base model
        splendor_spares_label = [Label(frame, text=splendor_list[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(10)]
        j=1 #loop to create multiple lables splendor
        for splendor_label in splendor_spares_label:
            splendor_label.place(relx=0.5,rely=(0.25+(j*0.07)),anchor=E)
            j+=1
        global splendor_spares #global variable to store splendor spares values
        splendor_spares = [Entry(frame, fg=def_input_fg, bg=def_input_bg, font=enter_font, bd=2, width=2) for x in range(10)]
        j=1 #loop to create multiple entry splendor
        for splendor_entry in splendor_spares:
            splendor_entry.place(relx=0.55,rely=(0.25+(j*0.07)),anchor=CENTER)
            j+=1
        splendor_spares_cost_label = [Label(frame, text=splendor_dict[splendor_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(10)]
        j=1 #loop to create multiple lables splendor
        for splendor_cost_label in splendor_spares_cost_label:
            splendor_cost_label.place(relx=0.64,rely=(0.25+(j*0.07)),anchor=E)
            j+=1

        #Mastro Model Label
        mastro_label_title = Label(frame,text='Mastro 2016',font=('arial', 14),fg=fg_default,bg=bg_default)
        mastro_label_title.place(relx=0.8,rely=0.24,anchor=CENTER)
        #parts in mastro base model
        mastro_spares_label = [Label(frame, text=mastro_list[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(7)]
        j=1 #loop to create multiple lables mastro
        for mastro_label in mastro_spares_label:
            mastro_label.place(relx=0.82,rely=(0.25+(j*0.07)),anchor=E)
            j+=1
        global mastro_spares #global variable to store mastro spares values
        mastro_spares = [Entry(frame, fg=def_input_fg, bg=def_input_bg, font=enter_font, bd=2, width=2) for x in range(7)]
        j=1 #loop to create multiple entry mastro
        for mastro_entry in mastro_spares:
            mastro_entry.place(relx=0.87,rely=(0.25+(j*0.07)),anchor=CENTER)
            j+=1
        mastro_spares_cost_label = [Label(frame, text=mastro_dict[mastro_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(7)]
        j=1 #loop to create multiple lables mastro
        for mastro_cost_label in mastro_spares_cost_label:
            mastro_cost_label.place(relx=0.96,rely=(0.25+(j*0.07)),anchor=E)
            j+=1
    #Class Funtion to call and display royal enfield spares based on their model 

#Funtion to clear the frame in root window to move next frame
def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()
#show analytics data in graphical data, label and message box
def show_analytics(get_data):
    #lists to store values from different columns from the sql database
    #Columns inclued Date Item Price Count Brand VechileType
    date_order = []
    price = []
    item = []
    count = []
    brand = []
    #Connect to MySQL database
    database = mysql.connector.connect(
        host='localhost',
        user=user_name,
        password=passwd,
        database='SparePartsManager',
        auth_plugin='mysql_native_password',
        port=3306
    )
    print(database)
    myCursor = database.cursor()
    myCursor.execute('Select * from salesdata;')
    myCursor.close
    #get data from the the database table and append values to list
    for x in myCursor:
        date_order.append(x[0])
        item.append(x[1])
        price.append(int(x[2]))
        count.append(x[3])
        brand.append(x[4])
    brands_list = ['Hero', 'RE','Yamaha'] #Brand in 2 wheeler
    values = [brand.count('Hero Motors'),brand.count('Royal Enfield'),brand.count('Yamaha')] #count the number of item sold in differnt brands and store in the list
    other_list = ['Led Spares','Engine Oil','Coolant'] #other items 
    other_val = [brand.count('Led Spares'), brand.count('Engine Oil'),brand.count('Coolant')] #other item count sold
    #Display the total number of items sold
    if get_data =='items_sold':
        print('Total number of items sold so for: {}'.format(len(item)))
        status_label.config(text='Total number of items sold: {}'.format(len(item)))
    #Display the total amount of revenue
    if get_data == 'revenue':
        status_label.config(text='Total Revenue: {}/- Rupees'.format(sum(price)))
    #plot bar graph of items sold in different brands
    if get_data =='graph': 
        plt.title('Showing total sales of parts based on the brands')
        plt.bar(brands_list,values,color=['red','dimgray','blue'])
    #plot pie chat of items sold in different brands
    if get_data=='show_pie':
        plt.title('Showing Pie-Chart of items sold based on the brand')
        plt.pie(values, labels = brands_list)
    #plot the histogram of spares sold by date on particular brand or other items
    if get_data == 'brand_show':
        comp = brand_show.get()
        status_label.config(text='No. of items sold in {}: {}'.format(comp,brand.count(comp)))
        myCursor.execute("select Date,Count from salesdata where Brand='{}' ;".format(comp))
        comp_data = []
        comp_brand = []
        for x in myCursor:
            comp_data.append(x[0])
            comp_brand.append(x[1])
        plt.title('Histogram of Item Sold in {}'.format(comp))
        plt.hist(comp_brand)
    #plot the graph on date and sales rate
    if get_data == 'salersByCost':
        plt.title('Showing sales by date')
        plt.plot(count,date_order)
    #plot bar graph of other items sold
    if get_data == 'missee':
        plt.title('Showing the sales of miscellaneous items')
        plt.bar(other_list,other_val,color=['cyan','m','orange'])
    #Displat the tax paid totally and profit
    if get_data == 'Tax_profit':
        status_label.config(text='Total Tax (INR): {a:.2f}/-\nTotal Profit (INR): {b}/-'.format(a=((12/100)*sum(price)),b=((sum(price))-((12/100)*sum(price))/1.6)))
    plt.show() #plot the created graph
#Funtion to get and display values from the database
def analytics():
    clear_frame()
    root.geometry('640x520')
    title_label = Label(frame, text='Spare Parts Manager', font=('arial',24),fg=fg_default,bg=bg_default)
    title_label.place(relx=0.5,rely=0.05,anchor=CENTER)
    heading_label = Label(frame,text='SSP Manager Analytics', font=('arial', 18),fg=fg_default,bg=bg_default)
    heading_label.place(relx=0.5,rely=0.13,anchor=CENTER)
    items_sold = Button(frame, text='Total Items\nSold',font=font_12, fg='white',bg='#002948',command=lambda: show_analytics('items_sold'))
    items_sold.place(relx=0.1,rely=0.22,anchor=CENTER)
    revenue_button = Button(frame,text='Total\nRevenue',font=font_12, fg='white',bg='#002948',command=lambda: show_analytics('revenue'))
    revenue_button.place(relx=0.25,rely=0.22,anchor=CENTER)
    list_button = Button(frame,text='Spare Sales\nGraph',font=font_12, fg='white',bg='#002948',command=lambda: show_analytics('graph'))
    list_button.place(relx=0.40,rely=0.22,anchor=CENTER)
    pie_button = Button(frame,text='Sales % Chart',font=font_12, fg='white',bg='#002948',command=lambda: show_analytics('show_pie'))
    pie_button.place(relx=0.58,rely=0.22,anchor=CENTER)
    global brand_show
    brand_listed = ['Hero Motors', 'Royal Enfield','Yamaha','Engine Oil','Coolant','Led Spares']
    brand_show = ttk.Combobox(frame,state = 'readonly', values=brand_listed,font=('arial'),width=12)
    brand_show.place(relx=0.78,rely=0.22,anchor=CENTER)
    brand_show_button = Button(frame,text='Show',font=font_12, fg='white',bg='#002948',command=lambda: show_analytics('brand_show'))
    brand_show_button.place(relx=0.93,rely=0.22,anchor=CENTER)
    salersByCost = Button(frame,text='Timeline',font=font_12, fg='white',bg='#002948',command=lambda: show_analytics('salersByCost'))
    salersByCost.place(relx=0.1,rely=0.32,anchor=CENTER)
    missee = Button(frame,text='Other Sales',font=font_12, fg='white',bg='#002948',command=lambda: show_analytics('missee'))
    missee.place(relx=0.25,rely=0.32,anchor=CENTER)
    tax_profit = Button(frame,text='Tax/Profit',font=font_12, fg='white',bg='#002948',command=lambda: show_analytics('Tax_profit'))
    tax_profit.place(relx=0.40,rely=0.32,anchor=CENTER)
    global status_label
    status_label = Label(frame,text='',font=font_14,fg='black',bg='white',height=10,width=55)
    status_label.place(relx=0.5,rely=0.5,anchor=N)
    print('analytcs')
#funtoin to call the item required to sell using list values
def get_items(get_model):
    database = mysql.connector.connect(
            host='localhost',
            user=user_name,
            password=passwd,
            database='SparePartsManager',
            auth_plugin='mysql_native_password',
            port=3306
        )
    my_cursor = database.cursor()
    #Create global lists to store the items to be billed
    global bill_achiver,bill_splendor,bill_mastro,bill_bullet,bill_thunderBird,bill_rx100,bill_fazer,bill_ray
    bill_achiver = []
    bill_splendor = []
    bill_mastro = []
    bill_bullet = []
    bill_thunderBird = []
    bill_rx100 = []
    bill_fazer = []
    bill_ray = []
    #get values from Hero spares if value is empty replace by 0
    print(get_model)
    if get_model =='hero':
        #achiver get data
        for achiver_vals in achiver_spares:
            val=achiver_vals.get()    
            if val=="":
                val=0
            bill_achiver.append(int(val))
        for x in range(len(achiver_list)):
            achiver_stock[x] = achiver_stock[x]-bill_achiver[x]
        my_cursor.execute('delete from achiver;')
        for i in range(len(achiver_stock)):
            my_cursor.execute('INSERT INTO achiver values({})'.format(achiver_stock[i]))
        #splendor get data
        for splendor_vals in splendor_spares:
            val=splendor_vals.get()
            if val=='':
                val=0
            bill_splendor.append(int(val))
        for x in range(len(splendor_list)):
            splendor_stock[x]=splendor_stock[x]-bill_splendor[x]
        my_cursor.execute('delete from splendor;')
        for i in range(len(splendor_stock)):
            my_cursor.execute('INSERT INTO splendor values({})'.format(splendor_stock[i]))
        #mastro get data
        for mastro_vals in mastro_spares:
            val = mastro_vals.get()
            if val=='':
                val=0
            bill_mastro.append(int(val))
        for x in range(len(mastro_list)):
            mastro_stock[x]=mastro_stock[x]-bill_mastro[x]
        my_cursor.execute('delete from mastro;')
        for i in range(len(mastro_stock)):
            my_cursor.execute('INSERT INTO mastro values({})'.format(mastro_stock[i]))
        make_bill_bike('hero_get_list')
        database.commit()
    #get values from RE spares if value is empty replace by 0
    elif get_model=='re':
        #bullet get data
        for bullet_vals in bullet_spares:
            val=bullet_vals.get()    
            if val=="":
                val=0
            bill_bullet.append(int(val))
        for x in range(len(bullet_list)):
            bullet_stock[x]=bullet_stock[x]-bill_bullet[x]
        my_cursor.execute('delete from bullet;')
        for i in range(len(bullet_stock)):
            my_cursor.execute('INSERT INTO bullet values({})'.format(bullet_stock[i]))
        for thunderBird_vals in thunderBird_spares:
            val=thunderBird_vals.get()
            if val=='':
                val=0
            bill_thunderBird.append(int(val))
        for x in range(len(thunderBird_stock)):
            thunderBird_stock[x]=thunderBird_stock[x]-bill_thunderBird[x]
        my_cursor.execute('delete from thunderbird;')
        for i in range(len(thunderBird_stock)):
            my_cursor.execute('INSERT INTO thunderbird values({})'.format(thunderBird_stock[i]))
        make_bill_bike('re_get_list')
        database.commit()
    #get values from yamaha spares if value is empty replace by 0
    elif get_model=='yamaha':
        for rx100_vals in rx100_spares:
            val=rx100_vals.get()    
            if val=="":
                val=0
            bill_rx100.append(int(val))
        for x in range(len(rx100_list)):
            rx100_stock[x]=rx100_stock[x]-bill_rx100[x]
        my_cursor.execute('delete from rx100;')
        for i in range(len(rx100_stock)):
            my_cursor.execute('INSERT INTO rx100 values({})'.format(rx100_stock[i]))
        for fazer_vals in fazer_spares:
            val=fazer_vals.get()
            if val=='':
                val=0
            bill_fazer.append(int(val))
        for x in range(len(fazer_list)):
            fazer_stock[x]=fazer_stock[x]-bill_fazer[x]
        my_cursor.execute('delete from fazer;')
        for i in range(len(fazer_stock)):
            my_cursor.execute('INSERT INTO fazer values({})'.format(fazer_stock[i]))
        for ray_vals in ray_spares:
            val = ray_vals.get()
            if val=='':
                val=0
            bill_ray.append(int(val))
        for x in range(len(ray_list)):
            ray_stock[x]=ray_stock[x]-bill_ray[x]
        my_cursor.execute('delete from ray;')
        for i in range(len(ray_stock)):
            my_cursor.execute('INSERT INTO ray values({})'.format(ray_stock[i]))
        make_bill_bike('yamaha_get_list')
        database.commit()
    #print('Achiver: ',bill_achiver,'\n','Splendor: ',bill_splendor,'\n','Mastro: ',bill_mastro)
    #print('Bullet: ',bill_bullet,'\n','Thunder Bird: ',bill_thunderBird)
    #print('rx100: ',bill_rx100,'\n','fazer: ',bill_fazer,'\n','ray: ',bill_ray) 
    global bill_led
    bill_led = []
    if get_model == 'leds':
        for led_vals in led_spares:
            val=led_vals.get()    
            if val=="":
                val=0
            bill_led.append(int(val))
        make_bill_bike('led_get_list')
    #get items in engine oil list if value is empty replace by 0
    global bill_engineOil
    bill_engineOil = []
    if get_model == 'engineOil':
        for led_vals in engineOil_spares:
            val=led_vals.get()    
            if val=="":
                val=0
            bill_engineOil.append(int(val))
        make_bill_bike('engineOil_get_list')
    #get items in coolant list if value is empty replace by 0
    global bill_coolant
    bill_coolant = []
    if get_model == 'coolant':
        for led_vals in coolant_spares:
            val=led_vals.get()    
            if val=="":
                val=0
            bill_coolant.append(int(val))
        make_bill_bike('coolant_get_list')
    #print('Led list: ',bill_led)

#Funtion set to Update stock values in the spaes for 2wheeler model
#Funtion order select model set stock value append to database
def update_list(get_brand):
    messagebox.showwarning('SSPM Warning','You are update Stock in stock list')
    new_stock = []
    database = mysql.connector.connect(
        host='localhost',
        user=user_name,
        password=passwd,
        database='SparePartsManager',
        auth_plugin='mysql_native_password',
        port=3306
        )
    my_cursor = database.cursor()
    #update stock values in hero brand
    if get_brand=='hero':
        for x in stock_achiver_entry:
            stock = x.get()
            if stock =="":
                stock=0
            new_stock.append(int(stock))
        for x in range(len(new_stock)):
            achiver_stock[x] = achiver_stock[x]+new_stock[x]
        my_cursor.execute('delete from achiver;')
        for x in range(len(achiver_stock)):
            my_cursor.execute('INSERT INTO achiver values({});'.format(achiver_stock[x]))
        new_stock.clear()
        for x in stock_splendor_entry:
            stock = x.get()
            if stock =="":
                stock=0
            new_stock.append(int(stock))
        for x in range(len(new_stock)):
            splendor_stock[x] = splendor_stock[x]+new_stock[x]
        my_cursor.execute('delete from splendor;')
        for x in range(len(splendor_stock)):
            my_cursor.execute('INSERT INTO splendor values({});'.format(splendor_stock[x]))
        new_stock.clear()
        for x in stock_mastro_entry:
            stock = x.get()
            if stock =="":
                stock=0
            new_stock.append(int(stock))
        for x in range(len(new_stock)):
            mastro_stock[x] = mastro_stock[x]+new_stock[x]
        my_cursor.execute('delete from mastro;')
        for x in range(len(mastro_stock)):
            my_cursor.execute('INSERT INTO mastro values({});'.format(mastro_stock[x]))
        new_stock.clear()
    #update stock values in re brand
    if get_brand == 're':
        for x in stock_bullet_entry:
            stock = x.get()
            if stock =="":
                stock=0
            new_stock.append(int(stock))
        for x in range(len(new_stock)):
            bullet_stock[x] = bullet_stock[x]+new_stock[x]
        my_cursor.execute('delete from bullet;')
        for x in range(len(bullet_stock)):
            my_cursor.execute('INSERT INTO bullet values({});'.format(bullet_stock[x]))
        new_stock.clear()
        for x in stock_thunderBird_entry:
            stock = x.get()
            if stock=="":
                stock=0
            new_stock.append(int(stock))
        for x in range(len(new_stock)):
            thunderBird_stock[x] = thunderBird_stock[x]+new_stock[x]
        my_cursor.execute('delete from thunderbird;')
        for x in range(len(thunderBird_stock)):
            my_cursor.execute('INSERT INTO thunderbird values({});'.format(thunderBird_stock[x]))
        new_stock.clear()
    #update stock values in yamaha brand
    if get_brand == 'yamaha':
        for x in stock_rx_100_entry:
            stock = x.get()
            if stock =="":
                stock=0
            new_stock.append(int(stock))
        for x in range(len(new_stock)):
            rx100_stock[x] = rx100_stock[x]+new_stock[x]
        my_cursor.execute('delete from rx100;')
        for x in range(len(rx100_stock)):
            my_cursor.execute('INSERT INTO rx100 values({});'.format(rx100_stock[x]))
        new_stock.clear()
        for x in stock_fazer_entry:
            stock = x.get()
            if stock =="":
                stock=0
            new_stock.append(int(stock))
        for x in range(len(new_stock)):
            fazer_stock[x] = fazer_stock[x]+new_stock[x]
        my_cursor.execute('delete from fazer;')
        for x in range(len(fazer_stock)):
            my_cursor.execute('INSERT INTO fazer values({});'.format(fazer_stock[x]))
        new_stock.clear()
        for x in stock_ray_entry:
            stock = x.get()
            if stock =="":
                stock=0
            new_stock.append(int(stock))
        for x in range(len(new_stock)):
            ray_stock[x] = ray_stock[x]+new_stock[x]
        my_cursor.execute('delete from ray;')
        for x in range(len(ray_stock)):
            my_cursor.execute('INSERT INTO ray values({});'.format(ray_stock[x]))
        new_stock.clear()
    print('List updater')
    database.commit()
    messagebox.showinfo('SSPM Info',"Stock List updated!")    
    login()
def update_stock(get_brand):
    clear_frame()
    root.geometry('690x520')
    title_label = Label(frame, text='Spare Parts Manager', font=('arial',24),fg=fg_default,bg=bg_default)
    title_label.place(relx=0.5,rely=0.03,anchor=CENTER)
    heading_label = Label(frame,text='Enter number of items to be added', font=('arial', 18),fg=fg_default,bg=bg_default)
    heading_label.place(relx=0.5,rely=0.1,anchor=CENTER)
    
    #Hero stock update enter and lable
    if get_brand == 'hero':
        topic_label = Label(frame,text='Achiver\t\t\tSplendor\t\t\tMastro',font=font_16,fg=fg_default,bg=bg_default)
        topic_label.place(relx=0.5,rely=0.17,anchor=CENTER)
        #achiver Stock update labels and entry
        stock_achiver_lable = [Label(frame,text=achiver_list[x],font=font_14,fg=fg_default,bg=bg_default) for x in range(len(achiver_list))]
        k=0.23  
        for x in stock_achiver_lable:
            x.place(relx=0.12,rely=k,anchor=CENTER)
            k+=0.08
        global stock_achiver_entry
        stock_achiver_entry = [Entry(frame,fg=def_input_fg,bg=def_input_bg,font=font_14 ,width=2)for x in range(len(achiver_list))]
        k=0.23   
        for x in stock_achiver_entry:
            x.place(relx=0.24,rely=k,anchor=CENTER)
            k+=0.08
        #aplendor Stock update labels and entry
        stock_splendor_lable = [Label(frame,text=splendor_list[x],font=font_14,fg=fg_default,bg=bg_default) for x in range(len(splendor_list))]
        k=0.23
        for x in stock_splendor_lable: 
            x.place(relx=0.42,rely=k,anchor=CENTER)
            k+=0.08
        global stock_splendor_entry
        stock_splendor_entry = [Entry(frame,fg=def_input_fg,bg=def_input_bg,font=font_14 ,width=2)for x in range(len(splendor_list))]
        k=0.23 
        for x in stock_splendor_entry:
            x.place(relx=0.55,rely=k,anchor=CENTER)
            k+=0.08
        #mastro Stock update labels and entry
        stock_mastro_lable = [Label(frame,text=mastro_list[x],font=font_14,fg=fg_default,bg=bg_default) for x in range(len(mastro_list))]
        k=0.23
        for x in stock_mastro_lable: 
            x.place(relx=0.72,rely=k,anchor=CENTER)
            k+=0.08
        global stock_mastro_entry
        stock_mastro_entry = [Entry(frame,fg=def_input_fg,bg=def_input_bg,font=font_14 ,width=2)for x in range(len(mastro_list))]
        k=0.23 
        for x in stock_mastro_entry:
            x.place(relx=0.85,rely=k,anchor=CENTER)
            k+=0.08

        set_brand = 'hero'
    #RE stock update enter and lable
    if get_brand == 're':
        topic_label = Label(frame,text='Bullet\t\t\tThunderBird',font=font_16,fg=fg_default,bg=bg_default)
        topic_label.place(relx=0.5,rely=0.17,anchor=CENTER)
        #bullet Stock update labels and entry
        stock_bullet_lable = [Label(frame,text=bullet_list[x],font=font_14,fg=fg_default,bg=bg_default) for x in range(len(bullet_list))]
        k=0.23  
        for x in stock_bullet_lable:
            x.place(relx=0.22,rely=k,anchor=CENTER)
            k+=0.08
        global stock_bullet_entry
        stock_bullet_entry = [Entry(frame,fg=def_input_fg,bg=def_input_bg,font=font_14 ,width=2)for x in range(len(bullet_list))]
        k=0.23   
        for x in stock_bullet_entry:
            x.place(relx=0.35,rely=k,anchor=CENTER)
            k+=0.08
        #thunderBird Stock update labels and entry
        stock_thunderBird_lable = [Label(frame,text=thunderBird_list[x],font=font_14,fg=fg_default,bg=bg_default) for x in range(len(thunderBird_list))]
        k=0.23 
        for x in stock_thunderBird_lable: 
            x.place(relx=0.62,rely=k,anchor=CENTER)
            k+=0.08
        global stock_thunderBird_entry
        stock_thunderBird_entry = [Entry(frame,fg=def_input_fg,bg=def_input_bg,font=font_14 ,width=2)for x in range(len(thunderBird_list))]
        k=0.23 
        for x in stock_thunderBird_entry:
            x.place(relx=0.75,rely=k,anchor=CENTER)
            k+=0.08
        set_brand='re'
    #Yamaha stock update enter and lable
    if get_brand == 'yamaha':
        topic_label = Label(frame,text='Rx100\t\t\tFazer\t\tRay',font=font_16,fg=fg_default,bg=bg_default)
        topic_label.place(relx=0.45,rely=0.17,anchor=CENTER)
        #rx_100 Stock update labels and entry
        stock_rx_100_lable = [Label(frame,text=rx100_list[x],font=font_14,fg=fg_default,bg=bg_default) for x in range(len(rx100_list))]
        k=0.23  
        for x in stock_rx_100_lable:
            x.place(relx=0.12,rely=k,anchor=CENTER)
            k+=0.08
        global stock_rx_100_entry
        stock_rx_100_entry = [Entry(frame,fg=def_input_fg,bg=def_input_bg,font=font_14 ,width=2)for x in range(len(rx100_list))]
        k=0.23   
        for x in stock_rx_100_entry:
            x.place(relx=0.24,rely=k,anchor=CENTER)
            k+=0.08
        #fazer Stock update labels and entry
        stock_fazer_lable = [Label(frame,text=fazer_list[x],font=font_14,fg=fg_default,bg=bg_default) for x in range(len(fazer_list))]
        k=0.23
        for x in stock_fazer_lable: 
            x.place(relx=0.42,rely=k,anchor=CENTER)
            k+=0.08
        global stock_fazer_entry
        stock_fazer_entry = [Entry(frame,fg=def_input_fg,bg=def_input_bg,font=font_14 ,width=2)for x in range(len(fazer_list))]
        k=0.23 
        for x in stock_fazer_entry:
            x.place(relx=0.55,rely=k,anchor=CENTER)
            k+=0.08
        #ray Stock update labels and entry
        stock_ray_lable = [Label(frame,text=ray_list[x],font=font_14,fg=fg_default,bg=bg_default) for x in range(len(ray_list))]
        k=0.23
        for x in stock_ray_lable: 
            x.place(relx=0.72,rely=k,anchor=CENTER)
            k+=0.08
        global stock_ray_entry
        stock_ray_entry = [Entry(frame,fg=def_input_fg,bg=def_input_bg,font=font_14 ,width=2)for x in range(len(ray_list))]
        k=0.23 
        for x in stock_ray_entry:
            x.place(relx=0.85,rely=k,anchor=CENTER)
            k+=0.08

        set_brand = 'yamaha'
    
    update_button = Button(frame, text='Update Stock',font=font_12, fg='red',bg='yellow',command=lambda: update_list(set_brand))
    update_button.place(relx=0.9,rely=0.1,anchor=CENTER)
    #print('Update stock')
def update_stock_brand_select():
    clear_frame()
    root.geometry('560x240')
    title_label = Label(frame, text='Spare Parts Manager', font=('arial',24),fg=fg_default,bg=bg_default)
    title_label.place(relx=0.5,rely=0.07,anchor=CENTER)
    heading_label = Label(frame,text='Select Brand to Update Stock', font=('arial', 18),fg=fg_default,bg=bg_default)
    heading_label.place(relx=0.5,rely=0.22,anchor=CENTER)

    #stock update setup for hero
    stock_achiver = Button(frame, text='Hero Motors',font=font_16, fg='white',bg='#002948',command=lambda: update_stock('hero'))
    stock_achiver.place(relx=0.2,rely=0.55,anchor=CENTER)
    stock_splendor = Button(frame, text='Royal Enfield',font=font_16, fg='white',bg='#002948',command=lambda: update_stock('re'))
    stock_splendor.place(relx=0.5,rely=0.55,anchor=CENTER)
    stock_mastro = Button(frame, text='Yamaha',font=font_16, fg='white',bg='#002948',command=lambda: update_stock('yamaha'))
    stock_mastro.place(relx=0.8,rely=0.55,anchor=CENTER)

    analytics_button = Button(frame,text='Sales Analytics',font=font_14,fg='red',bg='yellow',command=analytics)
    analytics_button.place(relx=0.5,rely=0.9,anchor=CENTER)

    print('brand select')
#Funtion to generate 2Wheeler and 4Wheeler brand selector 
def brands():
    vechile_type_val = vechile_comb.get()
    #print(vechile_type_val)
    root.geometry('690x520')
    clear_frame()
    heading_label = Label(frame, text='Select Brand or Accesories',font=font_16, fg=fg_default,bg=bg_default)
    heading_label.place(relx=0.5,rely=0.22,anchor=CENTER)
    accessories_label = Label(frame, text='Two Wheeler Accessories',font=('arial',12),bg=bg_default,fg=fg_default)
    accessories_label.place(relx=0.5,rely=0.8,anchor=CENTER)
    accessories_comb = ttk.Combobox(frame,state='readonly',values=accessories_collection,font=('arial'),width=12)
    accessories_comb.current(0)
    accessories_comb.place(relx=0.5,rely=0.87,anchor=CENTER)
    search_button = Button(frame, text='Search', font=font_14,bg='#FFD700',fg='purple',activebackground='#d4af27',activeforeground='purple',command=lambda:call_by_vechile_type(accessories_comb.get()))
    search_button.place(relx=0.7,rely=0.87,anchor=CENTER)
    #function to call 2wheeler vechiles
    if vechile_type_val == '2 Wheeler':
        title_label = Label(frame, text='Two Wheeler\nSpare Parts Manager',font=heading_font,fg=fg_default,bg=bg_default)
        title_label.place(relx=0.5,rely=0.1,anchor=CENTER)
        #image display for hero
        hero_img= (Image.open(r"C:\SparePartsManagementSystem\icons\hero.png"))
        hero_img= hero_img.resize((150,150), Image.ANTIALIAS)
        hero_img= ImageTk.PhotoImage(hero_img)
        hero_img_label = Label(frame,image=hero_img)
        hero_img_label.image = hero_img # keep a reference!
        hero_img_label.place(relx=0.2,rely=0.45,anchor=CENTER)

        hero_button = Button(frame,text='Hero Motors',font=font_14,bg='#FFD700',fg='purple',activebackground='#d4af27',activeforeground='purple', command=lambda: call_by_vechile_type('hero'))
        hero_button.place(relx=0.2,rely=0.7,anchor=CENTER)
        #image display for re
        re_img= (Image.open(r"C:\SparePartsManagementSystem\icons\re.png"))
        re_img= re_img.resize((150,150), Image.ANTIALIAS)
        re_img= ImageTk.PhotoImage(re_img)
        re_img_label = Label(frame,image=re_img)
        re_img_label.image = re_img # keep a reference!
        re_img_label.place(relx=0.5,rely=0.45,anchor=CENTER)

        re_button = Button(frame,text='Royal Enfield',font=font_14,bg='#FFD700',fg='purple',activebackground='#d4af27',activeforeground='purple',command=lambda: call_by_vechile_type('re'))
        re_button.place(relx=0.5,rely=0.7,anchor=CENTER)
        #image display for yamaha
        yamaha_img= (Image.open(r"C:\SparePartsManagementSystem\icons\yamaha.png"))
        yamaha_img= yamaha_img.resize((150,150), Image.ANTIALIAS)
        yamaha_img= ImageTk.PhotoImage(yamaha_img)
        yamaha_img_label = Label(frame,image=yamaha_img)
        yamaha_img_label.image = yamaha_img # keep a reference!
        yamaha_img_label.place(relx=0.8,rely=0.45,anchor=CENTER)

        yamaha_button = Button(frame,text='Yamaha',font=font_14,bg='#FFD700',fg='purple',activebackground='#d4af27',activeforeground='purple',command=lambda: call_by_vechile_type('yamaha'))
        yamaha_button.place(relx=0.8,rely=0.7,anchor=CENTER)
    #condtion to call 4Wheeler vechiles
    elif vechile_type_val == '4 Wheeler':
        title_label = Label(frame, text='Four Wheeler\nSpare Parts Manager',font=heading_font,fg=fg_default,bg=bg_default)
        title_label.place(relx=0.5,rely=0.1,anchor=CENTER)

        honda_img= (Image.open(r"C:\SparePartsManagementSystem\icons\honda.png"))
        honda_img= honda_img.resize((200,150), Image.ANTIALIAS)
        honda_img= ImageTk.PhotoImage(honda_img)
        honda_img_label = Label(frame,image=honda_img)
        honda_img_label.image = honda_img # keep a reference!
        honda_img_label.place(relx=0.3,rely=0.45,anchor=CENTER)

        honda_button = Button(frame,text='Honda',font=font_14,bg='#FFD700',fg='purple',activebackground='#d4af27',activeforeground='purple')
        honda_button.place(relx=0.3,rely=0.7,anchor=CENTER)

        tata_img= (Image.open(r"C:\SparePartsManagementSystem\icons\tata.png"))
        tata_img= tata_img.resize((200,150), Image.ANTIALIAS)
        tata_img= ImageTk.PhotoImage(tata_img)
        tata_img_label = Label(frame,image=tata_img)
        tata_img_label.image = tata_img # keep a reference!
        tata_img_label.place(relx=0.7,rely=0.45,anchor=CENTER)

        tata_button = Button(frame,text='Tata Motors',font=font_14,bg='#FFD700',fg='purple',activebackground='#d4af27',activeforeground='purple')
        tata_button.place(relx=0.7,rely=0.7,anchor=CENTER)

#Funtion to call class funtion for two wheeler 
def call_by_vechile_type(get_vechile_type):
    #create separate object of classes two_wheeler and other items
    two_wheeler_obj = two_wheeler()
    others_items_obj = others_items()
    if get_vechile_type == 'hero':
        two_wheeler_obj.hero_model()
    elif get_vechile_type == 're':
        two_wheeler_obj.re_model()
    elif get_vechile_type == 'yamaha':
        two_wheeler_obj.yamaha_model()
    elif get_vechile_type == 'Engine Oil':
        others_items_obj.engineOil()
    elif get_vechile_type == 'Liquid cooler':
        others_items_obj.coolant()

#call the value from brand and model list makes the bill value and print in the frame 
#funtion to take screenshort of the Invoice and save as PDF
def printBill(widget):
    #using ImageGrab from PIL to get the location the Tkinter window and snap the region the window
    img = ImageGrab.grab(bbox=(
        widget.winfo_rootx(),
        widget.winfo_rooty(),
        widget.winfo_rootx() + widget.winfo_width(),
        widget.winfo_rooty() + widget.winfo_height()
    ))
    #save the image to local storage as pdf with date 
    filename = r'C:\SparePartsManagementSystem\SSP_Bills\SSP Bill '+date_time+'.pdf'
    im_1 = img.convert('RGB')
    im_1.save(filename)
    print('Bill Saved!')
    thank_you()
# Closing page to print invoice (printing invoice is a dummy processes)
def thank_you():
    clear_frame()
    title_label = Label(frame, text='Spare Parts Manager',font=heading_font,fg=fg_default,bg=bg_default)
    title_label.place(relx=0.5,rely=0.05,anchor=CENTER)    
    heading_label = Label(frame, text='Thanks for Shopping\nPrint Invoice',font=font_16, fg=fg_default,bg=bg_default)
    heading_label.place(relx=0.5,rely=0.14,anchor=CENTER)
    print_button = Button(frame,text='Print Invoice',fg=fg_default,bg=bg_default,command=printer,font=font_14)
    print_button.place(relx=0.5,rely=0.30,anchor=CENTER)
    home_button = Button(frame,text='Home',fg=fg_default,bg=bg_default,command=lambda:home_page('admin','12345'),font=font_14)
    home_button.place(relx=0.5,rely=0.40,anchor=CENTER)
#function to show the printing info (dummy)
def printer():
    messagebox.showinfo('SSP Manager','Invoice Printing....\n PDF stored to Local storage')

def deco():
    clear_frame()
    root.geometry('640x480')
    title_label = Label(frame, text='Spare Parts Manager', font=('arial',24),fg=fg_default,bg=bg_default)
    title_label.place(relx=0.5,rely=0.05,anchor=CENTER)
    heading_label = Label(frame,text='Select the LED/Halogen Bulb', font=('arial', 18),fg=fg_default,bg=bg_default)
    heading_label.place(relx=0.5,rely=0.13,anchor=CENTER)
    #dummy line to separate GUI for reference
    line_label_1 = Label(frame,text='    ',font=('arial',1),width=680,height=1)
    line_label_1.place(relx=0.5,rely=0.19,anchor=CENTER)
    led_bill_button = Button(frame, text='Make Bill', font=font_14,bg='#FFD700',fg='purple',activebackground='#d4af27',activeforeground='purple',command=lambda:get_items('leds'))
    led_bill_button.place(relx=0.9,rely=0.1,anchor=CENTER)

    led_deco_label = [Label(frame, text=led_list[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(led_list))]
    j=0.25 #loop to create multiple lables led list
    for led_label in led_deco_label:
        if j<0.9:
            led_label.place(relx=0.3,rely=((j)),anchor=E)
        else:
            led_label.place(relx=0.7,rely=((j-0.7)),anchor=E)
        j+=0.1

    global led_spares
    led_spares = [Entry(frame, fg=def_input_fg, bg=def_input_bg, font=enter_font, bd=2, width=2) for x in range(len(led_list))]
    j=0.25 #loop to create multiple entry bullet
    for led_entry in led_spares:
        if j<0.9:
            led_entry.place(relx=0.38,rely=(j),anchor=E)
        else:
            led_entry.place(relx=0.78,rely=((j-0.7)),anchor=E)
        j+=0.1

    print('led decos')
#Funtion to generate bill page and caulation also to update stockdata and salesdata in database
def make_bill_bike(list_items): 
    clear_frame()   
    root.geometry("690x560")
    root.resizable(0,0)
    global database
    database = mysql.connector.connect(
        host='localhost',
        user=user_name,
        password=passwd,
        database='SparePartsManager',
        auth_plugin='mysql_native_password',
        port=3306
    )
    print(database)
    my_cursor = database.cursor()
    #Title and heading label of billing window
    title_label = Label(frame, text='Spare Parts Manager',font=heading_font,fg=fg_default,bg=bg_default)
    title_label.place(relx=0.5,rely=0.05,anchor=CENTER)    
    heading_label = Label(frame, text='SSP Shop Invoice\n(GST: 12%)',font=font_16, fg=fg_default,bg=bg_default)
    heading_label.place(relx=0.5,rely=0.14,anchor=CENTER)
    date_label = Label(frame,text=today,font=font_14,fg=fg_default,bg=bg_default)
    date_label.place(relx=0.9,rely=0.12,anchor=CENTER)
    #varialble decalared to handle data from the Entry from tkinter 
    #varibles declared to handle tkinter label posistion depends on the count of components
    samp_title = 0
    samp_count = 0
    same_cost = 0
    global index_list
    global index_items
    index_list = []
    index_items = []
    #variables declared to handle count of hero parts only
    global achiver_count
    achiver_count = []
    global achiver_cost
    achiver_cost = []
    global splendor_count
    splendor_count = []
    global mastro_count
    mastro_count = []
    #varialbe to handle count cost values
    global count_cost
    #collect data from Components page and print in billing page for Hero Parts
    if list_items=='hero_get_list':
        if sum(bill_achiver) !=0:
            for i in range(len(bill_achiver)):
                if bill_achiver[i]>0:
                    #index = bill_achiver.index(i)
                    index_list.append(i)
                    achiver_count.append(bill_achiver[i])      

            #print(achiver_count)
            achiver_bill_label = [Label(frame, text=achiver_list[index_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for bill_place in achiver_bill_label:
                bill_place.place(relx=0.21,rely=(0.30+samp_title),anchor=CENTER)
                samp_title=samp_title+0.07
            
            achiver_count_label = [Label(frame, text=achiver_count[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(achiver_count))]
            for count_lable in achiver_count_label:
                count_lable.place(relx=0.45,rely=(0.30+samp_count),anchor=CENTER)
                samp_count=samp_count+0.07

            
            achiver_cost_list = [achiver_dict[achiver_list[index_list[x]]] for x in range(len(index_list))]
            count_cost = [achiver_cost_list[x]*achiver_count[x] for x in range(len(achiver_count))]
            #print(count_cost)
            
            achiver_cost_label = [Label(frame, text=count_cost[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for price_place in achiver_cost_label:
                price_place.place(relx=0.65,rely=(0.30+same_cost),anchor=CENTER)
                same_cost=same_cost+0.07
            #sql upload data to table
            for x in range(len(index_list)):
                sleep(0.1)
                date_time = str(datetime.now())
                date_time = date_time.replace(':','-')
                my_cursor.execute("insert into salesdata values('{today_date}', '{part}', {cost}, '{count}', 'Hero Motors', 'W2');".format(today_date=date_time,part=achiver_list[index_list[x]],cost=(achiver_dict[achiver_list[index_list[x]]]*achiver_count[x]),count=achiver_count[x]))
            my_cursor.close()        
            print('SQL data updated!')
        if sum(bill_splendor) !=0:
            for i in range(len(bill_splendor)):
                if bill_splendor[i]>0:
                    #index = bill_splendor.index(i)
                    index_list.append(i)
                    splendor_count.append(bill_splendor[i])
                    

            splendor_bill_label = [Label(frame, text=splendor_list[index_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for bill_place in splendor_bill_label:
                bill_place.place(relx=0.21,rely=(0.30+samp_title),anchor=CENTER)
                samp_title=samp_title+0.07
            
            splendor_count_label = [Label(frame, text=splendor_count[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(splendor_count))]
            for count_lable in splendor_count_label:
                count_lable.place(relx=0.45,rely=(0.30+samp_count),anchor=CENTER)
                samp_count=samp_count+0.07            
            
            splendor_cost_list = [splendor_dict[splendor_list[index_list[x]]] for x in range(len(index_list))]
            count_cost = [splendor_cost_list[x]*splendor_count[x] for x in range(len(splendor_count))]
            #print(count_cost)
            
            splendor_cost_label = [Label(frame, text=count_cost[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for price_place in splendor_cost_label:
                price_place.place(relx=0.65,rely=(0.30+same_cost),anchor=CENTER)
                same_cost=same_cost+0.07
            for x in range(len(index_list)):
                sleep(0.1)
                date_time = str(datetime.now())
                date_time = date_time.replace(':','-')
                my_cursor.execute("insert into salesData values('{today_date}', '{part}', {cost}, '{count}', 'Hero Motors', 'W2');".format(today_date=date_time,part=splendor_list[index_list[x]],cost=(splendor_dict[splendor_list[index_list[x]]]*splendor_count[x]),count=splendor_count[x]))
            my_cursor.close()  
            print('Data uploaded to database')
        if sum(bill_mastro) !=0:
            for i in range(len(bill_mastro)):
                if bill_mastro[i]>0:
                    #index = bill_mastro.index(i)
                    index_list.append(i)
                    mastro_count.append(bill_mastro[i])

            mastro_bill_label = [Label(frame, text=mastro_list[index_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for bill_place in mastro_bill_label:
                bill_place.place(relx=0.21,rely=(0.30+samp_title),anchor=CENTER)
                samp_title=samp_title+0.07
            
            mastro_count_label = [Label(frame, text=mastro_count[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(mastro_count))]
            for count_lable in mastro_count_label:
                count_lable.place(relx=0.45,rely=(0.30+samp_count),anchor=CENTER)
                samp_count=samp_count+0.07            
            
            mastro_cost_list = [mastro_dict[mastro_list[index_list[x]]] for x in range(len(index_list))]
            count_cost = [mastro_cost_list[x]*mastro_count[x] for x in range(len(mastro_count))]
            #print(count_cost)
            
            mastro_cost_label = [Label(frame, text=count_cost[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for price_place in mastro_cost_label:
                price_place.place(relx=0.65,rely=(0.30+same_cost),anchor=CENTER)
                same_cost=same_cost+0.07
            for x in range(len(index_list)):
                sleep(0.1)
                date_time = str(datetime.now())
                date_time = date_time.replace(':','-')
                my_cursor.execute("insert into salesData values('{today_date}', '{part}', {cost}, '{count}', 'Hero Motors', 'W2');".format(today_date=date_time,part=mastro_list[index_list[x]],cost=(mastro_dict[mastro_list[index_list[x]]]*mastro_count[x]),count=mastro_count[x]))
            my_cursor.close()
            print('Data added to database')
            #print('mastor non')
    #variables declared to handle re parts only
    global bullet_count
    bullet_count = []
    global thunderBird_count
    thunderBird_count = []
    if list_items=='re_get_list':
        if sum(bill_bullet) !=0:
            for i in range(len(bill_bullet)):
                if bill_bullet[i]>0:
                    #index = bill_bullet.index(i)
                    index_list.append(i)
                    bullet_count.append(bill_bullet[i])                   
            #print(index_list)
            #print(bullet_count)
            bullet_bill_label = [Label(frame, text=bullet_list[index_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for bill_place in bullet_bill_label:
                bill_place.place(relx=0.21,rely=(0.30+samp_title),anchor=CENTER)
                samp_title=samp_title+0.07
            
            bullet_count_label = [Label(frame, text=bullet_count[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(bullet_count))]
            for count_lable in bullet_count_label:
                count_lable.place(relx=0.45,rely=(0.30+samp_count),anchor=CENTER)
                samp_count=samp_count+0.07

            #global count_cost
            bullet_cost_list = [bullet_dict[bullet_list[index_list[x]]] for x in range(len(index_list))]
            count_cost = [bullet_cost_list[x]*bullet_count[x] for x in range(len(bullet_count))]
            #print(count_cost)
            
            bullet_cost_label = [Label(frame, text=count_cost[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for price_place in bullet_cost_label:
                price_place.place(relx=0.65,rely=(0.30+same_cost),anchor=CENTER)
                same_cost=same_cost+0.07
            for x in range(len(index_list)):
                sleep(0.1)
                date_time = str(datetime.now())
                date_time = date_time.replace(':','-')
                my_cursor.execute("insert into salesData values('{today_date}', '{part}', {cost}, '{count}', 'Royal Enfield', 'W2');".format(today_date=date_time,part=bullet_list[index_list[x]],cost=(bullet_dict[bullet_list[index_list[x]]]*bullet_count[x]),count=bullet_count[x]))
            my_cursor.close()
        if sum(bill_thunderBird) !=0:
            for i in range(len(bill_thunderBird)):
                if bill_thunderBird[i]>0:
                    #index = bill_thunderBird.index(i)
                    index_list.append(i)
                    thunderBird_count.append(bill_thunderBird[i])                
            #print(index_list)
            #print(thunderBird_count)
            thunderBird_bill_label = [Label(frame, text=thunderBird_list[index_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for bill_place in thunderBird_bill_label:
                bill_place.place(relx=0.21,rely=(0.30+samp_title),anchor=CENTER)
                samp_title=samp_title+0.07
            
            thunderBird_count_label = [Label(frame, text=thunderBird_count[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(thunderBird_count))]
            for count_lable in thunderBird_count_label:
                count_lable.place(relx=0.45,rely=(0.30+samp_count),anchor=CENTER)
                samp_count=samp_count+0.07            
            
            thunderBird_cost_list = [thunderBird_dict[thunderBird_list[index_list[x]]] for x in range(len(index_list))]
            count_cost = [thunderBird_cost_list[x]*thunderBird_count[x] for x in range(len(thunderBird_count))]
            #print(count_cost)
            
            thunderBird_cost_label = [Label(frame, text=count_cost[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for price_place in thunderBird_cost_label:
                price_place.place(relx=0.65,rely=(0.30+same_cost),anchor=CENTER)
                same_cost=same_cost+0.07
            for x in range(len(index_list)):
                sleep(0.1)
                date_time = str(datetime.now())
                date_time = date_time.replace(':','-')
                my_cursor.execute("insert into salesData values('{today_date}', '{part}', {cost}, '{count}', 'Royal Enfield', 'W2');".format(today_date=date_time,part=thunderBird_list[index_list[x]],cost=(thunderBird_dict[thunderBird_list[index_list[x]]]*thunderBird_count[x]),count=thunderBird_count[x]))
            my_cursor.close()
            print('Data added to database')
    #variables declared to handle yamaha parts only
    global rx100_count
    rx100_count = []
    global fazer_count
    fazer_count = []
    global ray_count
    ray_count = []
    if list_items=='yamaha_get_list':
        if sum(bill_rx100) !=0:
            for i in range(len(bill_rx100)):
                if bill_rx100[i]>0:
                    #index = bill_rx100.index(i)
                    index_list.append(i)
                    rx100_count.append(bill_rx100[i])
                    
            #print(index_list)
            #print(rx100_count)
            rx100_bill_label = [Label(frame, text=rx100_list[index_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for bill_place in rx100_bill_label:
                bill_place.place(relx=0.21,rely=(0.30+samp_title),anchor=CENTER)
                samp_title=samp_title+0.07
            
            rx100_count_label = [Label(frame, text=rx100_count[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(rx100_count))]
            for count_lable in rx100_count_label:
                count_lable.place(relx=0.45,rely=(0.30+samp_count),anchor=CENTER)
                samp_count=samp_count+0.07

            rx100_cost_list = [rx100_dict[rx100_list[index_list[x]]] for x in range(len(index_list))]
            count_cost = [rx100_cost_list[x]*rx100_count[x] for x in range(len(rx100_count))]
            #print(count_cost)
            
            rx100_cost_label = [Label(frame, text=count_cost[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for price_place in rx100_cost_label:
                price_place.place(relx=0.65,rely=(0.30+same_cost),anchor=CENTER)
                same_cost=same_cost+0.07 
            for x in range(len(index_list)):
                sleep(0.1)
                date_time = str(datetime.now())
                date_time = date_time.replace(':','-')
                my_cursor.execute("insert into salesData values('{today_date}', '{part}', {cost}, '{count}', 'Yamaha', 'W2');".format(today_date=date_time,part=rx100_list[index_list[x]],cost=(rx100_dict[rx100_list[index_list[x]]]*rx100_count[x]),count=rx100_count[x]))
            my_cursor.close()
            print('Data added to database')          
        if sum(bill_fazer) !=0:
            for i in range(len(bill_fazer)):
                if bill_fazer[i]>0:
                    #index = bill_fazer.index(i)
                    index_list.append(i)
                    fazer_count.append(bill_fazer[i])

            fazer_bill_label = [Label(frame, text=fazer_list[index_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for bill_place in fazer_bill_label:
                bill_place.place(relx=0.21,rely=(0.30+samp_title),anchor=CENTER)
                samp_title=samp_title+0.07
            
            fazer_count_label = [Label(frame, text=fazer_count[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(fazer_count))]
            for count_lable in fazer_count_label:
                count_lable.place(relx=0.45,rely=(0.30+samp_count),anchor=CENTER)
                samp_count=samp_count+0.07            
            
            fazer_cost_list = [fazer_dict[fazer_list[index_list[x]]] for x in range(len(index_list))]
            count_cost = [fazer_cost_list[x]*fazer_count[x] for x in range(len(fazer_count))]
            #print(count_cost)
            
            fazer_cost_label = [Label(frame, text=count_cost[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for price_place in fazer_cost_label:
                price_place.place(relx=0.65,rely=(0.30+same_cost),anchor=CENTER)
                same_cost=same_cost+0.07
            for x in range(len(index_list)):
                sleep(0.1)
                date_time = str(datetime.now())
                date_time = date_time.replace(':','-')
                my_cursor.execute("insert into salesData values('{today_date}', '{part}', {cost}, '{count}', 'Yamaha', 'W2');".format(today_date=date_time,part=fazer_list[index_list[x]],cost=(fazer_dict[fazer_list[index_list[x]]]*fazer_count[x]),count=fazer_count[x]))
            my_cursor.close()
            print('Data added to database')
        if sum(bill_ray) !=0:
            for i in range(len(bill_ray)):
                if bill_ray[i]>0:
                    #index = bill_ray.index(i)
                    index_list.append(i)
                    ray_count.append(bill_ray[i])
                    
            ray_bill_label = [Label(frame, text=ray_list[index_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for bill_place in ray_bill_label:
                bill_place.place(relx=0.21,rely=(0.30+samp_title),anchor=CENTER)
                samp_title=samp_title+0.07
            
            ray_count_label = [Label(frame, text=ray_count[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(ray_count))]
            for count_lable in ray_count_label:
                count_lable.place(relx=0.45,rely=(0.30+samp_count),anchor=CENTER)
                samp_count=samp_count+0.07            
            
            ray_cost_list = [ray_dict[ray_list[index_list[x]]] for x in range(len(index_list))]
            count_cost = [ray_cost_list[x]*ray_count[x] for x in range(len(ray_count))]
            #print(count_cost)
            
            ray_cost_label = [Label(frame, text=count_cost[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for price_place in ray_cost_label:
                price_place.place(relx=0.65,rely=(0.30+same_cost),anchor=CENTER)
                same_cost=same_cost+0.07
            for x in range(len(index_list)):
                sleep(0.1)
                date_time = str(datetime.now())
                date_time = date_time.replace(':','-')
                my_cursor.execute("insert into salesData values('{today_date}', '{part}', {cost}, '{count}', 'Yamaha', 'W2');".format(today_date=date_time,part=ray_list[index_list[x]],cost=(ray_dict[ray_list[index_list[x]]]*ray_count[x]),count=ray_count[x]))
            my_cursor.close()
            print('data uploaded')
    #variable declared to handle led parts only        
    global led_count
    led_count = []
    if list_items == 'led_get_list':
        if sum(bill_led) !=0:
            for i in range(len(bill_led)):
                if bill_led[i]>0:
                    #index = bill_led.index(i)
                    index_list.append(i)
                    led_count.append(bill_led[i])
            #print(index_list)
            #print(led_count)
            led_bill_label = [Label(frame, text=led_list[index_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for bill_place in led_bill_label:
                bill_place.place(relx=0.21,rely=(0.30+samp_title),anchor=CENTER)
                samp_title=samp_title+0.07
            
            led_count_label = [Label(frame, text=led_count[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(led_count))]
            for count_lable in led_count_label:
                count_lable.place(relx=0.45,rely=(0.30+samp_count),anchor=CENTER)
                samp_count=samp_count+0.07
        
            led_cost_list = [led_dict[led_list[index_list[x]]] for x in range(len(index_list))]
            count_cost = [led_cost_list[x]*led_count[x] for x in range(len(led_count))]
            #print(count_cost)
            
            led_cost_label = [Label(frame, text=count_cost[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for price_place in led_cost_label:
                price_place.place(relx=0.65,rely=(0.30+same_cost),anchor=CENTER)
                same_cost=same_cost+0.07
            for x in range(len(index_list)):
                sleep(0.1)
                date_time = str(datetime.now())
                date_time = date_time.replace(':','-')
                my_cursor.execute("insert into salesData values('{today_date}', '{part}', {cost}, '{count}', 'Led Spares', 'GE');".format(today_date=date_time,part=led_list[index_list[x]],cost=(led_dict[led_list[index_list[x]]]*led_count[x]),count=led_count[x]))
            my_cursor.close() 
            print('data uploaded')
    #varaible declarationto handle engineoil
    global engineOil_count
    engineOil_count = []
    if list_items == 'engineOil_get_list':
        if sum(bill_engineOil) !=0:
            for i in range(len(bill_engineOil)):
                if bill_engineOil[i]>0:
                    #index = bill_engineOil.index(i)
                    index_list.append(i)
                    engineOil_count.append(bill_engineOil[i])
            #print(index_list)
            print(engineOil_count)
            engineOil_bill_label = [Label(frame, text=engineOil_list[index_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for bill_place in engineOil_bill_label:
                bill_place.place(relx=0.21,rely=(0.30+samp_title),anchor=CENTER)
                samp_title=samp_title+0.07
            
            engineOil_count_label = [Label(frame, text=engineOil_count[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(engineOil_count))]
            for count_lable in engineOil_count_label:
                count_lable.place(relx=0.45,rely=(0.30+samp_count),anchor=CENTER)
                samp_count=samp_count+0.07

            engineOil_cost_list = [engineOil_dict[engineOil_list[index_list[x]]] for x in range(len(index_list))]
            count_cost = [engineOil_cost_list[x]*engineOil_count[x] for x in range(len(engineOil_count))]
            
            engineOil_cost_label = [Label(frame, text=count_cost[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for price_place in engineOil_cost_label:
                price_place.place(relx=0.65,rely=(0.30+same_cost),anchor=CENTER)
                same_cost=same_cost+0.07
            for x in range(len(index_list)):
                sleep(0.1)
                date_time = str(datetime.now())
                date_time = date_time.replace(':','-')
                my_cursor.execute("insert into salesData values('{today_date}', '{part}', {cost}, '{count}', 'Engine Oil', 'GE');".format(today_date=date_time,part=engineOil_list[index_list[x]],cost=(engineOil_dict[engineOil_list[index_list[x]]]*engineOil_count[x]),count=engineOil_count[x]))
            my_cursor.close() 
            print('data uploaded')
    #varaible declarationto handle coolant
    global coolant_count
    coolant_count = []
    if list_items == 'coolant_get_list':
        if sum(bill_coolant) !=0:
            for i in range(len(bill_coolant)):
                if bill_coolant[i]>0:
                    #index = bill_coolant.index(i)
                    index_list.append(i)
                    coolant_count.append(bill_coolant[i])

            coolant_bill_label = [Label(frame, text=coolant_list[index_list[x]], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for bill_place in coolant_bill_label:
                bill_place.place(relx=0.21,rely=(0.30+samp_title),anchor=CENTER)
                samp_title=samp_title+0.07
            
            coolant_count_label = [Label(frame, text=coolant_count[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(coolant_count))]
            for count_lable in coolant_count_label:
                count_lable.place(relx=0.45,rely=(0.30+samp_count),anchor=CENTER)
                samp_count=samp_count+0.07

            coolant_cost_list = [coolant_dict[coolant_list[index_list[x]]] for x in range(len(index_list))]
            count_cost = [coolant_cost_list[x]*coolant_count[x] for x in range(len(coolant_count))]

            coolant_cost_label = [Label(frame, text=count_cost[x], fg=fg_default, bg=bg_default, font=font_14) for x in range(len(index_list))]
            for price_place in coolant_cost_label:
                price_place.place(relx=0.65,rely=(0.30+same_cost),anchor=CENTER)
                same_cost=same_cost+0.07
            for x in range(len(index_list)):
                sleep(0.1)
                date_time = str(datetime.now())
                date_time = date_time.replace(':','-')
                my_cursor.execute("insert into salesData values('{today_date}', '{part}', {cost}, '{count}', 'Coolant', 'GE');".format(today_date=date_time,part=coolant_list[index_list[x]],cost=(coolant_dict[coolant_list[index_list[x]]]*coolant_count[x]),count=coolant_count[x]))
            my_cursor.close() 
            print('data uploaded')
  
    #Other labels inthe bill page to print taxt and total
    item_columns_index = Label(frame, text='Item',font=font_16_bold,fg=fg_default,bg=bg_default)
    item_columns_index.place(relx=0.21,rely=0.23,anchor=CENTER)
    count_column_index = Label(frame, text='Count',font=font_16_bold,fg=fg_default,bg=bg_default)
    count_column_index.place(relx=0.45,rely=0.23,anchor=CENTER)
    cost_column_index = Label(frame, text='Price',font=font_16_bold,fg=fg_default,bg=bg_default)
    cost_column_index.place(relx=0.65,rely=0.23,anchor=CENTER)
    net= sum(count_cost)
    net_label = Label(frame,text='Net Price: ',font=font_16,fg=fg_default,bg=bg_default)
    net_label.place(relx=0.4,rely=0.85,anchor=CENTER)
    net_cost = Label(frame,text=net,fg=fg_default,bg=bg_default,font=font_16)
    net_cost.place(relx=0.65,rely=0.85,anchor=CENTER)
    gst = int((12/100)*net)
    gst_label = Label(frame,text='Taxes(GST): ',font=font_16,fg=fg_default,bg=bg_default)
    gst_label.place(relx=0.4,rely=0.91,anchor=CENTER)
    gst_cost = Label(frame,text=gst,fg=fg_default,bg=bg_default,font=font_16)
    gst_cost.place(relx=0.65,rely=0.91,anchor=CENTER)
    total = gst+net #Total CAlcualtion
    total_label = Label(frame,text='Total Cost(in Rupee): ',font=font_16,fg=fg_default,bg=bg_default)
    total_label.place(relx=0.4,rely=0.965,anchor=CENTER)
    total_cost = Label(frame,text=total,fg=fg_default,bg=bg_default,font=font_16)
    total_cost.place(relx=0.65,rely=0.965,anchor=CENTER)

    database.commit()
    print_bill = Button(frame,text='Confirm',font=font_14,bg='#FFD700',fg='purple',activebackground='#d4af27',activeforeground='purple',command=lambda:printBill(frame))
    print_bill.place(relx=0.9,rely=0.22,anchor=CENTER)
    
#Function to check stock in the backend up notify admin
def stock_check():
    if 0 in achiver_stock:
        messagebox.showinfo('Low Stock Alert','Achiver Parts LOW STOCK!')
    if 0 in splendor_stock:
        messagebox.showinfo('Low Stock Alert','Splendor Parts LOW STOCK!')
    if 0 in mastro_stock:
        messagebox.showinfo('Low Stock Alert','Mastro Parts LOW STOCK!')
    if 0 in bullet_stock:
        messagebox.showinfo('Low Stock Alert','Bullet Parts LOW STOCK!')
    if 0 in thunderBird_stock:
        messagebox.showinfo('Low Stock Alert','Thunder Bird Parts LOW STOCK!')
    if 0 in rx100_stock:
        messagebox.showinfo('Low Stock Alert','RX100 Parts LOW STOCK!')
    if 0 in fazer_stock:
        messagebox.showinfo('Low Stock Alert','Fazer Parts LOW STOCK!')
    if 0 in ray_stock:
        messagebox.showinfo('Low Stock Alert','Ray Parts LOW STOCK!')
    
#Home Screen open with main program
def home_page(use,passing):
    user_val = use
    passwd_val = passing
    if user_val=='admin' and passwd_val=='12345':
        clear_frame()
        try:
            back_button.destroy()
        except:
            print('')
        stock_check()
        back_button= Button(root,text='⌂Home',font=font_9,fg='white',bg='red', command=lambda:home_page('admin','12345'))
        back_button.place(relx=0,rely=0)
        root.geometry("480x240")
        root.resizable(0,0)
        title_label = Label(frame, text='Spare Parts Manager',font=heading_font,fg=fg_default,bg=bg_default)
        title_label.place(relx=0.5,rely=0.15,anchor=CENTER)    
        
        heading_label = Label(frame, text='Select Vechile Type',font=font_14, fg=fg_default,bg=bg_default)
        heading_label.place(relx=0.5,rely=0.35,anchor=CENTER)

        vechile_label = Label(frame,text='Select Vechile',font=('arial',12),bg=bg_default,fg=fg_default)
        vechile_label.place(relx=0.3,rely=0.55,anchor=CENTER)
        global vechile_comb
        vechile_comb = ttk.Combobox(frame,state = 'readonly', values=vechile_type,font=('arial'),width=12)
        vechile_comb.current(0)
        vechile_comb.place(relx=0.6,rely=0.55,anchor=CENTER)

        update_button = Button(frame, text='Update Stock/\nAnalytics', font=font_12, fg='white',bg='#002948',command=update_stock_brand_select)
        update_button.place(relx=0.2,rely=0.85,anchor=CENTER)

        set_button = Button(frame, text='Set Vechile',font=font_14, fg='red',bg='yellow',command=brands,height=1)
        set_button.place(relx=0.5,rely=0.85,anchor=CENTER)

        deco_button = Button(frame, text='LED/Decos',font=font_12, fg='white',bg='#002948',command=deco,height =1)
        deco_button.place(relx=0.8,rely=0.85,anchor=CENTER)
        #print(user_val, passwd_val)
    else:
        messagebox.showerror('Error','Wrong User Id or Password')
        login()
    
#Login page
def login():
    clear_frame()
    root.geometry("480x320")
    root.resizable(0,0)
    title_label = Label(frame, text='Spare Parts Manager',font=heading_font,fg=fg_default,bg=bg_default)
    title_label.place(relx=0.5,rely=0.15,anchor=CENTER)    
    global user_entry,passwd_entry
    heading_label = Label(frame, text='Login to Continue',font=font_14, fg=fg_default,bg=bg_default)
    heading_label.place(relx=0.5,rely=0.30,anchor=CENTER)
    user_lable = Label(frame,text='User: ',font=font_14,fg=fg_default,bg=bg_default)
    user_lable.place(relx=0.25,rely=0.45,anchor=CENTER)
    user_entry = Entry(frame,font=enter_font)
    user_entry.place(relx=0.6,rely=0.45,anchor=CENTER)
    passwd_lable = Label(frame,text='Password: ',font=font_14,fg=fg_default,bg=bg_default)
    passwd_lable.place(relx=0.25,rely=0.60,anchor=CENTER)
    passwd_entry = Entry(frame,font=enter_font,show='*')
    passwd_entry.place(relx=0.6,rely=0.60,anchor=CENTER)
    login_button = Button(frame,text='Login',font=font_14,fg='red',bg='yellow',command=lambda: home_page(user_entry.get(),passwd_entry.get()))
    login_button.place(relx=0.5,rely=0.8,anchor=CENTER)
    label_dummy = Label(frame,text='hh',fg=bg_default,bg=bg_default)
    label_dummy.pack(side =LEFT,anchor=NW,expand=YES)
    #Connect to Database get stock list from the server
    database = mysql.connector.connect(
            host='localhost',
            user=user_name,
            password=passwd,
            database='SparePartsManager',
            auth_plugin='mysql_native_password',
            port=3306
        )
    my_cursor = database.cursor()
    achiver_stock.clear()
    splendor_stock.clear()
    mastro_stock.clear()
    bullet_stock.clear()
    thunderBird_stock.clear()
    rx100_stock.clear()
    fazer_stock.clear()
    ray_stock.clear()
    #get stock and update to the respected stock lists
    for i in range(len(model_list)):
        my_cursor.execute('select Stock from {}'.format(model_list[i]))
        for x in my_cursor:
            if i==0:
                achiver_stock.append(x[0])
            elif i==1:
                splendor_stock.append(x[0])
            elif i==2:
                mastro_stock.append(x[0])
            elif i==3:
                bullet_stock.append(x[0])
            elif i==4:
                thunderBird_stock.append(x[0])
            elif i==5:
                rx100_stock.append(x[0])
            elif i==6:
                fazer_stock.append(x[0])
            elif i==7:
                ray_stock.append(x[0])

#---------------------------------#---------------------------------##---------------------------------#---------------------------------#
version_label = Label(root,text='v1.2.4',font=('arial',9),bg=bg_default,fg='white')
version_label.pack(side=RIGHT,anchor=SE)
#Main Program to initiate the login page!
if __name__ == '__main__':
    login()
    root.mainloop() #root page mainloop to keep the window open
