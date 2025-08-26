from kivy.app import App
from kivy.uix.label import Label

class HealthApp(App):
    def build(self):
        return Label(text="سلام! اپلیکیشن سلامت")

if __name__ == "__main__":
    HealthApp().run()
