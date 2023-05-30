import tkinter as tk

def buttons(self,janela):
    self.janela=janela
    self.janela.title("itens")
    self.selecione = tk.Label(self.janela, text="Qual é a sua cor favorita?")
    self.pergunta.pack()



janela=tk.Tk()
janela.geometry("800x600")

janela.mainloop()