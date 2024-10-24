import customtkinter as ctk
import tkinter as tk  # Importar tkinter para a Listbox
from tkinter import messagebox

# Definir o modo de aparência do CustomTkinter
ctk.set_appearance_mode('dark')

# Função para adicionar a tarefa
def adicionar_tarefa():
    titulo_tarefa = tarefa.get()
    descricao_tarefa = descricao.get()
    prioridade_tarefa = prioridade.get()

    if not titulo_tarefa or not prioridade_tarefa:
        messagebox.showwarning("Entrada Inválida", "O título e a prioridade são obrigatórios.")
        return
    if prioridade_tarefa not in ['alta', 'media', 'baixa']:
        messagebox.showwarning("Entrada Inválida", "A prioridade deve ser: Alta, Média ou Baixa.")
        return

    nova_tarefa = f"Título: {titulo_tarefa} | Descrição: {descricao_tarefa} | Prioridade: {prioridade_tarefa}"
    tarefas.append(nova_tarefa)

    # Atualizar a lista de tarefas
    lista_tarefas.delete(0, tk.END)  # Limpa a listbox antes de adicionar as tarefas novamente
    for i in tarefas:
        lista_tarefas.insert(tk.END, i)

    # Limpar os campos de entrada
    tarefa.delete(0, ctk.END)
    descricao.delete(0, ctk.END)
    prioridade.delete(0, ctk.END)


janela = ctk.CTk()
janela.geometry('600x460')
janela.title('GERENCIADOR DE TAREFAS')
janela.resizable(False, False)


tarefas = []

# Título da aplicação
ctk.CTkLabel(janela, 
             text='Gerenciar Tarefas',
             text_color='White',
             font=('arial', 15, 'bold')).pack(pady=10)


ctk.CTkLabel(janela, text="Título da Tarefa").pack(pady=10)
tarefa = ctk.CTkEntry(janela)
tarefa.pack(pady=5)


ctk.CTkLabel(janela, text="Descrição da Tarefa").pack(pady=10)
descricao = ctk.CTkEntry(janela)
descricao.pack(pady=5)

ctk.CTkLabel(janela, text='Prioridade: Alta - Média - Baixa').pack(pady=10)
prioridade = ctk.CTkEntry(janela)
prioridade.pack(pady=10)


btt = ctk.CTkButton(janela,
                    text='Adicionar',
                    width=100,
                    height=50,
                    fg_color='green',
                    command=adicionar_tarefa)
btt.pack(pady=5)


lista_tarefas = tk.Listbox(janela, height=10, width=80)
lista_tarefas.pack(pady=10)

janela.mainloop()
