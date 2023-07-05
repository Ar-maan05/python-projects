import kivy
from kivy.app import App
from kivy.lang import Builder

KV = '''
GridLayout
    display: entry
    rows: 5
    padding: 10
    spcaing: 20
    BoxLayout:
        TextInput:
            id: entry
            font_size: 32
    BoxLayout:
        spacing: 10
        Button:
            text: "7"
            on_press: entry.text += self.text
        Button:
            text: "8"
            on_press: entry.text += self.text
        Button:
            text: "9"
            on_press: entry.text += self.text
        Button:
            text: "+"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 10
        Button:
            text: "4"
            on_press: entry.text += self.text
        Button:
            text: "5"
            on_press: entry.text += self.text
        Button:
            text: "6"
            on_press: entry.text += self.text
        Button:
            text: "-"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 10
        Button:
            text: "1"
            on_press: entry.text += self.text
        Button:
            text: "2"
            on_press: entry.text += self.text
        Button:
            text: "3"
            on_press: entry.text += self.text
        Button:
            text: "*"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 10
        Button:
            text: "AC"
            on_press: entry.text = ""
        Button:
            text: "0"
            on_press: entry.text += self.text
        Button:
            text: "="
            on_press: app.calc(entry.text)
        Button:
            text: "/"
            on_press: entry.text += self.text
'''

class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

    def calc(self, form):
        self.root.display.text = str(eval(form))

MyApp().run()