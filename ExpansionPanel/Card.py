from kivy.uix.bubble import Image
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

KV = '''
FloatLayout:
    MDCard:
        size_hint: None, None
        pos: '250dp','250dp'
        elevation:6
        Image:
            source:"cat.png"
    MDCard:
        size_hint: None, None
        pos: '400dp','250dp'
        elevation:12
        Image:
            source:"cat.png"
            allow_stretch: True
            keep_ratio: False
'''

class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)

Example().run()