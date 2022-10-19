#!/usr/bin/python3

# Automatizador de construção do Hexagonix, por Felipe Miguel Nery Lunkes
# Licenciado sobre GPL-3.0 
#
# Frontend para a ferramenta hx

from tkinter import *
import os

class hxAutoBuild:

    def __init__(self, win):

        self.lbl1=Label(win, text='Ferramenta de automatização de construção para Hexagonix')
        self.lbl2=Label(win, text='Selecione uma das opções abaixo para continuar')

        self.lbl1.place(x=40, y=5)
        self.lbl2.place(x=80, y=50)

        self.botao0=Button(win, text='Configurar ambiente (./configure.sh)', command=self.configure)
        self.botao1=Button(win, text='Construir Hexagonix', command=self.construirHX)
        self.botao2=Button(win, text='Limpar árvore', command=self.limpar)
        self.botao3=Button(win, text='Executar Hexagonix (vm)', command=self.execHX)

        self.botao0.place(x=120, y=100)
        self.botao1.place(x=5, y=150)
        self.botao2.place(x=375, y=150)
        self.botao3.place(x=174, y=150)

    def configure(self):

        print("Ação solicitada pelo usuário: configure\n")

        os.system("gnome-terminal -- bash -c 'echo hx autobuild && echo && echo Você deve inserir sua senha para continuar... && echo && sudo ./configure.sh && echo &&echo Pressione ENTER para voltar ao hx autobuild... && read pausa'")

        self.terminar() 

    def construirHX(self):

        print("Ação solicitada pelo usuário: construirHX\n")

        os.system("gnome-terminal -- bash -c 'echo hx autobuild && echo && echo Você deve inserir sua senha para continuar... && echo && sudo hx -i hx && echo && echo Pressione ENTER para voltar ao hx autobuild... && read pausa'")

        self.terminar() 

    def limpar(self):

        print("AçAção solicitada pelo usuárioão: limpar\n")

        os.system("hx limpar")

        self.terminar()

    def execHX(self):

        print("Ação solicitada pelo usuário: execHX\n")

        os.system("hx -v hx")

        self.terminar()

    def terminar(self):

        print("Solicitação finalizada.\n")

# 

janela=Tk()
autobuild=hxAutoBuild(janela)
janela.title('hx autobuild para Hexagonix H2 (v0.8)')
janela.geometry("500x250+10+10")
print("\nhx autobuild (Hexagonix H1-R6+)")
print("Copyright (C) 2022-2022 Felipe Miguel Nery Lunkes")
print("Todos os direitos reservados")
print("\nAguardando interação com o usuário...")
janela.mainloop()
print("Finalizado pelo usuário.")