import time  #allows time operations
import winsound
from tkinter import *
import math


hr=0 #global variables
m=0
flag=0
mins=None
hou=None

root = Tk()   #main window
root.geometry("1400x900")

var =IntVar()   ## variable 'var' to get alarm time for hours
var.set(0)
vl=Label(root, textvariable=var,font= ("roboto bold", 15 ,"normal"))
vl.place( x=885,y=500)

var2 =IntVar() ## variable 'var2' to get alarm time for minutes
var2.set(0)
v2=Label(root, textvariable=var2,font= ("roboto bold", 15 ,"normal"))
v2.place( x=885,y=550)


def tick():      ## tick()  function to count seconds and beep when alarm time matches real time
    time_keeper = time.strftime("%H:%M:%S")
    clock.config(text = time_keeper)  #configures time continouslly
    clock.after(1000,tick)   #allows clock to work continouslly calling tick function after 1000 millisecond i.e.1 second
    global hr,var,var2,m,flag,mins,hou
    hr=int(time.strftime("%H"))
    m=int(time.strftime("%M"))
    mins=var2.get()
    hou=var.get()
    if(hr==var.get() and m==var2.get() and flag==1):
             winsound.Beep(1000,1000)
             winsound.Beep(1000,1000)
             flag=0

         
        

photo = PhotoImage(file="images.png",)             
clock = Label(root, font= ("roboto bold", 150 ,"normal"), bg="#efefef")
clock2 = Label(root, image=photo)
clock2.place(x=40,y=90)
clock.place(x=550,y=100)  #positions element in a grid

def set_time():    ##Function to  set alarm time 
    global flag,hou,mins
    flag=1
    time=Label( root,text="Alarm Time",font= ("roboto bold", 45 ,"normal"))
    time.place( x=750,y=350)
    hrs = Label( root,text="Hours:",font= ("roboto bold", 15 ,"normal"))
    hrs.place( x=810,y=420)
    mn = Label( root,text="Min:",font= ("roboto bold", 15 ,"normal"))
    mn.place( x=900,y=420)
    hou=var.get()
    mins=var2.get()
    atl = Label(root,text=hou,font= ("roboto bold", 15 ,"normal"))
    atl.place( x=870,y=420)
    at2 = Label(root,text=mins,font= ("roboto bold", 15 ,"normal"))
    at2.place( x=940,y=420)



 
def add_timer(): ##Funtion of + button for hours
      global var
      if(var.get()<24):
       x=var.get()+1
      if(var.get()==24):
       x=0 
      var.set(x)
      
def sub_timer(): ##Funtion of - button for hours
      global var
      if(var.get()>0):
       x=var.get()-1
      if(var.get()==0):
       x=24   
      var.set(x)

def add_timerm(): ##Funtion of + button for minutes
      global var2
      if(var2.get()<59):
       i=var2.get()+1
      if(var.get()==59):
       i=0  
      var2.set(i)
      
      
def sub_timerm(): ##Funtion of - button for minutse
      global var2
      if(var2.get()>0):
       i=var2.get()-1
      if(var2.get()==0):
       i=59 
      var2.set(i)
      
#for hours       ##UI for setting hours
buttonp=Button(text="+",width=5,command= add_timer)
buttonp.place( x=920,y=500)

buttonm=Button(text="-",width=5,command= sub_timer)
buttonm.place( x=835,y=500)

hours = Label( root,text="Hours:",font= ("roboto bold", 15 ,"normal"))
hours.place( x=770,y=500)


#for minutes       ##UI for setting minutes
buttonp2=Button(text="+",width=5,command= add_timerm)
buttonp2.place( x=920,y=550)

buttonm2=Button(text="-",width=5,command= sub_timerm)
buttonm2.place( x=835,y=550)

minute= Label( root,text="Min:",font= ("roboto bold", 15 ,"normal"))
minute.place( x=770,y=550)


   
##Button to set alarm time
setbutton=Button(text="Set",width=7,command= set_time)
setbutton.place( x=865,y=600)


tick()        

root.mainloop()  #executes infinite loop untill main window is not closed
