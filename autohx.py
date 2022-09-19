#!/usr/bin/python3

# Automatizador de construção do Hexagonix, por Felipe Miguel Nery Lunkes
# Licenciado sobre GPL-3.0 

from tkinter import *
import os

class hxAutoBuild:

    def __init__(self, win):

        self.lbl1=Label(win, text='Ferramenta de automatização de construção para Hexagonix')
        self.lbl2=Label(win, text='Copyright (C) 2022 Felipe Miguel Nery Lunkes')
        self.lbl3=Label(win, text='Todos os direitos reservados.')

        self.lbl1.place(x=40, y=10)
        self.lbl2.place(x=90, y=30)
        self.lbl3.place(x=150, y=50)

        self.botao0=Button(win, text='Configurar ambiente (./configure.sh)', command=self.configure)
        self.botao1=Button(win, text='Construir Hexagonix', command=self.construirHX)
        self.botao2=Button(win, text='Construir Andromeda', command=self.construirAHX)
        self.botao3=Button(win, text='Limpar árvore', command=self.limpar)
        self.botao4=Button(win, text='Executar Hexagonix (vm)', command=self.execHX)
        self.botao5=Button(win, text='Executar Andromeda (vm)', command=self.execAHX)
       
        self.botao0.place(x=120, y=80)
        self.botao1.place(x=20, y=130)
        self.botao2.place(x=190, y=130)
        self.botao3.place(x=365, y=130)
        self.botao4.place(x=40, y=180)
        self.botao5.place(x=250, y=180)

    def configure(self):

        print("configure")

        os.system("./configure.sh")

        self.terminar() 

    def construirHX(self):

        print("construirHX")

        os.system("hx -i hx")

        fim() 

    def construirAHX(self):

        print("construirAHX")

        os.system("hx -i ahx")

    def limpar(self):

        print("limpar")

        os.system("hx limpar")

    def execHX(self):

        print("execHX")

        os.system("hx -v hx")

    def execAHX(self):

        print("execAHX")

        os.system("hx -v ahx")

    def terminar(self):

        print("Terminado!")

# 

janela=Tk()
imcalc=hxAutoBuild(janela)
janela.title('hx autobuild para Hexagonix H1-R6+')
janela.geometry("500x400+10+10")
janela.mainloop()