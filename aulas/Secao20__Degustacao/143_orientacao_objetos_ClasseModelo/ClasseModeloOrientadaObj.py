# coding: utf-8

# Códigos padrão utilizado em todas as classes App
from kivy.app import App
from kivy.uix.label import Label


class MeuProgra(App):

    def build(self):
        return Label()


MeuProgra().run()
