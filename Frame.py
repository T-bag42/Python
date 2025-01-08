from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title('Frame')

frame = Frame(janela, width=300, height=300, bg='red').grid(row=0, column=0)
Label(frame, text='olha só').grid(row=0, column=0)

janela.mainloop()
