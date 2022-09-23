#!/usr/bin/python3

# Automatizador de construção do Hexagonix, por Felipe Miguel Nery Lunkes
# Licenciado sobre GPL-3.0 
#
# Front-end para a ferramenta hx

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

        print("Ação: configure\n")

        os.system("sudo ./configure.sh")

        self.terminar() 

    def construirHX(self):

        print("Ação: construirHX\n")

        os.system("sudo hx -i hx")

        self.terminar() 

    def construirAHX(self):

        print("Ação: construirAHX\n")

        os.system("sudo hx -i ahx")

        self.terminar()

    def limpar(self):

        print("Ação: limpar\n")

        os.system("hx limpar")

        self.terminar()

    def execHX(self):

        print("Ação: execHX\n")

        os.system("hx -v hx")

        self.terminar()

    def execAHX(self):

        print("Ação: execAHX\n")

        os.system("hx -v ahx")

        self.terminar()

    def terminar(self):

        print("\nTerminado!\n")

# 

janela=Tk()
autobuild=hxAutoBuild(janela)
janela.title('hx autobuild para Hexagonix H1-R6+ (v0.1)')
janela.geometry("500x400+10+10")
print("\nhx autobuild para Hexagonix H1-R6+")
print("Copyright (C) 2022-2022 Felipe Miguel Nery Lunkes")
print("Todos os direitos reservados")
print("\nAguardando interação com o usuário...")
janela.mainloop()
print("Finalizado pelo usuário.")