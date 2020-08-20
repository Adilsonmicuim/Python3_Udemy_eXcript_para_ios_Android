# coding: utf-8

# Códigos padrão utilizado em todas as classes App
from kivy.app import App
from kivy.uix.label import Label

def build():
    # pass
    return Label()

janela = App()
janela.build = build
janela.run()
