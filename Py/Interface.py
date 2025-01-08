from tkinter import *

janela = Tk() #elemento basico para criação da janeja
janela.title('Sistema pizzaria') #define o titulo da janela
janela.geometry('700x700') # Define o tamanho da interface
janela.resizable(False,False) #bloqueia que o usuraio altere o tamanho da inteface 

def acessar():
    acesslabel['text'] = 'Digite usuario e senha para confirmar acesso'

Label(janela, text='Teste', bg='blue', fg='yellow3', padx=30, pady=80).grid(row=0, column=0)

Button(janela, text='Confirmar acesso',bg='black', fg='white', height=4, width=22, command=acessar).grid(row=371, column=350)

Entry(janela, bg='black', fg='white').grid(row=350, column=350) #elemento de entrada de dados
Entry(janela, bg='black', fg='white', show='*').grid(row=370, column=350) #elemento de entrada de dados ocultando o que for digitado

acesslabel = Label(janela, text='Coloque suas credenciais')
acesslabel.grid(row=372, column=350)

janela.mainloop() #elemento basico para criação da janeja