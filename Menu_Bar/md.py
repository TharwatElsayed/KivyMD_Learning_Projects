from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    def build(self):

        self.theme_cls.theme_style ="Light"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file("tst.kv")
    
    def presser(self):
        self.root.ids.mylabel.text = "FAB Clicked!"
       
MainApp().run()