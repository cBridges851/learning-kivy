from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        # with self.canvas:
        #     Color(1, 0.4, 1, 1, mode="rgba")
        #     self.rect = Rectangle(pos=(0, 0), size=(100, 100))
        #     Color(0.5, 1, 1, 1, mode="rgba")


    # def on_touch_down(self, touch):
    #     print(f"Mouse down {touch}")
    #     # self.rect.pos = touch.pos

    # def on_touch_move(self, touch):
    #     print(f"Mouse moved {touch}")
    #     # self.rect.pos = touch.pos

    # def on_touch_up(self, touch):
    #     print(f"Mouse up {touch}")

class DrawingApp(App):
    def build(self):
        return Touch()

if __name__ == "__main__":
    DrawingApp().run()