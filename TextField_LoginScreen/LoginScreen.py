from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.button import MDButton, MDButtonText

KV = '''
MDScreen:
    md_bg_color: app.theme_cls.backgroundColor

    MDTextField:
        id: username_field
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
        id: password_field
        mode: "outlined"
        password: True
        size_hint_x: None
        width: "240dp"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDTextFieldLeadingIcon:
            icon: "lock"

        MDTextFieldHintText:
            text: "Password"

        MDTextFieldHelperText:
            text: "Enter Password"
            mode: "persistent"

        MDTextFieldTrailingIcon:
            icon: "information"

        MDTextFieldMaxLengthText:
            max_text_length: 10

    MDButton:
        style: "filled"
        pos_hint: {"center_x": .5, "center_y": .35}
        on_release: app.find_requirements()
        MDButtonText:
            text: "Login"
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Olive"
        return Builder.load_string(KV)

    def find_requirements(self):
        """Retrieve username and password from text fields."""
        username = self.root.ids.username_field.text
        password = self.root.ids.password_field.text

        if not username or not password:
            MDSnackbar(
                MDButton(
                    MDButtonText(text="Please enter both username and password")
                ),
                duration=2,
            ).open()
        else:
            MDSnackbar(
                MDButton(
                    MDButtonText(text=f"Username: {username} | Password: {password}")
                ),
                duration=2,
            ).open()


Example().run()
