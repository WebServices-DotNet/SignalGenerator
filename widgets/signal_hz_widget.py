from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from widgets.spacer import Spacer


class SignalHzWidget:

    def __init__(self, on_change):
        self.on_change = on_change

    def build(self):
        content = GridLayout()
        content.cols = 2
        content.add_widget(Label(text="Signal Hz"))
        content.add_widget(SignalPicker(self.on_change).build())
        return content


class SignalPicker:
    def __init__(self, on_change):
        self.on_change = on_change

    def build(self):
        content = GridLayout()
        content.cols = 3

        content.add_widget(Spacer())

        def callback(instance):
            self.on_change("test")

        btn1 = Button(text='--')
        btn1.bind(on_press=callback)
        content.add_widget(btn1)
        content.add_widget(Label(text="val"))

        return content
