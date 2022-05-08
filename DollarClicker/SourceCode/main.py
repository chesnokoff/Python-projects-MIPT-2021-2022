from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from threading import Thread
from time import sleep

# Set the app size
Window.size = (800, 700)

# Designate Our .kv design file
Builder.load_file('design.kv')


class MyLayout(Widget):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.helper_work = False
        self.additional_value = 0

    #Нажатие пробела
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    # Нажатие пробела
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'spacebar':
            self.add_to_total_scores(0.000001)
        return True

    def get_total_score(self):
        score_string = self.ids.scores.text
        score_string = score_string[:-1]
        total = float(score_string)
        return total

    def set_total_scores(self, new_total_scores):
        self.ids.scores.text = f'{new_total_scores:.6f}$'

    def add_to_total_scores(self, add):
        self.set_total_scores(self.get_total_score() + add)

    #Обработка главной кнопки
    def click(self):
        self.add_to_total_scores(1)

    # Создает новый поток для купленного кликера если потока до этого не было
    def start_adding_additional_value(self):
        if not self.helper_work:
            self.helper_work = True
            command = Thread(target=self.start_generating)
            # set daemon to true so the thread dies when app is closed
            command.daemon = True
            # start the thread
            command.start()

    #Выполняет работу купленных кликеров
    def start_generating(self):
        while True:
            self.add_to_total_scores(self.additional_value)
            sleep(1)

    def weak_creator_clicked(self):
        if self.get_total_score() >= 0:
            self.additional_value += 0.000005
            self.start_adding_additional_value()
            self.ids.weak_creator.background_color = 'green'

    def middle_creator_clicked(self):
        if self.get_total_score() >= 4:
            self.add_to_total_scores(-4)
            self.additional_value += 0.0005
            self.start_adding_additional_value()
            self.ids.middle_creator.background_color = 'green'

    def hard_creator_clicked(self):
        if self.get_total_score() >= 50:
            self.add_to_total_scores(-50)
            self.additional_value += 1
            self.start_adding_additional_value()
            self.ids.hard_creator.background_color = 'green'


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()