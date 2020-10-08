from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty


class ClockDemo(App):
    message = StringProperty()

    def __init__(self, **kwargs):
        super(ClockDemo, self).__init__(**kwargs)
        self.counter = 0
        Window.size = (500, 200)
        self.clock_event = None

    def build(self):
        self.root = Builder.load_file('clock_demo2.kv')
        return self.root

    def update(self, seconds):
        self.message = 'counter {:2} dt {:20}'.format(self.counter, seconds)
        self.counter += 1

    def start(self):
        self.stop()
        self.clock_event = Clock.schedule_interval(self.update, 0.5)

    def stop(self):
        if self.clock_event:
            self.clock_event.cancel()


ClockDemo().run()
