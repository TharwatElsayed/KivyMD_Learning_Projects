from kivy.lang.builder import Builder
from kivymd.app import MDApp

kv = '''
<MySwiper@MDSwiperItem>:
    source: ""
    FitImage:
        source: root.source
        radius: [dp(20),]

MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDSwiper:
        size_hint_y: None
        height: root.height - dp(40)
        y: root.height - self.height - dp(20)

        MySwiper:
            source: "img1.jpg"
        MySwiper:
            source: "image.png"
        MySwiper:
            source: "img1.jpg"
        MySwiper:
            source: "image.png"
        MySwiper:
            source: "img1.jpg"
'''
class Main(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(kv)

Main().run()
