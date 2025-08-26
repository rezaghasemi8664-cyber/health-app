
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import socket
import json
import numpy as np
import time

class HealthApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='سلام! اپلیکیشن سلامت')
        self.btn = Button(text='شروع مانیتورینگ')
        layout.add_widget(self.label)
        layout.add_widget(self.btn)
        return layout

if __name__ == '__main__':
    HealthApp().run()
