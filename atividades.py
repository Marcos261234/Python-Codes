'''import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox


def calcular_velo():
    try:
        vel = float(velocidade.get())
        if vel > 80:
            multa = (vel - 80) * 5 
            messagebox.showwarning('MULTA', f'Você foi multado em R${multa:.2f}!')
        else:
            messagebox.showinfo('Boa Viagem', 'Velocidade permitida.')
    except ValueError:
        messagebox.showerror('Erro', 'Por favor, insira um número válido.')


ctk.set_appearance_mode("dark")  

janela = ctk.CTk()
janela.geometry('300x250')
janela.title('Calcular Velocidade')
janela.resizable(False, False)

ctk.CTkLabel(janela, text="Digite a velocidade").pack(pady=10)
velocidade = ctk.CTkEntry(janela)
velocidade.pack(pady=5)

btt = ctk.CTkButton(janela,
                    text='Calcular',
                    width=100,
                    height=50,
                    fg_color='green',
                    command=calcular_velo)
btt.pack(pady=5)

janela.mainloop()'''

'''import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

def calculo_notas():
    global nota_unidade1, nota_unidade2, nota_unidade3, media
    nota_unidade1 = float(valor1_entry.get())
    nota_unidade2 = float(valor2_entry.get())
    nota_unidade3 = float(terceira_unidade.get())
    
    media = (nota_unidade1 + nota_unidade2 +nota_unidade3)/3
    
    if media >= 7:
        messagebox.showinfo('Emissão de nota', f'Aprovado com média: {media:.2f}')
    if media >= 5:
        messagebox.showinfo('Emissão de nota', f'Em recuperação com média: {media:.2f}')
    if media <= 4.9:
        messagebox.showinfo('Emissão de nota', f'Reprovado com média: {media:.2f}')
        
ctk.set_appearance_mode("dark")  

janela = ctk.CTk()
janela.geometry('300x350')
janela.title('Calcular Velocidade')
janela.resizable(False, False)

ctk.CTkLabel(janela, text="Digite a nota da unidade 1").pack(pady=10)
valor1_entry = ctk.CTkEntry(janela)
valor1_entry.pack(pady=5)

ctk.CTkLabel(janela, text="Digite a nota da unidade 2").pack(pady=10)
valor2_entry = ctk.CTkEntry(janela)
valor2_entry.pack(pady=5)

ctk.CTkLabel(janela, text="Digite a nota da unidade 3").pack(pady=10)
terceira_unidade = ctk.CTkEntry(janela)
terceira_unidade.pack(pady=5)

btt = ctk.CTkButton(janela,
                    text='Calcular',
                    width=100,
                    height=50,
                    fg_color='green',
                    command=calculo_notas)
btt.pack(pady=5)

janela.mainloop()'''

'''import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox



def soma():
    valor1 = float(valor1_entry.get())
    valor2 = float(valor2_entry.get())
    somado = valor1 + valor2   
    messagebox.showinfo('Soma', f'resultado: {somado}')
    
    
def sub():
    valor1 = float(valor1_entry.get())
    valor2 = float(valor2_entry.get())
    subt = valor1 - valor2    
    messagebox.showinfo('Subtração', f'resultado: {subt}')
    
    
def div():
    valor1 = float(valor1_entry.get())
    valor2 = float(valor2_entry.get())
    divid = valor1 / valor2    
    messagebox.showinfo('Divisão', f'Resultado: {divid}')

    
def multi():
    valor1 = float(valor1_entry.get())
    valor2 = float(valor2_entry.get())
    multip = valor1 * valor2    
    messagebox.showinfo('Multiplicação', f'Resultado: {multip}')
    

janela = ctk.CTk()
janela.geometry('400x450')
janela.title('Calcular Velocidade')
janela.resizable(False, False)

ctk.CTkLabel(janela, text="Digite um numero").pack(pady=10)
valor1_entry = ctk.CTkEntry(janela)
valor1_entry.pack(pady=5)

ctk.CTkLabel(janela, text="Digite outro numero").pack(pady=10)
valor2_entry = ctk.CTkEntry(janela)
valor2_entry.pack(pady=5)

btt1 = ctk.CTkButton(janela,
                    text='Somar',
                    width=100,
                    height=50,
                    fg_color='green',
                    command=soma)
btt1.pack(pady=5)

btt2 = ctk.CTkButton(janela,
                    text='Subtrair',
                    width=100,
                    height=50,
                    fg_color='green',
                    command=sub)
btt2.pack(pady=5)

btt3 = ctk.CTkButton(janela,
                    text='Divisão',
                    width=100,
                    height=50,
                    fg_color='green',
                    command=div)
btt3.pack(pady=5)

btt4 = ctk.CTkButton(janela,
                    text='Multiplicação',
                    width=100,
                    height=50,
                    fg_color='green',
                    command=multi)
btt4.pack(pady=5)

janela.mainloop()'''

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

