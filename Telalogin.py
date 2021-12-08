#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Dec 06, 2021 10:12:55 PM -03  platform: Windows NT

import sys
from tkinter import Tk

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

class Toplevel1:
    def __init__(self):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.top = tk.Tk()
        self.top.geometry("724x613+422+114")
        self.top.minsize(120, 1)
        self.top.maxsize(1540, 845)
        self.top.resizable(1,  1)
        self.top.title("New Toplevel")
        self.top.configure(background="#000000")

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.249, rely=0.065, relheight=0.878
                , relwidth=0.508)
        self.Frame1.configure(relief='flat')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(cursor="fleur")

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.163, rely=0.112, height=20, relwidth=0.663)
        self.Entry1.configure(background="white")
        self.Entry1.configure(cursor="fleur")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(self.Frame1, show='*')
        self.Entry2.place(relx=0.163, rely=0.223, height=20, relwidth=0.663)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Button1 = tk.Button(self.Frame1, command=self.LoginBackEnd)
        self.Button1.place(relx=0.163, rely=0.409, height=54, width=257)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 15")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Login''')

        self.Button1_1 = tk.Button(self.Frame1, command=self.Cadastro)
        self.Button1_1.place(relx=0.163, rely=0.595, height=54, width=257)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#d9d9d9")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font="-family {Segoe UI} -size 15")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Cadastro''')

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.136, rely=0.037, height=31, width=84)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 13")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Usuario''')

        self.Label1_1 = tk.Label(self.Frame1)
        self.Label1_1.place(relx=0.136, rely=0.167, height=21, width=84)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Segoe UI} -size 13")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Senha''')
        self.top.mainloop()

    def Cadastro(self):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.root = tk.Tk()
        self.root.geometry("724x613+422+114")
        self.root.minsize(120, 1)
        self.root.maxsize(1540, 845)
        self.root.resizable(1,  1)
        self.root.title("Cadastro")
        self.root.configure(background="#000000")

        self.FrameCadastro = tk.Frame(self.root)
        self.FrameCadastro.place(relx=0.249, rely=0.065, relheight=0.878
                , relwidth=0.508)
        self.FrameCadastro.configure(relief='flat')
        self.FrameCadastro.configure(borderwidth="2")
        self.FrameCadastro.configure(background="#d9d9d9")
        self.FrameCadastro.configure(cursor="fleur")

        self.Entry1Cadastro = tk.Entry(self.FrameCadastro)
        self.Entry1Cadastro.place(relx=0.163, rely=0.112, height=20, relwidth=0.663)
        self.Entry1Cadastro.configure(background="white")
        self.Entry1Cadastro.configure(cursor="fleur")
        self.Entry1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Entry1Cadastro.configure(font="TkFixedFont")
        self.Entry1Cadastro.configure(foreground="#000000")
        self.Entry1Cadastro.configure(insertbackground="black")

        self.Entry2Cadastro = tk.Entry(self.FrameCadastro, show='*')
        self.Entry2Cadastro.place(relx=0.163, rely=0.223, height=20, relwidth=0.663)
        self.Entry2Cadastro.configure(background="white")
        self.Entry2Cadastro.configure(disabledforeground="#a3a3a3")
        self.Entry2Cadastro.configure(font="TkFixedFont")
        self.Entry2Cadastro.configure(foreground="#000000")
        self.Entry2Cadastro.configure(insertbackground="black")

        self.Button1Cadastro_1 = tk.Button(self.FrameCadastro, command=self.CadastrarBackEnd)
        self.Button1Cadastro_1.place(relx=0.163, rely=0.595, height=54, width=257)
        self.Button1Cadastro_1.configure(activebackground="#ececec")
        self.Button1Cadastro_1.configure(activeforeground="#000000")
        self.Button1Cadastro_1.configure(background="#d9d9d9")
        self.Button1Cadastro_1.configure(disabledforeground="#a3a3a3")
        self.Button1Cadastro_1.configure(font="-family {Segoe UI} -size 15")
        self.Button1Cadastro_1.configure(foreground="#000000")
        self.Button1Cadastro_1.configure(highlightbackground="#d9d9d9")
        self.Button1Cadastro_1.configure(highlightcolor="black")
        self.Button1Cadastro_1.configure(pady="0")
        self.Button1Cadastro_1.configure(text='''Cadastro''')

        self.Label1Cadastro = tk.Label(self.FrameCadastro)
        self.Label1Cadastro.place(relx=0.136, rely=0.037, height=31, width=84)
        self.Label1Cadastro.configure(background="#d9d9d9")
        self.Label1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro.configure(font="-family {Segoe UI} -size 13")
        self.Label1Cadastro.configure(foreground="#000000")
        self.Label1Cadastro.configure(text='''Usuario''')

        self.Label1Cadastro_1 = tk.Label(self.FrameCadastro)
        self.Label1Cadastro_1.place(relx=0.136, rely=0.167, height=21, width=84)
        self.Label1Cadastro_1.configure(activebackground="#f9f9f9")
        self.Label1Cadastro_1.configure(activeforeground="black")
        self.Label1Cadastro_1.configure(background="#d9d9d9")
        self.Label1Cadastro_1.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro_1.configure(font="-family {Segoe UI} -size 13")
        self.Label1Cadastro_1.configure(foreground="#000000")
        self.Label1Cadastro_1.configure(highlightbackground="#d9d9d9")
        self.Label1Cadastro_1.configure(highlightcolor="black")
        self.Label1Cadastro_1.configure(text='''Senha''')
        self.root.mainloop()

    def CadastrarBackEnd(self):
        try:
            with open('usuarios.txt', 'a') as arquivoUsuario:
                arquivoUsuario.write(self.Entry1Cadastro.get() + '\n')

            with open('senhas.txt', 'a') as arquivoUsuario:
                arquivoUsuario.write(self.Entry2Cadastro.get() + '\n')
            self.root.destroy()
        except:
            print('Houve um erro')

    def LoginBackEnd(self):
        with open('usuarios.txt', 'r') as arquivoUsuario:
            usuarios = arquivoUsuario.readlines()
        
        with open('senhas.txt', 'r') as arquivoUsuario:
            senhas = arquivoUsuario.readlines()

        usuarios = list(map(lambda x: x.replace('\n', ''), usuarios))
        senhas = list(map(lambda x: x.replace('\n', ''), senhas))

        usuario = self.Entry1.get()
        senha = self.Entry2.get()

        logado = False

        for i in range(len(usuarios)):
            if usuario == usuarios[i] and senha == senhas[i]:
                print('Usuario Logado')
                self.top.destroy()
                logado = True
        if not logado:
            print('Usuario ou senha incorreto')
            self.top.destroy()
Toplevel1()


