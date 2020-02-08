from tkinter import *
from tkinter import messagebox
def clear():
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    var.set(NONE)
    checkbutton_1.deselect()
    checkbutton_2.deselect()
    checkbutton_3.deselect()
    spin_1.delete(0, END)
def submit():
    dict_1={}
    x1=entry_1.get()
    dict_1['Name']=x1
    x1=entry_2.get()
    dict_1['Email']=x1
    x1=var.get()
    if x1==1:
        dict_1['Gender']='male'
    elif x1==2:
        dict_1['Gender']='female'

    x1=var1.get()
    x2=var2.get()
    x3=var3.get()
    if x1==1 and x2==0 and x3==0:
        dict_1['Hobbies']='Football'
    elif x1==0 and x2==1 and x3==0:
        dict_1['Hobbies']='Cricket'        
    elif x1==0 and x2==0 and x3==1:
        dict_1['Hobbies']='Other'     
    elif x1==1 and x2==1 and x3==0:
        dict_1['Hobbies']='Football Cricket'   
    elif x1==0 and x2==1 and x3==1:
        dict_1['Hobbies']='Cricket and Other' 
    elif x1==1 and x2==0 and x3==1:
        dict_1['Hobbies']='Football and Other' 
    elif x1==1 and x2==1 and x3==1:
        dict_1['Hobbies']='Football Cricket and Other'      
    elif x1==0 and x2==0 and x3==0:
        dict_1['Hobbies']='NONE' 

    x1=spin_1.get()
    if x1 =='':
        dict_1['Age']='None'
    else :
        dict_1['Age']=x1
    messagebox.showinfo("Response",dict_1)

root = Tk()
root.geometry('500x500')
#root.configure(bg='black')
label_1=Label(root,text='Biodata Form',font=('bold',25),width=20)
label_1.place(x=60,y=50)
label_2=Label(root,text='Name',font=('bold',10),width=20)
label_2.place(x=80,y=120)
entry_1=Entry(root,relief=RAISED)
entry_1.place(x=250,y=120)
label_3=Label(root,text='Email',font=('bold',10),width=20)
label_3.place(x=80,y=170)
entry_2=Entry(root,relief=RAISED)
entry_2.place(x=250,y=170)
label_4=Label(root,text='Gender',font=('bold',10),width=20)
label_4.place(x=80,y=220)
var=IntVar()
radio_1=Radiobutton(root,text='Male',variable=var,value=1)
radio_1.place(x=250,y=220)
radio_2=Radiobutton(root,text='Female',variable=var,value=2)
radio_2.place(x=320,y=220)

label_5=Label(root,text='Hobbies',font=('bold',10),width=20)
label_5.place(x=80,y=270)
var1=IntVar()
checkbutton_1=Checkbutton(root,text='Football',variable=var1)
checkbutton_1.place(x=250,y=270)
var2=IntVar()
checkbutton_2=Checkbutton(root,text='Cricket',variable=var2)
checkbutton_2.place(x=320,y=270)
var3=IntVar()
checkbutton_3=Checkbutton(root,text='Other',variable=var3)
checkbutton_3.place(x=390,y=270)
label_6=Label(root,text='Age',font=('bold',10),width=20)
label_6.place(x=80,y=320)
spin_1=Spinbox(root,from_=0,to=100)
spin_1.place(x=250,y=320)
button_1=Button(root,text='Submit',bg='Brown',width=20,fg='white',command=submit)
button_1.place(x=70,y=410)
button_2=Button(root,text='Clear',bg='Brown',width=20,fg='white',command=clear)
button_2.place(x=280,y=410)
root.mainloop()