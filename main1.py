from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from os import walk

import requests
import json
from workoutbanner import WorkoutBanner


class HomeScreen(Screen):
    pass


class ImageButton(ButtonBehavior, Image):
    pass


class SettingsScreen(Screen):
    pass


class ChangeAvatarsScreen(Screen):
    pass


GUI = Builder.load_file("main1.kv")


class MainApp(App):
    my_friend_id= 1
    def build(self):
        return GUI

    def on_start(self):
        # Get database data
        result = requests.get("https://fitness-buddy-6813e-default-rtdb.firebaseio.com/"+ str(self.my_friend_id) + ".json")
        print("Was it ok?", result.ok)
        data= json.loads(result.content.decode())
        # Get and Update Avatar image
        avatar_image = self.root.ids['home_screen'].ids['avatar_image']
        avatar_image.source = "icons/" + data['avatar']

        # Populate avatar grid
        avatar_grid = self.root.ids['change_avatars_screen'].ids['avatar_grid']
        for root_dir, folders, files in walk("icons/avatars"):
            for f in files:
                img = ImageButton(source="icons/avatars/" + f, on_release=self.change_avatar)
                avatar_grid.add_widget(img)

        # Get update streak level
        streak_label= self.root.ids['home_screen'].ids['streak_label']
        streak_label.text = str(data['streak']) + " Day Streak!"

        banner_grid =self.root.ids['home_screen'].ids['banner_grid']
        workouts = data['workouts'][1:]
        for workout in workouts:
            for i in range(5):
                # Populate workout grid in home screen
                W = WorkoutBanner(workout_image=workout['workout_image'], description=workout['description'],
                                  type_image=workout['type_image'], number=workout['number'], units=workout['units'], likes=workout['likes'])
                banner_grid.add_widget(W)

    def change_avatar(self, *args):
        pass


    def change_screen(self, screen_name):
        # Get the screen manager from kv file
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name
        screen_manager.transition


MainApp().run()