from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
import webbrowser
import subprocess

class MasterApp(App):
def build(self):
self.title = "Stolyarnaya Masterskaya Rasseya"
Window.size = (400, 600)
Window.clearcolor = (0.9, 0.8, 0.7, 1)