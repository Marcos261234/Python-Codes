import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

ctk.set_appearance_mode('dark')
# ----------------------------------------------------FUNCAO-------------------------------------------------------
def calculo_imc():
    peso_calculo = float(peso.get())
    altura_calculo = float(altura.get())
    imc = peso_calculo/(altura_calculo * altura_calculo)
    
    if imc < 17:
        label_message.configure(text=f'IMC {imc:.2f}: ABAIXO DO PESO', text_color='red')
    elif imc >= 17 and imc < 18.5:
         label_message.configure(text=f'IMC {imc:.2f}: ABAIXO DO PESO', text_color='yellow')
    elif imc >= 18.5 and imc <= 24.99:
        label_message.configure(text=f'IMC {imc:.2f}: PESO NORMAL', text_color='green')
    elif imc >= 25 and imc <= 29.99:
        label_message.configure(text=f'IMC {imc:.2f}: ACIMA DO PESO', text_color='yellow')
    elif imc >= 30 and imc <= 34.99:
        label_message.configure(text=f'IMC {imc:.2f}: OBESIDADE I', text_color='red')
    elif imc >- 35 and imc <= 39.99:
        label_message.configure(text=f'IMC {imc:.2f}: OBESIDADE II(severo)', text_color='red')
    elif imc > 40:
        label_message.configure(text=f'IMC {imc:.2f}: ABAIXO DO PESO', text_color='red')
# ----------------------------------------------------Vinyplg----------------------------------------------------------

janela = ctk.CTk()
janela.geometry('300x300')
janela.resizable(False, False)
janela.title('App Saúde')

imagem = Image.open("imagem funde.jpeg")
imagem = imagem.resize((300, 300))
imagem_fundo = ImageTk.PhotoImage(imagem)

label_fundo = ctk.CTkLabel(janela, image=imagem_fundo, text="")
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)
label_fundo.image = imagem_fundo

ctk.CTkLabel(janela, text='CALCULO DE IMC',
             text_color='yellow',
             corner_radius=10,
             font=('arial', 20, 'bold')).pack(pady=10)

ctk.CTkLabel(janela, text="Digite o peso", corner_radius=10).pack(pady=5)
peso = ctk.CTkEntry(janela, corner_radius=10)
peso.pack(pady=5)

ctk.CTkLabel(janela, text='Digite sua altura', corner_radius=10).pack(pady=5)
altura = ctk.CTkEntry(janela, corner_radius=10)
altura.pack(pady=5)

btt = ctk.CTkButton(janela,
                    text='Calcular IMC',
                    fg_color='green',
                    corner_radius=10,
                    command=calculo_imc)
btt.pack(pady=10)

label_message = ctk.CTkLabel(janela, text='')
label_message.pack(pady=20)



janela.mainloop()