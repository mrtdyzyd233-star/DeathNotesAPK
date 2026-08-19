#Pydroid run kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):

    def build(self):

        main = GridLayout(cols=1)

        # شاشة الآلة الحاسبة
        self.screen = TextInput(
            text="",
            readonly=True,
            font_size=40
        )

        main.add_widget(self.screen)

        # أزرار الآلة الحاسبة
        buttons = GridLayout(cols=4)

        for number in ["7", "8", "9"]:
            button = Button(text=number)
            button.bind(on_press=self.add_number)
            buttons.add_widget(button)

        button = Button(text="/")
        button.bind(on_press=self.add_operation)
        buttons.add_widget(button)

        for number in ["4", "5", "6"]:
            button = Button(text=number)
            button.bind(on_press=self.add_number)
            buttons.add_widget(button)

        button = Button(text="*")
        button.bind(on_press=self.add_operation)
        buttons.add_widget(button)

        for number in ["1", "2", "3"]:
            button = Button(text=number)
            button.bind(on_press=self.add_number)
            buttons.add_widget(button)

        button = Button(text="-")
        button.bind(on_press=self.add_operation)
        buttons.add_widget(button)

        button = Button(text="0")
        button.bind(on_press=self.add_number)
        buttons.add_widget(button)

        button = Button(text="C")
        button.bind(on_press=self.clear)
        buttons.add_widget(button)

        button = Button(text="=")
        button.bind(on_press=self.calculate)
        buttons.add_widget(button)

        button = Button(text="+")
        button.bind(on_press=self.add_operation)
        buttons.add_widget(button)

        main.add_widget(buttons)

        return main

    # إضافة رقم للشاشة
    def add_number(self, button):
        self.screen.text += button.text

    # إضافة عملية حسابية
    def add_operation(self, button):
        self.screen.text += " " + button.text + " "

    # مسح الشاشة
    def clear(self, button):
        self.screen.text = ""

    # حساب النتيجة
    def calculate(self, button):
        try:
            result = eval(self.screen.text)
            self.screen.text = str(result)
        except:
            self.screen.text = "Error"


CalculatorApp().run()