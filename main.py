from kivy.config import Config
# Ekran boyutunu uygulama açılmadan sabitleyelim (En üste yazılmalı)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '700')
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import webbrowser

class SpaceMineHome(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Arka Plan
        self.add_widget(Image(source='pngtree-beautiful-space-background-picture-image_15376044_2.jpg', 
                              allow_stretch=True, keep_ratio=False))
        
        # Logo
        self.add_widget(Label(text='SpaceMine', font_size='40sp', bold=True,
                              color=(0, 0.8, 1, 1), pos_hint={'center_x': .5, 'center_y': .85}))
        
        # Arama Kutusu
        self.ti = TextInput(hint_text='Kesfe basla...', size_hint=(.7, .06),
                            pos_hint={'center_x': .5, 'center_y': .6}, multiline=False)
        self.add_widget(self.ti)
        
        # Git Butonu
        btn = Button(text='ARA', size_hint=(.3, .07), pos_hint={'center_x': .5, 'center_y': .5},
                     background_color=(0, 0.5, 1, 1))
        btn.bind(on_press=self.ara)
        self.add_widget(btn)

    def ara(self, instance):
        if self.ti.text:
            webbrowser.open(f"https://www.google.com/search?q={self.ti.text}")

class SpaceMine(App):
    def build(self):
        return SpaceMineHome()

if __name__ == '__main__':
    SpaceMine().run()