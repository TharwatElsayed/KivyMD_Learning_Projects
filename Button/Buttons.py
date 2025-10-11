from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:
    md_bg_color: app.theme_cls.surfaceColor

    MDButton:
        style: "elevated"
        pos_hint: {"center_x": .5, "center_y":.1}

        MDButtonIcon:
            icon: "plus"

        MDButtonText:
            text: "Elevated"

    MDButton:
        style: "filled"
        pos_hint: {"center_x": .5, "center_y":.2}
        MDButtonText:
            text: "Filled"
    MDButton:
        style: "tonal"
        pos_hint: {"center_x": .5, "center_y":.3}
        MDButtonText:
            text: "tonal"
    MDButton:
        style: "outlined"
        pos_hint: {"center_x": .5, "center_y":.4}
        MDButtonText:
            text: "outlined"
    MDButton:
        style: "text"
        pos_hint: {"center_x": .5, "center_y":.5}
        MDButtonText:
            text: "text"

    MDButton:
        style: "tonal"
        pos_hint: {"center_x": .3, "center_y":.6}
        theme_width: "Custom"
        height: "56dp"
        size_hint_x: .5

        MDButtonIcon:
            x: text.x - (self.width + dp(10))
            icon: "plus"

        MDButtonText:
            id: text
            text: "Tonal"
            pos_hint: {"center_x": .5, "center_y": .5}

    MDButton:
        style: "filled"
        pos_hint: {"center_x": .65, "center_y":.6}
        MDButtonIcon:
            icon: "plus"
        MDButtonText:
            text: "Filled"
            font_style: "Title"

    MDButton:
        style: "elevated"
        pos_hint: {"center_x": .83, "center_y":.6}
        theme_shadow_color: "Custom"
        shadow_color: "red"
        MDButtonIcon:
            icon: "plus"
            theme_icon_color: "Custom"
            icon_color: "green"
        MDButtonText:
            text: "Elevated"
            theme_text_color: "Custom"
            text_color: "red"

    MDIconButton:
        icon: "heart-outline"
        pos_hint: {"center_x": .05, "center_y":.7}
        style: "standard"

    MDIconButton:
        icon: "heart-outline"
        pos_hint: {"center_x": .15, "center_y":.7}
        style: "filled"

    MDIconButton:
        icon: "heart-outline"
        pos_hint: {"center_x": .25, "center_y":.7}
        style: "tonal"

    MDIconButton:
        icon: "heart-outline"
        pos_hint: {"center_x": .35, "center_y":.7}
        style: "outlined"

    MDIconButton:
        icon: "heart-outline"
        pos_hint: {"center_x": .45, "center_y":.7}
        style: "tonal"
        theme_font_size: "Custom"
        font_size: "48sp"
        radius: [self.height / 2, ]
        size_hint: None, None
        size: "84dp", "84dp"

    MDIconButton:
        icon: "heart-outline"
        style: "tonal"
        pos_hint: {"center_x": .55, "center_y":.7}
        theme_bg_color: "Custom"
        md_bg_color: "brown"
        theme_icon_color: "Custom"
        icon_color: "white"

    MDIconButton:
        icon: "pencil-outline"
        pos_hint: {"center_x": .65, "center_y":.7}
        style: "standard"

'''


class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)


Example().run()