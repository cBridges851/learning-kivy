from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
import kivy
class Widgets(Widget):
    def btn(self):
        show_popup()

class ChrispyPopup(FloatLayout):
    pass

class PopupApp(App):
    def build(self):
        return Widgets()

def show_popup():
    show = ChrispyPopup()

    popup_window = Popup(title="This is a Popup", content=show, size_hint=(None, None), size=(400,400))
    popup_window.open()

if __name__ == "__main__":
    PopupApp().run()