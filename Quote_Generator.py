import random
import json
from tkinter import *

with open('Quotes.json', encoding='utf-8') as base:
     quotes = json.load(base)

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1["pady"] = 20
        self.widget1.pack()

        self.widget2 = Frame(master)
        self.widget2["pady"] = 50
        self.widget2.pack()

        self.widget3 = Frame(master)
        self.widget3["pady"] = 50
        self.widget3.pack()
        
        self.msg1 = Label(self.widget1, text="Quote Generator")
        self.msg1["font"] = ("Aptos Black", "18", "italic", "bold")
        self.msg1.pack (side=TOP)

        self.msg2 = Label(self.widget2, text="", wraplength= 350)
        self.msg2["font"] = ("Verdana", "10", "italic", "bold")
        self.msg2.pack ()

        self.msg3 = Label(self.widget3, text="Thanks")
        self.msg3["font"] = ("Verdana", "10", "italic", "bold")
        self.msg3.pack ()
        
        self.gerar = Button(self.widget2)
        self.gerar["text"] = "Generate"
        self.gerar["font"] = ("Calibri", "12", "bold")
        self.gerar["width"] = 15
        self.gerar["command"] = self.mudarTexto
        self.gerar.pack ()

        self.exit = Button(self.widget3)
        self.exit["text"] = "Exit"
        self.exit["font"] = ("Calibri", "10", "bold")
        self.exit["width"] = 10
        self.exit["command"] = self.widget3.quit
        self.exit.pack (side=BOTTOM)

    def mudarTexto(self):
        random_quote = random.choice([quote["quote"] for quote in quotes])
        self.msg2.config(text=random_quote)
        
root = Tk()
root.title("Quote Generator")
Application(root)
root.geometry("400x400")
root.minsize(400, 400)
root.maxsize(400, 400)
root.mainloop()
