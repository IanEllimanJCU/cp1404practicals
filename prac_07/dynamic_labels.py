from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.fruit_list = ["apple", "banana", "pear"]

    def build(self):
        self.title = "Dynamic Labels App"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for fruit in self.fruit_list:
            temp_label = Label(text=fruit)
            self.root.ids.entries_box.add_widget(temp_label)

DynamicLabelsApp().run()