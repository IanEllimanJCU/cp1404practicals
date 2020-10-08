from kivy.app import App
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.uix.widget import Widget


class BasicGraphicsDemo(App):
    def build(self):
        self.root = Widget()

        # white rectangle 100x100
        self.root.canvas.add(Color(1, 1, 1, 1))
        self.root.canvas.add(Rectangle(size=(100, 100)))

        # blue circle 50x50
        self.root.canvas.add(Color(0, 0, 1, 1))
        self.root.canvas.add(Ellipse(size=(50, 50), pos=(50, 50)))
        return self.root


BasicGraphicsDemo().run()
