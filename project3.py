from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("1366x768")
def show_bus():
    Label(root,text="select bus ",fg="green",font=("Aerial 12 bold")).grid(row=6,column=1)
    Label(root,text="Operator",fg="green",font=("Aerial 12 bold")).grid(row=6,column=2)
    Label(root,text="Bus Type",fg="green",font=("Aerial 12 bold")).grid(row=6,column=3,padx=50)
    Label(root,text="Availability",fg="green",font=("Aerial 12 bold")).grid(row=6,column=4)
    Label(root,text="Fare",fg="green",font=("Aerial 12 bold")).grid(row=6,column=5)
def on_click():
   messagebox.showerror('Error', 'Error: Please complete the entry!')

Label(root,text="  ").grid(row=0,column=0,padx=150)
label1=Label(root,text="Online Bus Booking System",font=("Aerial 30 bold"),fg="red",bg="sky blue")
pic=PhotoImage(file='C:\\Users\\DEBANJAN SINGHA ROY\\OneDrive\\Desktop\\Bus Reservation System\\Bus_for_Project.png')
Label(root,image=pic).grid(row=0,column=1,columnspan=6)
label1.grid(row=1,column=1,pady=30,columnspan=6)
Label(root,text="Enter Journey Details",font=("Aerial 15 bold"),fg= "Green",bg="light Green").grid(row=3,column=1,columnspan=6,pady=10)
Label(root,text="TO",font=("Aerial 15 bold")).grid(row=5,column=1)
v=Entry(root,width=20).grid(row=5,column=2)
Label(root,text="FROM",font=("Aerial 15 bold")).grid(row=5,column=3)
Entry(root,width=20,).grid(row=5,column=4)
Label(root,text="Journey Date",font=("Aerial 15 bold")).grid(row=5,column=5)
Entry(root,width=20).grid(row=5,column=6)
Button(root,text="Show bus",font=(" Aerial 15 bold"),bg="green").grid(row=5,column=7)
pic1=PhotoImage(file=".\\home.png")
Button(root,image=pic1).grid(row=5,column=8,padx=10)
def passeng():
    Label(root,text="Fill Passenger Details to book ticket",font=("Aerial 15 bold"),fg="red",bg="sky blue").grid(row=10,column=2,columnspan=8) 
Button(root,text="Proceed To Book",font=("Aerial 12 bold"),bg="green",command=passeng).grid(row=8,column=8,pady=20)
root.mainloop()
