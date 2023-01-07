#!/usr/bin/python3

# Hexagonix build automator, by Felipe Miguel Nery Lunkes
# Licensed under BSD-3-Clause
#
# Frontend for the hx tool

from tkinter import *
import os

class hxAutoBuild:

    def __init__(self, win):

        self.lbl1=Label(win, text='Hexagonix build automator')
        self.lbl2=Label(win, text='Select one of the options below to continue')
        self.lbl3=Label(win, text='Configuration options')
        self.lbl4=Label(win, text='Build options')

        self.lbl1.place(x=160, y=5)
        self.lbl2.place(x=100, y=50)
        
        self.lbl3.place(x=180, y=90)

        self.botao0=Button(win, text='Configure environment', command=self.configure)
        self.botao1=Button(win, text='Build Hexagonix', command=self.construirHX)
        self.botao2=Button(win, text='Clear source tree', command=self.limpar)
        self.botao3=Button(win, text='Run Hexagonix (vm)', command=self.execHX)

        self.botao0.place(x=50, y=130)
        self.botao2.place(x=300, y=130)

        self.lbl4.place(x=210, y=190)

        self.botao1.place(x=50, y=230)
        self.botao3.place(x=300, y=230)

    def configure(self):

        print("Action requested by the user: configure\n")

        os.system("gnome-terminal -- bash -c 'echo hx autobuild && echo && echo You must enter your password to continue... && echo && sudo ./configure.sh && echo && echo Press ENTER to return to hx autobuild... && read pausa'")

        self.terminar() 

    def construirHX(self):

        print("Action requested by the user: construirHX\n")

        os.system("gnome-terminal -- bash -c 'echo hx autobuild && echo && echo You must enter your password to continue... && echo && sudo hx -i hx && echo && echo Press ENTER to return to hx autobuild... && read pausa'")

        self.terminar() 

    def limpar(self):

        print("Action requested by the user: limpar\n")

        os.system("hx -c")

        self.terminar()

    def execHX(self):

        print("Action requested by the user: execHX\n")

        os.system("hx -v hx")

        self.terminar()

    def terminar(self):

        print("Request completed.\n")

# 

janela=Tk()
autobuild=hxAutoBuild(janela)
janela.title('hx autobuild for Hexagonix H2 (v0.8)')
janela.geometry("500x400+10+10")
print("\nhx autobuild (Hexagonix H1-R6+)")
print("Copyright (C) 2022-2023 Felipe Miguel Nery Lunkes")
print("All rights reserved.")
print("\nWaiting for user interaction...")
janela.mainloop()
print("Ended by user.")