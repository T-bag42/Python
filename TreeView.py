from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title('Tree View')

# Definindo o Treeview
tree = ttk.Treeview(janela, selectmode='browse', columns=('a', 'b', 'c'), show='headings')

# Configurando as colunas e os cabeçalhos
tree.column('a', width=50, minwidth=50, stretch=NO)
tree.heading('a', text='Id')

tree.column('b', width=200, minwidth=50, stretch=NO)
tree.heading('b', text='Nome')

tree.column('c', width=100, minwidth=50, stretch=NO)
tree.heading('c', text='Preço')

# Posicionando o Treeview na janela
tree.grid(row=0, column=0)

elementos = [1, '4 queijos', '42']

for i in range(0, 4):
    tree.insert("", "end", values=elementos, tags='1')
    
tree.insert("", "end", values=(2, "Produto B", 20.0))

janela.mainloop()
