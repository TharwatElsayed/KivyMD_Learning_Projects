from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText

KV = '''
Button:
    text: "Show Snackbar"
    on_release: app.show_popup()
'''

class Example(MDApp):
    def show_popup(self):
        snackbar = MDSnackbar(
            MDSnackbarText(
                text="This is a Snackbar message"
            ),
            y=20,  # optional: distance from bottom
        )
        snackbar.open()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

Example().run()
