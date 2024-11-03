import customtkinter as ctk

def atualizar_display(valor):
    texto_atual = resultado_display.cget("text")
    resultado_display.configure(text=texto_atual + valor)
    
def limpar():
    resultado_display.configure(text="")
    
def calcular():
    expressao = resultado_display.cget("text")
    resultado = eval(expressao) 
    resultado_display.configure(text=str(resultado))
    
def calcular_porcentagem():
    expressao = resultado_display.cget("text")
    valor = eval(expressao)
    porcentagem = valor / 100  
    resultado_display.configure(text=str(porcentagem))


ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.geometry('600x400')
app.resizable('false', 'false')
app.title('Calculadora')

numero7_btt = ctk.CTkButton(app, text='7',
                            width=100,
                            height=50,
                            fg_color='#1C1C1C',
                            command=lambda: atualizar_display('7'))
numero7_btt.place(x=25, y=85)

numero8_btt = ctk.CTkButton(app, text='8',
                            width=100,
                            height=50,
                            fg_color='#1C1C1C',
                            command=lambda: atualizar_display('8'))
numero8_btt.place(x=145, y=85)

numero9_btt = ctk.CTkButton(app, text='9',
                            width=100,
                            height=50,
                            fg_color='#1C1C1C',
                            command=lambda: atualizar_display('9'))
numero9_btt.place(x=260, y=85)

numero4_btt = ctk.CTkButton(app, text='4',
                            width=100,
                            height=50,
                            fg_color='#1C1C1C',
                            command=lambda: atualizar_display('4'))
numero4_btt.place(x=25, y=150)

numero5_btt = ctk.CTkButton(app, text='5',
                            width=100,
                            height=50,
                            fg_color='#1C1C1C',
                            command=lambda: atualizar_display('5'))
numero5_btt.place(x=145, y=150)

numero6_btt = ctk.CTkButton(app, text='6',
                            width=100,
                            height=50,
                            fg_color='#1C1C1C',
                            command=lambda: atualizar_display('6'))
numero6_btt.place(x=260, y=150)

numero1_btt = ctk.CTkButton(app, text='1',
                            width=100,
                            height=50,
                            fg_color='#1C1C1C',
                            command=lambda: atualizar_display('1'))
numero1_btt.place(x=25, y=215)

numero2_btt = ctk.CTkButton(app, text='2',
                            width=100,
                            height=50,
                            fg_color='#1C1C1C',
                            command=lambda: atualizar_display('2'))
numero2_btt.place(x=145, y=215)

numero3_btt = ctk.CTkButton(app, text='3',
                            width=100,
                            height=50,
                            fg_color='#1C1C1C',
                            command=lambda: atualizar_display('3'))
numero3_btt.place(x=260, y=215)

numero0_btt = ctk.CTkButton(app, text='0',
                            width=220,
                            height=50,
                            fg_color='#1C1C1C',
                            command=lambda: atualizar_display('0'))
numero0_btt.place(x=25, y=285)

ponto_btt = ctk.CTkButton(app, text='.',
                            width=100,
                            height=50,
                            fg_color='#1C1C1C',
                            command=lambda: atualizar_display('.'))
ponto_btt.place(x=260, y=285)

btn_clear = ctk.CTkButton(app, text="AC",
                          width=92, 
                          height=50, 
                          fg_color='grey', 
                          command=limpar)
btn_clear.place(x=380, y=285)

btn_porcent = ctk.CTkButton(app, text="%",
                          width=92, 
                          height=50, 
                          fg_color='grey', 
                          command=lambda: calcular_porcentagem())
btn_porcent.place(x=480, y=285)

btn_resultado = ctk.CTkButton(app, text="=",
                          width=195, 
                          height=50, 
                          fg_color='DarkGoldenrod', 
                          command=calcular)
btn_resultado.place(x=380, y=215)


btt_soma = ctk.CTkButton(app, text='+',
                            width=92,
                            height=50,
                            fg_color='DarkGoldenrod',
                            command=lambda: atualizar_display('+'))
btt_soma.place(x=380, y=150)

btt_sub = ctk.CTkButton(app, text='-',
                            width=92,
                            height=50,
                            fg_color='DarkGoldenrod',
                            command=lambda: atualizar_display('-'))
btt_sub.place(x=480, y=150)

btt_multi = ctk.CTkButton(app, text='x',
                            width=92,
                            height=50,
                            fg_color='DarkGoldenrod',
                            command=lambda: atualizar_display('*'))
btt_multi.place(x=380, y=85)

btt_div = ctk.CTkButton(app, text='÷',
                            width=92,
                            height=50,
                            fg_color='DarkGoldenrod',
                            command=lambda: atualizar_display('/'))
btt_div.place(x=480, y=85)




resultado_display = ctk.CTkLabel(app, text="", width=550, height=50, fg_color="black", corner_radius=8, text_color="white", font=("Arial", 24))
resultado_display.place(x=25, y=25)



app.mainloop()


'''A excessividade dos botões são propositais, para compreensão que tenho noção de espaço e algoritmo'''