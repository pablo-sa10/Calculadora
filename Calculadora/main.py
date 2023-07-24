from tkinter import  *
from tkinter import ttk

#cores
cor1 = '#1e1f1e' #preto
cor2 = '#feffff' #branco
cor3 = '#38576b' #azul
cor4 = '#ECEFF1' #cinza
cor5 = '#FFAB40' #laranja

janela = Tk()
janela.title('Calculadora do Pablão')
janela.geometry('235x310')
janela.config(bg=cor1)

#criando frames
frame_tela = Frame(janela, width=235, height=50, bg= cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268,)
frame_corpo.grid(row=1, column=0)

#variavel
todos_valores = ''

#criando label
valor_texto = StringVar()

#criando a logica
def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
    
    #passando o valor p tela
    valor_texto.set(todos_valores)

#função para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

#função limpar tela

def limpar():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')



app_label = Label(frame_tela, textvariable = valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('ivy 18'), bg= cor3, fg=cor2)
app_label.place(x=0,y=0)

#criando botões
#botao de limpar
b_1 = Button(frame_corpo, command = limpar, text='C', width=11, height=2, bg=cor4, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
#botao de porcent
b_2 = Button(frame_corpo, command = lambda: entrar_valores('%'), text='%', width=5, height=2, bg=cor4, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
#botao de divisao
b_3 = Button(frame_corpo, command = lambda: entrar_valores('/'), text='/', width=5, height=2, bg=cor5, fg= cor2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

#botao 7 ao 9
b_4 = Button(frame_corpo, command = lambda: entrar_valores('7'), text='7', width=5, height=2, bg=cor4, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, command = lambda: entrar_valores('8'), text='8', width=5, height=2, bg=cor4, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_corpo, command = lambda: entrar_valores('9'), text='9', width=5, height=2, bg=cor4, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)

#botao de multiplicação
b_7 = Button(frame_corpo, command = lambda: entrar_valores('*'), text='*', width=5, height=2, bg=cor5, fg= cor2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

#botao do 4 ao 6
b_8 = Button(frame_corpo, command = lambda: entrar_valores('4'), text='4', width=5, height=2, bg=cor4, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, command = lambda: entrar_valores('5'), text='5', width=5, height=2, bg=cor4, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_corpo, command = lambda: entrar_valores('6'), text='6', width=5, height=2, bg=cor4, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)

#botao de menos
b_11 = Button(frame_corpo, command = lambda: entrar_valores('-'), text='-', width=5, height=2, bg=cor5, fg= cor2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

#botao do 1 ao 3
b_12 = Button(frame_corpo, command = lambda: entrar_valores('1'), text='1', width=5, height=2, bg=cor4, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, command = lambda: entrar_valores('2'), text='2', width=5, height=2, bg=cor4, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_corpo, command = lambda: entrar_valores('3'), text='3', width=5, height=2, bg=cor4, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)

#botao de mais
b_15 = Button(frame_corpo, command = lambda: entrar_valores('+'), text='+', width=5, height=2, bg=cor5, fg= cor2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

#botao 0
b_16 = Button(frame_corpo, command = lambda: entrar_valores('0'), text='0', width=11, height=2, bg=cor4, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
#botao de ponto
b_17 = Button(frame_corpo, command = lambda: entrar_valores('.'), text='.', width=5, height=2, bg=cor4, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
#botao de igual
b_18 = Button(frame_corpo, command = calcular, text='=', width=5, height=2, bg=cor5, fg= cor2, font=('ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)


janela.mainloop()