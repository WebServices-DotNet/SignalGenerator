import kivy
from kivy.app import App

from screen.main_page import MainPage


class MyFirstKivyApp(App):
    def build(self):
        return MainPage()


if __name__ == "__main__":
    MyFirstKivyApp().run()