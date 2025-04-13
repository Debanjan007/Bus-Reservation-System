from tkinter import*
import tkinter as tk
root=tk.Tk()
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.title("Bus Reservation System")
bus=PhotoImage(file='C:\\Users\\DEBANJAN SINGHA ROY\\OneDrive\\Desktop\\Bus Reservation System\\Bus_for_Project.png')
Label(root, image=bus).grid(row=0,column=0,columnspan=5,padx=width//2.5)
Label(root,text='Online Bus Booking System',bg='lightblue',fg='red',font='Arial 18 bold').grid(row=1,column=0,columnspan=5,padx=width//2.5)
b=Button(root,text='Seat Booking',height=2,width=15,bg='green',font='Arial 18 bold').grid(row=4,column=1,pady=height//10)
c=Button(root,text='Check Booked Details',height=2,width=20,bg='green',font='Arial 18 bold').grid(row=4,column=2,pady=height//10)
d=Button(root,text='Add Bus Details',height=2,width=15,bg='green',font='Arial 18 bold').grid(row=4,column=3,pady=height//10)
Label(root,text='ADMIN ONLY',fg='red',font='Arial 10 bold').grid(row=5,column=3,pady=height//25)
