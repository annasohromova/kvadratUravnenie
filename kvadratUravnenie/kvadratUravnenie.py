from tkinter import *

def tekst_to_lbl(event):
    t=ent.get() 
    lbl.configure(text=t)
    ent.delete(0,END)#2,7

aken=Tk() 
aken.geometry("700x300") 
aken.title("Ruutvõrrandi lahendamine") 
lbl=Label(aken,text="Ruutvõrrandi lahendamine",bg="yellow",fg="#AA4A44",font="Arial 20", height=2,width=22)
ent=Entry(aken,fg="blue",bg="lightblue",width=5,font="Arial 20",justify=LEFT)

ent.bind("<Return>",tekst_to_lbl)#Enter
lbl.pack()
ent.pack(side=LEFT)
aken.mainloop()
