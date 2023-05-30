import tkinter as tk
from Class import Buttons
def buttons(self,janela):
    self.janela=janela
    self.janela.title("itens")
    self.selecione = tk.Label(self.janela, text="Qual é a sua cor favorita?")
    self.pergunta.pack()



janela=tk.Tk()
jg=Buttons(janela)
janela.mainloop()