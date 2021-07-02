from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END) #delete existing entries in listbox
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(TOOL_NAME_text.get(),Manufacturer_text.get(),Quantity_integer.get(),Supplier_Name_text.get()):
            list1.insert(END,row)

def add_command():
    backend.insert(80,TOOL_NAME_text.get(),Manufacturer_text.get(),Quantity_integer.get(),Supplier_Name_text.get())
    list1.delete(0,END)
    list1.insert(END,(TOOL_NAME_text.get(),Manufacturer_text.get(),Quantity_integer.get(),Supplier_Name_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(TOOL_NAME_text.get(),Manufacturer_text.get(),Quantity_integer.get(),Supplier_Name_text.get())

def clear_text():
    e1.delete(first=0,last=100)
    e2.delete(first=0,last=100)
    e3.delete(first=0,last=100)
    e4.delete(first=0,last=100)
    e5.delete(first=0,last=100)

window=Tk()

window.wm_title("Manufacturing Tools Management By Sourabh Antarkar")
window.configure(bg="Black")
l1=Label(window,text="TOOL_NAME",bg="Black",fg="white", font = ('Comic Sans MS',16))
l1.grid(row=0,column=0)

l2=Label(window,text="Manufacturer",bg="Black",fg="white",font = ('Comic Sans MS',16))
l2.grid(row=0,column=2)

l3=Label(window,text="Quantity",bg="Black",fg="white",font = ('Comic Sans MS',16))
l3.grid(row=1,column=0)

l4=Label(window,text="Supplier Name",bg="Black",fg="white",font = ('Comic Sans MS',16))
l4.grid(row=1,column=2)

l5=Label(window,text="Date of Purchase",bg="Black",fg="white",font = ('Comic Sans MS',16))
l5.grid(row=0,column=4)

TOOL_NAME_text=StringVar()
e1=Entry(window,textvariable=TOOL_NAME_text,bg="Black",fg="Grey",font = ('Comic Sans MS',16))
e1.grid(row=0,column=1)

Manufacturer_text=StringVar()
e2=Entry(window,textvariable=Manufacturer_text,bg="Black",fg="Grey",font = ('Comic Sans MS',16))
e2.grid(row=0,column=3)

Quantity_integer=StringVar()
e3=Entry(window,textvariable=Quantity_integer,bg="Black",fg="Grey",font = ('Comic Sans MS',16))
e3.grid(row=1,column=1)

Supplier_Name_text=StringVar()
e4=Entry(window,textvariable=Supplier_Name_text,bg="Black",fg="Grey",font = ('Comic Sans MS',16))
e4.grid(row=1,column=3)

date_text=StringVar()
e5=Entry(window,textvariable=date_text,bg="Black",fg="Grey",font = ('Comic Sans MS',16))
e5.grid(row=0,column=5)

list1=Listbox(window, height=20,width=90,bg="black",fg="Grey",highlightcolor="Red",selectbackground="Purple",font = ('Comic Sans MS',16))
list1.grid(row=2,column=0,rowspan=16,columnspan=10)

sb1=Scrollbar(window)
sb1.grid(row=2,column=16,rowspan=4)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=12,command=view_command,bg="Black",fg="white",font = ('Comic Sans MS',16))
b1.grid(row=2,column=15)

b2=Button(window,text="Search entry", width=12,command=search_command,bg="Black",fg="white",font = ('Comic Sans MS',16))
b2.grid(row=4,column=15)

b3=Button(window,text="Add entry", width=12,command=add_command,bg="Black",fg="white",font = ('Comic Sans MS',16))
b3.grid(row=6,column=15)

b4=Button(window,text="Update selected", width=12,command=update_command,bg="Black",fg="white",font = ('Comic Sans MS',16))
b4.grid(row=8,column=15)

b5=Button(window,text="Delete selected", width=12,command=delete_command,bg="Black",fg="white",font = ('Comic Sans MS',16))
b5.grid(row=10,column=15)

b6=Button(window,text="Clear Text", width=12,command=clear_text, bg="black",fg="white",font = ('Comic Sans MS',16))
b6.grid(row=12,column=15)

b7=Button(window,text="Close", width=12,command=window.destroy,bg="Black",fg="white",font = ('Comic Sans MS',16))
b7.grid(row=14,column=15)

window.mainloop()