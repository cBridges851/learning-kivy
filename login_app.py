# This is a practice app based on what I have learnt up to the float layout video

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Interface(Widget):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def login(self):
        if self.username.text == "Christa" and self.password.text == "banana":
            print("Login Successful")
        else:
            print("Incorrect username or password")

        self.username.text = ""
        self.password.text = ""

class LoginApp(App):
    def build(self):
        return Interface()

if __name__ == "__main__":
    LoginApp().run()