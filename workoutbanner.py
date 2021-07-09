import kivy.utils
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
import kivy.utils


class WorkoutBanner(GridLayout):
    rows = 1

    def __init__(self, **kwargs):
        super(WorkoutBanner, self).__init__()
        with self.canvas.before:
            Color(rgb=(kivy.utils.get_color_from_hex("#676976")))
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)

        # Left Float layout
        left = FloatLayout()
        left_image = Image(source= "icons/" + kwargs['workout_image'], size_hint=(1, 0.8), pos_hint= {"top": 1, "right": 1})
        left_label = Label(text=kwargs['description'], size_hint=(1, .2), pos_hint={"top": .2, "right":1})
        left.add_widget(left_image)
        left.add_widget(left_label)

        # Middle Float layout
        middle = FloatLayout()
        middle_image = Image(source="icons/" + kwargs['type_image'], size_hint=(1, 0.8), pos_hint={"top": 1, "right": 1})
        middle_label = Label(text=str(kwargs['number']) + " " + str(kwargs['units']), size_hint=(1, .2), pos_hint={"top": .2, "right": 1})
        middle.add_widget(middle_image)
        middle.add_widget(middle_label)

        # Right Float Layout
        right = FloatLayout()
        right_image = Image(source="icons/Handshake.png",size_hint=(1, 0.8), pos_hint={"top": 1, "right": 1})
        right_label = Label(text=str(kwargs['likes']) + " Handshakes", size_hint=(1, .2), pos_hint={"top": .2, "right": 1})
        right.add_widget(right_image)
        right.add_widget(right_label)

        self.add_widget(left)
        self.add_widget(middle)
        self.add_widget(right)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size