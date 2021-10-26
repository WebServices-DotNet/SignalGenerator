from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from generator.generator import GeneratorManager
from widgets.button import PrimaryButton
from widgets.number_picker_widget import NumberPickerWidget
from widgets.signal_hz_widget import SignalHzWidget
from widgets.spacer import Spacer


class MainPage(GridLayout):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.generator = GeneratorManager()
        self.is_running = False

        self.cols = 1
        self.add_widget(NumberPickerWidget("Cars number:", self.on_car_number_change, self.generator.numberOfCars, 1).build())
        self.add_widget(NumberPickerWidget("Signal Hz:", self.on_hz_change, self.generator.hz, 0.1).build())

        self.state_label = Label()

        self.add_widget(self.state_label)
        self._update_state_label()

        self.add_widget(PrimaryButton("start", self.on_start).build())
        self.add_widget(PrimaryButton("stop", self.on_stop).build())

    def _update_state_label(self):
        self.state_label.text = \
            "Running: " + str(self.is_running) + "  |  " + \
            "Hz: " + f"{self.generator.hz*60.0:.1f}" + " per minute (per car)" + "  |  " + \
            "Hz: " + f"{self.generator.hz * self.generator.numberOfCars:.1f}" + " per seconds (all)" + "  |  " + \
            "Cars: " + f"{self.generator.numberOfCars:.1f}"

    def on_car_number_change(self, value):
        self.generator.on_car_number_change(value)
        self._update_state_label()

    def on_hz_change(self, value):
        self.generator.on_hz_change(value)
        self._update_state_label()

    def on_start(self, value):
        self.is_running = True
        self.generator.on_start()
        self._update_state_label()

    def on_stop(self, value):
        self.is_running = False
        self.generator.on_stop()
        self._update_state_label()