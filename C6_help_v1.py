from tkinter import *
from functools import partial  # to prevent unwanted windows
import csv
import random


class ChooseRounds:

    def __init__(self):
        # invoke play class with three rounds for testing purposes.
        self.to_play(3)

    def to_play(self, num_rounds):
        Play(num_rounds)

        # hide root window (ie: hide rounds chose window)
        root.withdraw()


class Play:

    def __init__(self, how_many):
        self.play_box = Toplevel()

        self.quest_frame = Frame(self.play_box, pady=10, padx=10)
        self.quest_frame.grid()

        self.control_frame = Frame(self.quest_frame)
        self.control_frame.grid(row=6)

        control_buttons = [
            ["#CC6600", "Help", "get help"], ["#004C99", "Statistics", "get stats"],
            ["#808080", "Start Over", "start over"]
        ]

        # list to hold references for control buttons so that
        # the text of the 'start over' button can easily be
        # configured when the game is over
        self.control_button_ref = []

        for item in range(0, 3):
            self.make_control_button = Button(self.control_frame, fg="#FFFFFF", bg=control_buttons[item][0],
                                              text=control_buttons[item][1], width=11, font=("Arial", "16", "bold"),
                                              command=lambda i=item: self.to_do(control_buttons[i][2]))
            self.make_control_button.grid(row=0, column=item, pady=5, padx=5)

            # add buttons to control list
            self.control_button_ref.append(self.make_control_button)

            self.to_help_btn = self.control_button_ref[0]

    # detects which 'control' button was pressed and
    # invokes necessary function. Can possibly replace functions with
    # calls to classes in this section!
    def to_do(self, action):
        if action == "get help":
            DisplayHelp(self)
        elif action == "get stats":
            pass
        else:
            self.close_play()

    # DONT USE THIS FUNCTION IN BASE AS IT KILLS THE ROOT
    def close_play(self):
        root.destroy()


class DisplayHelp:

    def __init__(self, partner):
        # setup dialogue box and bg colour
        background = "#ffe6cc"
        self.help_box = partner
        self.help_box = Toplevel()

        # disable help button
        partner.to_help_btn.config(state=DISABLED)

        # if users press cross at top, closes help and
        # 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))
        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg=background, text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "Your goal in this game is to beat the computer and you have an advantage - you get to choose " \
                    "your colour first. The points associated with the colours are based on the colour's hex code. \n" \
                    "The higher the value of the colour, the greater your score. To see your statistics, click on " \
                    "the 'Statistics' button. \n\n Win the game by scoring more than the computer overall. Don't be " \
                    "discouraged if you don't win every round, it's your overall score that counts. \n\n " \
                    "Good luck! Choose carefully"
        self.help_text_label = Label(self.help_frame, bg=background, text=help_text, wrap=350, justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame, font=("Arial", "12", "bold"), text="Dismiss",
                                     bg="#CC6600", fg="#FFFFFF", command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    # closes help dialogue (used by button and x at top of dialogue)
    def close_help(self, partner):
        # put help button back to normal...
        partner.to_help_btn.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    ChooseRounds()
    root.mainloop()
