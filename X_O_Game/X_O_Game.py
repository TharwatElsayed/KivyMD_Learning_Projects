from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('X_O_Game.kv')
    
    turn = 'X'
    winner = False
    X_win = 0
    O_win = 0

    def drawn(self):
        if self.winner == False and \
        self.root.ids.btn1.disabled == True and \
        self.root.ids.btn2.disabled == True and \
        self.root.ids.btn3.disabled == True and \
        self.root.ids.btn4.disabled == True and \
        self.root.ids.btn5.disabled == True and \
        self.root.ids.btn6.disabled == True and \
        self.root.ids.btn7.disabled == True and \
        self.root.ids.btn8.disabled == True and \
        self.root.ids.btn9.disabled == True:
            self.root.ids.score.text=f'DRAWN'
            


    def end_game(self,x1,x2,x3):
        self.winner=True
        x1.color = "yellow"
        x2.color = "blue"
        x3.color = "red"
        self.dis_buttons()
        self.root.ids.score.text=f'{x1.text} Wins'

        if x1.text=="X":
            self.X_win = self.X_win+1
        else:
            self.O_win = self.O_win+1
        
        self.root.ids.game.text = f'X Wins: {self.X_win} | O Wins: {self.O_win}'
            

    def dis_buttons(self):
        self.root.ids.btn1.disabled = True
        self.root.ids.btn2.disabled = True
        self.root.ids.btn3.disabled = True
        self.root.ids.btn4.disabled = True
        self.root.ids.btn5.disabled = True
        self.root.ids.btn6.disabled = True
        self.root.ids.btn7.disabled = True
        self.root.ids.btn8.disabled = True
        self.root.ids.btn9.disabled = True

    def win(self):
        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn2.text and self.root.ids.btn2.text==self.root.ids.btn3.text:
            self.end_game(self.root.ids.btn1,self.root.ids.btn2,self.root.ids.btn3)

        if self.root.ids.btn4.text != "" and self.root.ids.btn4.text == self.root.ids.btn5.text and self.root.ids.btn5.text==self.root.ids.btn6.text:
            self.end_game(self.root.ids.btn4,self.root.ids.btn5,self.root.ids.btn6)

        if self.root.ids.btn7.text != "" and self.root.ids.btn7.text == self.root.ids.btn8.text and self.root.ids.btn8.text==self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn7,self.root.ids.btn8,self.root.ids.btn9)

        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn4.text and self.root.ids.btn4.text==self.root.ids.btn7.text:
            self.end_game(self.root.ids.btn1,self.root.ids.btn4,self.root.ids.btn7)

        if self.root.ids.btn2.text != "" and self.root.ids.btn2.text == self.root.ids.btn5.text and self.root.ids.btn5.text==self.root.ids.btn8.text:
            self.end_game(self.root.ids.btn2,self.root.ids.btn5,self.root.ids.btn8)

        if self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn6.text and self.root.ids.btn6.text==self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn3,self.root.ids.btn6,self.root.ids.btn9)

        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn5.text and self.root.ids.btn5.text==self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn1,self.root.ids.btn5,self.root.ids.btn9)

        if self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn5.text and self.root.ids.btn5.text==self.root.ids.btn7.text:
            self.end_game(self.root.ids.btn3,self.root.ids.btn5,self.root.ids.btn7)

        

    def press(self,btn):
        if self.turn == 'X':
            btn.text='X'
            btn.disabled = True
            self.root.ids.score.text="O's Turn"
            self.turn = "O"

        elif self.turn == 'O':
            btn.text='O'
            btn.disabled = True
            self.root.ids.score.text="X's Turn"
            self.turn = "X"

        self.win()
        self.drawn()
        
    def restart(self):
        self.turn = "X"
        self.root.ids.btn1.disabled = False
        self.root.ids.btn2.disabled = False
        self.root.ids.btn3.disabled = False
        self.root.ids.btn4.disabled = False
        self.root.ids.btn5.disabled = False
        self.root.ids.btn6.disabled = False
        self.root.ids.btn7.disabled = False
        self.root.ids.btn8.disabled = False
        self.root.ids.btn9.disabled = False
        self.root.ids.btn1.text = ""
        self.root.ids.btn2.text = ""
        self.root.ids.btn3.text = ""
        self.root.ids.btn4.text = ""
        self.root.ids.btn5.text = ""
        self.root.ids.btn6.text = ""
        self.root.ids.btn7.text = ""
        self.root.ids.btn8.text = ""
        self.root.ids.btn9.text = ""
        self.root.ids.score.text="X's Turn"
    
MainApp().run()