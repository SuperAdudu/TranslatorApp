from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator

root = Tk()
root.title('Google Translator')
root.geometry('1080x400')
root.resizable(False,False)
root.configure(background='white')

def choose_language():
    c1 = combo1.get()
    c2 = combo2.get()
    label1.configure(text=c1)
    label2.configure(text=c2)
    root.after(1000,choose_language)

def translate_now():
    text_ = text1.get(1.0,END)
    t1 = Translator()
    trans_text = t1.translate(text_,src=combo1.get(),dest=combo2.get())
    trans_text = trans_text.text
    text2.delete(1.0,END)
    text2.insert(END,trans_text)
    

imageTrans = PhotoImage(file='image/arrow.png')
imageLabel = Label(root,image=imageTrans,width=150).place(x=460,y=50)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combo1 = ttk.Combobox(root, values=languageV,font= 'Roboto 14',state='r')
combo1.place(x=110, y=20)
combo1.set("ENGLISH")
label1 = Label(root, text='ENGLISH',font='segoe 30 bold',bg='white',width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

combo2 = ttk.Combobox(root, values=languageV,font= 'Roboto 14',state='r')
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")
label2 = Label(root, text='SELECT LANGUAGE',font='segoe 30 bold',bg='white',width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

f1 = Frame(root,bg='Black',bd=5)
f1.place(x=10,y=118,width=440,height=210)
text1 = Text(f1,font='Roboto 20',bg='white',relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)
scroll1 = Scrollbar(f1)
scroll1.pack(side='right',fill='y')
scroll1.configure(command=text1.yview)
text1.configure(yscrollcommand=scroll1.set)

f2 = Frame(root,bg='Black',bd=5)
f2.place(x=620,y=118,width=440,height=210)
text2 = Text(f2,font='Roboto 20',bg='white',relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)
scroll2 = Scrollbar(f2)
scroll2.pack(side='right',fill='y')
scroll2.configure(command=text2.yview)
text2.configure(yscrollcommand=scroll2.set)

translate = Button(root,text="Translate",font=('Roboto 15'),activebackground='white',cursor='hand2',bd=1,width=10,height=2,bg='black',fg='white',command=translate_now)
translate.place(x=476,y=250)

choose_language()

root.mainloop()