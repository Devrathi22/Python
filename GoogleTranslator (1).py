#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from tkinter import ttk
#ttk brings combo box
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = combo_sor.get()
    d = combo_dest.get()
    masg = Sor_txt.get(1.0,END)
    textget = change(text = masg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)
    
root=Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='purple')

lab_txt=Label(root,text="Translator",font=("Time New Roman",40,"bold"),bg="white")
lab_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Source Text",font=("Time New Roman",20,"bold"),fg="black",bg="white")
lab_txt.place(x=100,y=100,height=20,width=300)

Sor_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD,bg="plum")
Sor_txt.place(x=10,y=130,height=150,width=480)

list_text = list(LANGUAGES.values())

combo_sor = ttk.Combobox(frame,value=list_text)
combo_sor.place(x=10,y=300,height=40,width=150)
combo_sor.set("English")

button_change = Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=300,height=40,width=150)

combo_dest = ttk.Combobox(frame,value=list_text)
combo_dest.place(x=330,y=300,height=40,width=150)
combo_dest.set("English")

lab_txt=Label(root,text="Destination Text",font=("Time New Roman",20,"bold"),bg="white")
lab_txt.place(x=100,y=360,height=20,width=300)

dest_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD,bg="plum")
dest_txt.place(x=10,y=400,height=150,width=480)


root.mainloop()


# In[1]:


pip install googletrans


# In[2]:


pip install googletrans==3.1.0a0


# In[ ]:




