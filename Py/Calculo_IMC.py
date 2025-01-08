from tkinter import *

janela = Tk()  # elemento básico para criação da janela
janela.title('Sistema pizzaria')  # define o título da janela
janela.geometry('500x300')  # Define o tamanho da interface
janela.resizable(False, False)  # bloqueia que o usuário altere o tamanho da interface



def calcular():
    try:
        peso_valor = float(peso.get())  # Obtém o valor inserido no campo de entrada "peso"
        altura_valor = float(altura.get())  # Obtém o valor inserido no campo de entrada "altura"
        
        # Calcula o IMC
        imc = peso_valor / (altura_valor ** 2)
        
        # Formata o resultado com 1 casa decimal
        resultado_formatado = f"{imc:.1f}"
        
        # Atualiza o texto do Label
        resultado.config(text=f'Seu IMC é: {resultado_formatado}')
    except ValueError:
        resultado.config(text='Por favor, insira valores válidos!')


Label(janela, text='Cálculo de IMC').grid(row=0, column=0, columnspan=2)

Label(janela, text='Insira seu peso (kg)').grid(row=1, column=0)

peso = Entry(janela)
peso.grid(row=1, column=1)

Label(janela, text='Insira sua altura (m)').grid(row=2, column=0)

altura = Entry(janela)
altura.grid(row=2, column=1)

# Adiciona a função "calcular" ao botão
Button(janela, text='Calcular', command=calcular).grid(row=3, column=0)

resultado = Label(janela, text='Seu IMC é...')
resultado.grid(row=3, column=1)

Label(janela, text='SubPeso', fg='blue').grid(row=4, column=1)
Label(janela, text='Normal', fg='green').grid(row=4, column=2)
Label(janela, text='SobrePeso', fg='red').grid(row=4, column=3)

Label(janela, text='', bg='blue',padx=60, pady=1).grid(row=5, column=1)
Label(janela, text='', bg='green',padx=50, pady=1).grid(row=5, column=2)
Label(janela, text='', bg='red',padx=50, pady=1).grid(row=5, column=3)

Label(janela, text='16.0').grid(row=6, column=0, columnspan=2)
Label(janela, text='18.5').grid(row=6, column=1, columnspan=2)
Label(janela, text='25.0').grid(row=6, column=2, columnspan=2)
Label(janela, text='40.0').grid(row=6, column=4)

janela.mainloop()  # elemento básico para criação da janela
