
from tkinter import *
from tkinter import Tk,ttk,messagebox
import tkinter
from PIL import Image,ImageTk
from numpy import double

#colors
color1="white"
color2="black"
color3="red"

root=Tk()
root.geometry('300x320')
root.title('Converter')
root.configure(bg=color1)
root.resizable(height=FALSE,width=FALSE)


#frames
top=Frame(root,width=300,height=60,bg="#A2CD5A")
top.grid(row=0,column=0)

main=Frame(root,width=300,height=260,bg="white")
main.grid(row=1,column=0) 

#top_frame
icon=Image.open('images/logo1.png')
icon=icon.resize((40,40))
icon=ImageTk.PhotoImage(icon)
app_name=Label(top,image=icon,compound=LEFT,text="Currency Converter",height=3,padx=13,pady=30,anchor=CENTER,font=('Arial 16 bold'),bg="#A2CD5A",fg="black")
app_name.place(x=0,y=0)



#main frame
result=Label(main,relief="solid",width=16,height=2,pady=7,anchor=CENTER,font=('Ivy 15 bold'),bg="white",fg="black")
result.place(x=50,y=20)


from_label=Label(main,text="From",width=10,height=1,padx=0,pady=0,anchor=NW,font=('Ivy 12 bold'),bg="white",fg="black")
from_label.place(x=47,y=100)


to_label=Label(main,text="To",width=10,height=1,padx=0,pady=0,anchor=NW,font=('Ivy 12 bold'),bg="white",fg="black")
to_label.place(x=165,y=100)



currency=['CAD','BRL','EUR','INR','USD']


combo1=ttk.Combobox(main,width=10,justify=CENTER,font=("Ivy 10 "))
combo1['value']=(currency)
combo1.place(x=50,y=125)



combo2=ttk.Combobox(main,width=10,justify=CENTER,font=("Ivy 10 "))
combo2['value']=(currency)
combo2.place(x=160,y=125)

value=Entry(main,width=22,justify=CENTER,relief="solid",font=("Ivy 12 bold"),text="Enter amount")
value.place(x=50,y=165)


def convert_button():
    currency1=combo1.get()
    currency2=combo2.get()
    if currency1==currency2:
        messagebox.showinfo("Error","Same currencies")
    amount=value.get()
    if amount.isdigit():
        amount=int(amount)
    else:
        messagebox.showinfo("Error","Enter only numerical value.")
    if currency1=="CAD" and currency2=="INR":
       result1 = round((amount*61.37),2)
       result.config(text=result1)
    if currency1=="CAD" and currency2=="BRL":
       result1 = round((amount*4.05),2)
       result.config(text=result1)
    if currency1=="CAD" and currency2=="EUR":
       result1 = round((amount*0.74),2)
       result.config(text=result1)
    if currency1=="CAD" and currency2=="USD":
       result1 = round((amount*0.78),2)
       result.config(text=result1)
    

    if currency1=="INR" and currency2=="CAD":
       result1 = round((amount*0.016),2)
       result.config(text=result1)
    if currency1=="INR" and currency2=="USD":
       result1 = round((amount*0.013),2)
       result.config(text=result1)
    if currency1=="INR" and currency2=="EUR":
       result1 = round((amount*0.012),2)
       result.config(text=result1)
    if currency1=="INR" and currency2=="BRL":
       result1 = round((amount*0.066),2)
       result.config(text=result1)

    
    if currency1=="BRL" and currency2=="CAD":
       result1 = round((amount*0.25),2)
       result.config(text=result1)
    if currency1=="BRL" and currency2=="USD":
       result1 = round((amount*0.19),2)
       result.config(text=result1)
    if currency1=="BRL" and currency2=="INR":
       result1 = round((amount*15.11),2)
       result.config(text=result1)
    if currency1=="BRL" and currency2=="EUR":
       result1 = round((amount*0.18),2)
       result.config(text=result1)
    
    
    if currency1=="EUR" and currency2=="INR":
       result1 = round((amount*82.75),2)
       result.config(text=result1)
    if currency1=="EUR" and currency2=="CAD":
       result1 = round((amount*1.35),2)
       result.config(text=result1)
    if currency1=="EUR" and currency2=="USD":
       result1 = round((amount*1.05),2)
       result.config(text=result1)
    if currency1=="EUR" and currency2=="BRL":
       result1 = round((amount*5.48),2)
       result.config(text=result1)
    
    
    if currency1=="USD" and currency2=="INR":
       result1 = round((amount*78.96),2)
       result.config(text=result1)
    if currency1=="USD" and currency2=="EUR":
       result1 = round((amount*0.95),2)
       result.config(text=result1)
    if currency1=="USD" and currency2=="BRL":
       result1 = round((amount*5.23),2)
       result.config(text=result1)
    if currency1=="USD" and currency2=="CAD":
       result1 = round((amount*1.29),2)
       result.config(text=result1)



button=Button(main,text="Convert",width=19,height=1,bg="#A2CD5A",fg="black",font=("Ivy 12 bold"),command=convert_button)
button.place(x=52,y=200)



root.mainloop()

