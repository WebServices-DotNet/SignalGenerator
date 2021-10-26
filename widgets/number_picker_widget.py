from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from widgets.spacer import Spacer


class NumberPickerWidget:

    def __init__(self, text, on_change, value, step):
        self.text = text
        self.on_change = on_change
        self.value = value
        self.step = step

    def build(self):
        content = GridLayout()
        content.cols = 2
        content.add_widget(Label(text=self.text))

        content.add_widget(NumberPicker(self.on_change, self.value, self.step).build())
        return content


class NumberPicker:

    def __init__(self, on_change, value, step):
        self.step = step
        self.on_change = on_change
        self.value = value
        self.label = Label(text=f"{self.value:.1f}")

    def build(self):
        content = GridLayout()
        content.cols = 3
        content.add_widget(Spacer())

        def callback1(instance):
            self.on_add()

        def callback2(instance):
            self.on_sub()

        content.add_widget(self.label)

        button_content = GridLayout()
        button_content.cols = 1

        btn1 = Button(text='+')
        btn1.bind(on_press=callback1)
        button_content.add_widget(btn1)

        btn2 = Button(text='-')
        btn2.bind(on_press=callback2)
        button_content.add_widget(btn2)

        content.add_widget(button_content)

        return content

    def on_add(self):
        self.value += self.step
        self.on_change(self.value)
        self.label.text = f"{self.value:.1f}"

    def on_sub(self):
        self.value -= self.step
        self.on_change(self.value)
        self.label.text = f"{self.value:.1f}"


