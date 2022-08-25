import kivy
from playsound import playsound
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.button import Button
class Holodilnik(App):
    def build(self):
        btn = Button(text="Нажми чтобы поговорить с Гелей !",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(8, 8),
                     size_hint=(.4, .4),
                     pos=(300, 250))
        btn.bind(on_press=self.callback)
        return btn
    def callback(self, event):
        print("аа?")
        playsound('play.mp3')
root = Holodilnik()
root.run()
