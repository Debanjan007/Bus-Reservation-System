from tkinter import*
import tkinter as tk
root=tk.Tk()
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.title("Bus Reservation System")
bus=PhotoImage(file='C:\\Users\\DEBANJAN SINGHA ROY\\OneDrive\\Desktop\\Bus Reservation System\\Bus_for_Project.png')
Label(root, image=bus).grid(row=0,column=0,columnspan=8,padx=width//2.5)
Label(root,text='Online Bus Booking System',bg='lightblue',fg='red',font='Arial 18 bold').grid(row=1,column=0,columnspan=8,padx=width//2.5)
Label(root,text='Name: Debanjan Singha Roy',fg='black',font='Arial 18 bold').grid(row=2,column=0,columnspan=8,padx=width//2.5,pady=height//10)
Label(root,text='Enrollment Number = 211B406',fg='black',font='Arial 18 bold').grid(row=3,column=0,columnspan=8,padx=width//2.5,pady=height//20)
Label(root,text='Mobile : 9475240460',fg='black',font='Arial 18 bold').grid(row=4,column=0,columnspan=8,padx=width//2.5,pady=height//20)
Label(root,text='Submitted To : Dr Mahesh Kumar',bg='lightblue',fg='red',font='Arial 18 bold').grid(row=5,column=0,columnspan=8,padx=width//2.5)
root.mainloop()
