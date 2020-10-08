from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
CONVERSION_NUMBER = 1.609

class ConvertMtoKMApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root

#    def handle_convert_press(self, user_input):
#        while True:
#            try:
#                self.root.ids.output_label.text = str((float(user_input) * CONVERSION_NUMBER))
#                break
#            except ValueError:
#                self.root.ids.output_label.text = "0.0"
#                return

    def constant_convert(self, user_input):
        while True:
            try:
                self.root.ids.output_label.text = str((float(user_input) * CONVERSION_NUMBER))
                break
            except ValueError:
                self.root.ids.output_label.text = "0.0"
                return

    def handle_increment(self, user_input, increment):
        while True:
            try:
                self.root.ids.user_input.text = str(int(user_input) + increment)
                break
            except ValueError:
                self.root.ids.user_input.text = str(0 + increment)
                return

ConvertMtoKMApp().run()