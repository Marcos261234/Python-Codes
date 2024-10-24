import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox

ctk.set_appearance_mode('dark')  
ctk.set_default_color_theme('blue')


users = {}

def register_user():
    nome = entry_nome.get()
    email = entry_email.get()
    usuario = entry_usuario_registro.get()
    senha = entry_senha_registro.get()

    if nome and email and usuario and senha:
        if usuario not in users:
            users[usuario] = {'nome': nome, 'email': email, 'senha': senha}
            messagebox.showinfo('Registro', 'Usuário registrado com sucesso!')
            form_janela.destroy()
        else:
            messagebox.showerror('Erro', 'Usuário já existe!')
    else:
        messagebox.showerror('Erro', 'Preencha todos os campos!')

def register_formulario():
    global form_janela, entry_nome, entry_email, entry_usuario_registro, entry_senha_registro

    
    form_janela = ctk.CTkToplevel(janela)
    form_janela.title("Formulário de Registro")
    form_janela.geometry('400x500')
    form_janela.iconbitmap("b1b6f00d-f82b-4719-82bf-0dd5365cfa19.ico")

    imagem = Image.open("istockphoto-1414729026-612x612.jpg")
    imagem = imagem.resize((400, 500))
    imagem_fundo = ImageTk.PhotoImage(imagem)

    label_fundo = ctk.CTkLabel(form_janela, image=imagem_fundo, text="")
    label_fundo.place(x=0, y=0, relwidth=1, relheight=1)
    label_fundo.image = imagem_fundo
    
    ctk.CTkLabel(form_janela, text="Nome Completo").pack(pady=5)
    entry_nome = ctk.CTkEntry(form_janela, placeholder_text="Digite seu nome")
    entry_nome.pack(pady=5)

    ctk.CTkLabel(form_janela, text="E-mail").pack(pady=5)
    entry_email = ctk.CTkEntry(form_janela, placeholder_text="Digite seu e-mail")
    entry_email.pack(pady=5)

    ctk.CTkLabel(form_janela, text="Usuário").pack(pady=5)
    entry_usuario_registro = ctk.CTkEntry(form_janela, placeholder_text="Escolha um nome de usuário")
    entry_usuario_registro.pack(pady=5)

    ctk.CTkLabel(form_janela, text="Senha").pack(pady=5)
    entry_senha_registro = ctk.CTkEntry(form_janela, placeholder_text="Escolha uma senha", show='*')
    entry_senha_registro.pack(pady=5)

    ctk.CTkButton(form_janela, text="Registrar", command=register_user).pack(pady=5)


def login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    if usuario in users and users[usuario]['senha'] == senha:
        label_message.configure(text='Login bem-sucedido!', text_color='green')
    else:
        label_message.configure(text='Usuário ou senha incorretos!', text_color='red')

def mostrar_cadastros():
    janela_cadastros = ctk.CTkToplevel(janela)
    janela_cadastros.title('Lista de Cadastros')
    janela_cadastros.geometry('300x300')
    janela_cadastros.iconbitmap("b1b6f00d-f82b-4719-82bf-0dd5365cfa19.ico")
    
    imagem = Image.open("istockphoto-1414729026-612x612.jpg")
    imagem = imagem.resize((300, 300))
    imagem_fundo = ImageTk.PhotoImage(imagem)
    
    label_fundo = ctk.CTkLabel(janela_cadastros, image=imagem_fundo, text="")
    label_fundo.place(x=0, y=0, relwidth=1, relheight=1)
    label_fundo.image = imagem_fundo
    
    label_cadastros = ctk.CTkLabel(janela_cadastros, text="Usuários Registrados", font=('Arial', 18, 'bold'))
    label_cadastros.pack(pady=10)
    

    for usuario in users:
        ctk.CTkLabel(janela_cadastros, text=usuario).pack(pady=5)
        

janela = ctk.CTk()
janela.title('Menu de Registro e Login')
janela.geometry('400x400')
janela.iconbitmap("b1b6f00d-f82b-4719-82bf-0dd5365cfa19.ico")

imagem = Image.open("istockphoto-1414729026-612x612.jpg")
imagem = imagem.resize((400, 400))
imagem_fundo = ImageTk.PhotoImage(imagem)

label_fundo = ctk.CTkLabel(janela, image=imagem_fundo, text="")
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

label_usuario = ctk.CTkLabel(janela, text='Senai', bg_color='transparent', font=('arial', 25, 'bold',))
label_usuario.pack(pady=25)

entry_usuario = ctk.CTkEntry(janela, placeholder_text='usuário')
entry_usuario.pack(pady=10)

entry_senha = ctk.CTkEntry(janela, placeholder_text= 'senha', show='*')
entry_senha.pack(pady=10)

button_register = ctk.CTkButton(janela, text='Registrar', command=register_formulario)
button_register.pack(pady=5)

button_login = ctk.CTkButton(janela, text='Login', command=login)
button_login.pack(pady=5)

button_cadastros = ctk.CTkButton(janela, text='Mostrar Cadastros', command=mostrar_cadastros)
button_cadastros.pack(pady=5)

label_message = ctk.CTkLabel(janela, text='')
label_message.pack(pady=20)

janela.mainloop()