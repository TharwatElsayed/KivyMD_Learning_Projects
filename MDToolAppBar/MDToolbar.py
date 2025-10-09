from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.secondaryContainerColor

    MDTopAppBar:
        type: "small"
        size_hint_x: 1
        pos_hint: {"center_x": .5, "center_y": .95}

        MDTopAppBarLeadingButtonContainer:

            MDActionTopAppBarButton:
                icon: "arrow-left"

        MDTopAppBarTitle:
            text: "Mohamed & Mustafa App"

        MDTopAppBarTrailingButtonContainer:

            MDActionTopAppBarButton:
                icon: "attachment"

            MDActionTopAppBarButton:
                icon: "calendar"

            MDActionTopAppBarButton:
                icon: "dots-vertical"


    MDBottomAppBar:

        MDFabBottomAppBarButton:
            icon: "plus"
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


Example().run()