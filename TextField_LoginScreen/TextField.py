from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:
    md_bg_color: app.theme_cls.backgroundColor

    MDTextField:
        mode: "outlined"
        size_hint_x: None
        width: "240dp"
        pos_hint: {"center_x": .5, "center_y": .7}

        MDTextFieldLeadingIcon:
            icon: "account"

        MDTextFieldHintText:
            text: "User Name"

        MDTextFieldHelperText:
            text: "Enter User Name"
            mode: "persistent"

        MDTextFieldTrailingIcon:
            icon: "information"

        MDTextFieldMaxLengthText:
            max_text_length: 10

    MDTextField:
        mode: "outlined"
        size_hint_x: None
        width: "240dp"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDTextFieldLeadingIcon:
            icon: "password"

        MDTextFieldHintText:
            text: "Password"

        MDTextFieldHelperText:
            text: "Enter Password"
            mode: "persistent"

        MDTextFieldTrailingIcon:
            icon: "information"

        MDTextFieldMaxLengthText:
            max_text_length: 10
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Olive"
        return Builder.load_string(KV)


Example().run()