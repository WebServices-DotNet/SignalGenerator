import time
import kivy
from kivy.app import App
import sys
from generator.generator import GeneratorManager
from screen.main_page import MainPage


class MyFirstKivyApp(App):
    def build(self):
        return MainPage()


def start(number_of_cars):
    generator = GeneratorManager()
    generator.numberOfCars = number_of_cars
    generator.on_start()
    while True:
        time.sleep(0.1)
        pass


if __name__ == "__main__":

    try:
        cars = int(sys.argv[1])
    except:
        cars = 1

    start(cars)

    # MyFirstKivyApp().run()