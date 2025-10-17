from kivy.lang import Builder

from kivymd.app import MDApp


KV = '''
MDFloatLayout:

    MDCheckbox:
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_active: app.on_checkbox_active(*args)
        active: False
        color_active: "blue"
        color_inactive: "red"
    


    MDSwitch:
        pos_hint: {'center_x': .5, 'center_y': .4}
        #width: dp(45)
        active: False
        icon_active: "check"
        icon_inactive: "close"
        icon_active_color: "white"
        icon_inactive_color: "grey"

'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_checkbox_active(self, checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
        else:
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')

Test().run()