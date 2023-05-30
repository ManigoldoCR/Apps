import tkinter as tk
class Buttons:
  def __init__(self,janela):
    self.janela=janela
    self.janela.title("itens")
    self.selecione = tk.Label(self.janela, text="selecione um arquivo")
    self.selecione.pack()
    self.bott1 = tk.Button(self.janela,text="Informações",command=self.usuarios)
    self.bott1.pack()
  def usuarios(self):
    self.ress = tk.Label(self.janela, text="ainda estou começando a programar")
    self.ress.pack()
