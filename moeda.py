import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode('dark')
#--------------------------------------------Função---------------------------------------
def converter():
    v = float(valor.get())
    c = float(cotacao.get())
    valor_convertido = v * c
    messagebox.showinfo('Valor Convertido', f'O valor é {valor_convertido:.2f}R$')
#--------------------------------------------by viny--------------------------------------------

janela = ctk.CTk()
janela.geometry('350x350')
janela.title('Conversor de Moedas')
janela.resizable(False, False)
janela.title('Sistema de Conversão de moedas')

ctk.CTkLabel(janela, 
             text='Sistema de Conversão',
             text_color='White',
             font=('arial', 25, 'bold')).pack(pady=10)

valor = ctk.CTkEntry(janela,
                     width=250,
                     height=20,
                     placeholder_text='Digite o valor em dólar')
valor.pack()
cotacao = ctk.CTkEntry(janela,
                     width=250,
                     height=20,
                     placeholder_text='Digite o valor da cotação')
cotacao.pack(pady=10)

btt = ctk.CTkButton(janela,
                      text='Calcular',
                      width=150,
                      height=50,
                      fg_color='red',
                      command=converter)

btt.pack()



janela.iconbitmap('interface/banknotespaymentmoney_billetesdebanco_pag_3773.ico')


janela.mainloop()
