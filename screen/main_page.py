from kivy.uix.gridlayout import GridLayout

from generator.generator import GeneratorManager
from widgets.button import PrimaryButton
from widgets.cars_number_widget import CarsNumberWidget
from widgets.signal_hz_widget import SignalHzWidget
from widgets.spacer import Spacer


class MainPage(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.generator = GeneratorManager()

        self.cols = 1
        self.add_widget(CarsNumberWidget(self.on_car_number_change).build())
        self.add_widget(SignalHzWidget(self.on_hz_change).build())
        self.add_widget(Spacer())
        self.add_widget(PrimaryButton("start", self.on_start).build())
        self.add_widget(PrimaryButton("stop", self.on_stop).build())

    def on_car_number_change(self, value):
        self.generator.on_car_number_change(value)

    def on_hz_change(self, value):
        self.generator.on_hz_change(value)

    def on_start(self, value):
        self.generator.on_start()

    def on_stop(self, value):
        self.generator.on_stop()