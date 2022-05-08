from kivy.lang import Builder
from kivy.core.window import Window
import BuildFile

# Set the app size
Window.size = (800, 700)

# Designate Our .kv design file
Builder.load_file('design.kv')


if __name__ == '__main__':
    BuildFile.CalculatorApp().run()