# import Tkinter and make interface of size(300x180)
import tkinter as tk
from tkinter import * 
root = tk.Tk()
root.geometry("300x180")
root.configure(bg='#856ff8')

item_name=tk.StringVar()
item_price=tk.IntVar()
item_quant=tk.IntVar()

# add() method is use for operatimg add button
def add():
    global name 
    global price
    global quant
    global sum
    name=item_name.get()
    price=item_price.get()
    quant=item_quant.get()
    print("Item : " + name)
    print("Price:" ,price)
    print("Quant:",quant)
    sum=quant*price
    print("Total=" ,sum)
    
    item_name.set("")
    item_price.set("") 
    item_quant.set("") 
    
# reciept() method is use for operation of reciept button to show the reciept    
def reciept():
    top=Toplevel()
    top.geometry("300x180")
    
    top.config(background='white')
    item1=name
    price1=price
    quant1=quant
    total=sum
   
    # Creating Heading,Labels on reciept screen
    
    l=Label(top,text='----------RECIEPT---------')
    l.pack()
    l.config(background='white')
    
    
    heading=Label(top,text='ITEM\tPRICE\tQUANTITY\t\tTOTAL')
    heading.pack()
    heading.config(background='red')

    item1=Label(top,text=f'{item1}\t{price1}\t{quant1}\t\t\t{total}')
    item1.pack()
    item1.config(background='white')
    
    total1=Label(top,text='TOTAL PAYABLE').place(x=155,y=155)
    total1=Label(top,text=f'{total}').place(x=255,y=155)
    total1.pack()
    total1.config(background='white')

# Creating Heading,Labels,Entrybox,Buttons on main(root) screen    

lblcompany=Label(root, text='STATIONARY',bg='orange', font=('Helvetica', 18, 'bold'), width = 20,justify= 'center').place(x=0, y=2) 
Item=Label(root,text='ITEM NAME',bg='#856ff8').place(x=10, y=45)
price=Label(root,text='PRICE',bg='#856ff8').place(x=10, y=70)
quant=Label(root,text='QUANTITY',bg='#856ff8').place(x=10, y=95)


entry1= Entry(root, textvariable = item_name).place(x=120, y=45)   
entry2 = Entry(root, textvariable = item_price).place(x=120, y=70) 
entry3 = Entry(root, textvariable = item_quant).place(x=120, y=95)

b=Button(root,text='Print Reciept',command=reciept,bg='red').place(x=120, y=135) 
a=Button(root,text='Add',bg='yellow',command=add).place(x=210, y=135) 




root.mainloop()    
    
