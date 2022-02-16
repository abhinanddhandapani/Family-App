# MIT License
# Copyright (c) 2022 Abhinand Dhandapani

# This app is mainly build for Dhandapani Family, Please Use this as template.
# This app is fully being a personalised one.

# Warning It's not 100% a clean code, It's not efficient one.
# Thank You - kivy, kivymd, python devs, all my well-wishers.

import kivy
import kivymd
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.app import MDApp

class Homescreen(Screen):
    pass

class Windowmanager(ScreenManager):
    pass

class FamilyApp(MDApp):
    def build(self):
        kv = Builder.load_file('familia.kv')
        self.theme_cls.theme_style = "Dark" # Currently in Dark Mode only
        return kv

if __name__ == '__main__':
    FamilyApp().run()