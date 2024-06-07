from tkinter import *
from PIL import Image,ImageTk
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3

engine = pyttsx3.init()

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)


##########Funcionality

def search():
    data = json.load(open('data.json'))
    word = enterwordEntry.get()
    word = word.lower()
    if word in data:
        meaning = data[word]
        print(meaning)
        textArea.delete(1.0,END)
        for item in meaning:
            textArea.insert(END,u'\u2022'+item+'\n')

    elif len(get_close_matches(word,data.keys())) >0:
        close_match = get_close_matches(word,data.keys())[0]
        res = messagebox.askyesno("confirm",f'Did you mean {close_match} instead? ')
        if res == True:
            enterwordEntry.delete(0,END)
            enterwordEntry.insert(END,close_match)

            meaning = data[close_match]

            textArea.delete((1.0,END))
            for item in meaning:


                textArea.insert(END, u'\u2022'+'\n\n')

        else:
            messagebox.showerror('Error','The word doesnt exist,Please double check it.')
            enterwordEntry.delete(0,END)
            textArea.delete((1.0,END))

    else:
        messagebox.showinfo('Information ', 'The word doesnt exist.')
        enterwordEntry.delete(0,END)
        textArea.delete()


def clear():
    enterwordEntry.delete(0,END)
    textArea.delete(1.0,END)


def wordaudio():
    engine.say(enterwordEntry.get())
    engine.runAndWait()


def meaningaudio():
    engine.say(textArea.get())
############GUI
root = Tk()
root.geometry('1000x626+100+30')
root.title('TalkingDictionary')
root.resizable(False, False)



bgImage = ImageTk.PhotoImage(file='bgImage2.png')
#Label(root)
bgLabel = Label(root,image=bgImage)
bgLabel.place(x=0,y=0)

#enterLabel = Label(root, text='Hello', font=('Arial', 20, 'bold'), foreground='blue', bg='#FFFFFF')
#enterLabel.pack()
#enterLabel.place(x=750, y=200)


enterwordEntry = Entry(root, font=('airal',23), justify=CENTER, bd=3, relief=GROOVE)
enterwordEntry.place(x=318, y=130)

searchImage = PhotoImage(file='search.png')
searchButton = Button(root, image=searchImage, bd=0, bg='white', cursor='hand2', activebackground='white', command=search)
searchButton.place(x=420,y=188)

micImage = PhotoImage(file='mic.png')
micButton = Button(root,image=micImage, bd=0, bg='white', activebackground='white',cursor='hand2', command=wordaudio)
micButton.place(x=510, y=188)

meaningLabel = Label(root, text='Meaning', font=('Arial', 17), foreground='blue',bg='white')
meaningLabel.place(x=430, y=240)

textArea = Text(root,width=50,height=10,font=('arial',10), bd=4, relief=GROOVE)
textArea.place(x=310, y=280)

audioImage = PhotoImage(file='mic.png')
audioButton = Button(root,image=audioImage, bd=0, bg='white', activebackground='white',cursor='hand2',command=meaningaudio)
audioButton.place(x=420, y=460)

clearImage = PhotoImage(file='trash.png')
clearButton = Button(root,image=clearImage, bd=0, bg='white', activebackground='white',cursor='hand2', command=clear)
clearButton.place(x=510, y=460)

def enter_function(event):
    searchButton.invoke()



root.bind('<Return>',enter_function)

root.mainloop()