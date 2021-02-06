from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.core.window import Window
from kivy.graphics import Line

Window.clearcolor = (1, 1, 1, 1)

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        is_pen_down = False
        with self.canvas:
            Color(0, 0, 0, 1, mode="rgba")
            self.line = Line(points=())


    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 0, 0, 1, mode="rgba")
            self.line = Line(points=())

    def on_touch_move(self, touch):
        print(f"Mouse moved {touch}")
        self.line.points.append(touch.pos[0])
        self.line.points.append(touch.pos[1])
        print(self.line.points)
        with self.canvas:
            Color(0, 0, 0, 1, mode="rgba")
            self.line = Line(points=self.line.points)
        # self.rect.pos = touch.pos

    # def on_touch_up(self, touch):
    #     print(f"Mouse up {touch}")

class DrawingApp(App):
    def build(self):
        return Touch()

if __name__ == "__main__":
    DrawingApp().run()