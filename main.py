import time

import kivy
from kivy.app import App

from generator.generator import GeneratorManager
from screen.main_page import MainPage


class MyFirstKivyApp(App):
    def build(self):
        return MainPage()


def test():
    generator = GeneratorManager()
    generator.numberOfCars = 100
    generator.on_start()
    while True:
        time.sleep(0.1)
        pass

if __name__ == "__main__":
    test()
    # MyFirstKivyApp().run()