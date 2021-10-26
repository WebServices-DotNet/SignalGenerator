from kivy.uix.button import Button


class PrimaryButton:
    def __init__(self, text, on_change):
        self.on_change = on_change
        self.text = text

    def build(self):

        def callback(instance):
            self.on_change("test")

        btn1 = Button(text=self.text)
        btn1.bind(on_press=callback)

        return btn1
