# coding: utf-8

import kivy

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.button import Button


class KVvsPY(App):
    def build(self):
        return Button(text="Teste")


janela = KVvsPY()
janela.run()
