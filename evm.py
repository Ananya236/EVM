from tkinter import *
from tkinter import messagebox
#from PIL import ImageTk, Image

v1=0;v2=0;v3=0;

root=Tk()
root.geometry('1200x800')
root.title('ATM')
r=Frame(root)
r.grid(row=0,column=0,sticky='news')

def p1():
    global v1
    v1+=1
def p2():
    global v2
    v2+=1
def p3():
    global v3
    v3+=1

def res():
    tot=v1+v2+v3
    if(tot==0):
        return
    p1=(v1/tot)*100
    p2=(v2/tot)*100
    p3=(v3/tot)*100
    #win=(p1>p2)?(p1>p3?"Party 1":"Party 3"):(p2>p3?"Party 2":"Party 3")
    if(p1>p2):
        if(p1>p3):
            win="Party 1"
        else:
            win="Party 3"
    else:
        if(p2>p3):
            win="Party 2"
        else:
            win="Party 3"
    Label(r,text=str(p1)+"%",font=('Chiller 40')).grid(row=4,column=4)  
    Label(r,text=str(p2)+"%",font=('Chiller 40')).grid(row=6,column=4)  
    Label(r,text=str(p3)+"%",font=('Chiller 40')).grid(row=8,column=4)  
    Label(r,text=win+" is winner!!",font=('Chiller 40')).grid(row=11,column=2)      

Label(r,text='EVM',font=('Aerial 70 bold')).grid(row=0,column=0)
Label(r,text='').grid(row=1,column=0)
Label(r,text='').grid(row=2,column=0)
Label(r,text='').grid(row=3,column=0)
Label(r,text='Party 1',font=('Chiller 40')).grid(row=4,column=0)
Label(r,text='').grid(row=4,column=1)
Button(r,text='VOTE',command=p1).grid(row=4,column=2)
Label(r,text='').grid(row=4,column=3)
Label(r,text='').grid(row=5,column=0)
Label(r,text='Party 2',font=('Chiller 40')).grid(row=6,column=0)
Label(r,text='').grid(row=6,column=1)
Button(r,text='Vote',command=p2).grid(row=6,column=2)
Label(r,text='').grid(row=6,column=3)
Label(r,text='').grid(row=7,column=0)
Label(r,text='Party 3',font=('Chiller 40')).grid(row=8,column=0)
Label(r,text='').grid(row=8,column=1)
Button(r,text='Vote',command=p3).grid(row=8,column=2)
Label(r,text='').grid(row=8,column=3)
Label(r,text='').grid(row=9,column=0)
Label(r,text='').grid(row=10,column=0)
Button(r,text='Result',command=res).grid(row=11,column=0)
Label(r,text='').grid(row=6,column=1)

