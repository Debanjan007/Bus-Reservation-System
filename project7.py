from tkinter import *
root=Tk()
root.geometry("1366x768")
menu= StringVar()
menu.set("Select Any Language")
Label(root,text="  ").grid(row=0,column=0,padx=100)
label1=Label(root,text="Online Bus Booking System",font=("Aerial 30 bold"),fg="red",bg="sky blue")
pic=PhotoImage(file='C:\\Users\\DEBANJAN SINGHA ROY\\OneDrive\\Desktop\\Bus Reservation System\\Bus_for_Project.png')
Label(root,image=pic).grid(row=0,column=1,columnspan=12)
label1.grid(row=1,column=1,pady=15,columnspan=12)
Label(root,text="ADD BUS DETAILS",font=("Aerial 20 bold"),fg="green",bg="white").grid(row=2,column=1,pady=15,columnspan=12)
Label(root,text="Bus Type",font=("Aerial 15")).grid(row=4,column=1,padx=5)
Entry(root,width=5).grid(row=4,column=2)
Label(root,text="Bus id",font=("Aerial 15")).grid(row=4,column=3)
OptionMenu(root,menu,"AC 2X2","AC 3X2","Non AC 2X2","Non AC 3X2","AC-Sleeper2x1","Non-AC Sleeper 2x1").grid(row=4,column=4)
Label(root,text="Capacity",font=("Aerial 15")).grid(row=4,column=5)
Entry(root).grid(row=4,column=6)
Label(root,text="Fare Rs",font=("Aerial 15")).grid(row=4,column=7)
Entry(root).grid(row=4,column=8)
Label(root,text="Operator Id",font=("Aerial 15")).grid(row=4,column=9)
Entry(root,width=10).grid(row=4,column=10)
Label(root,text="Route id",font=("Aerial 15")).grid(row=4,column=11)
Entry(root,width=5).grid(row=4,column=12)
Button(root,text="Add Bus",bg="green",font=("Aerial 12")).grid(row=10,column=6,pady=70)
Button(root,text="Edit Bus",bg="green",font=("Aerial 12")).grid(row=10,column=7,padx=5,pady=70)
pic1=PhotoImage(file=".\\home.png")
Button(root,image=pic1).grid(row=10,column=8,padx=10)
root.mainloop()
