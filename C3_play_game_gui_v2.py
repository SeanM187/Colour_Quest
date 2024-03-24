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

        # if users press cross at top, closes help and 'releases' help button
        self.play_box.protocol('WM_DELETE_WINDOW', partial(self.close_play))

        # variables used to work out statistics, when game ends etc
        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)

        # initially set rounds played and rounds won to 0
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        self.rounds_won = IntVar()
        self.rounds_won.set(0)

        # lists to hold user score/s and computer score/s
        # used to work out statistics

        user_scores = []
        computer_scores = []

        # get all the colours for use in game
        self.all_colours = self.get_all_colours()

        self.quest_frame = Frame(self.play_box, pady=10, padx=10)
        self.quest_frame.grid()

        rounds_heading = "Choose - Round 1 of {}".format(how_many)
        self.choose_heading = Label(self.quest_frame, text=rounds_heading, font=("Arial", "16", "bold"))
        self.choose_heading.grid(row=0)

        instructions = "Choose one of the colours below. When you choose"
        self.instructions_label = Label(self.quest_frame, text=instructions, wraplength=350, justify="left")
        self.instructions_label.grid(row=1)

        # get colour buttons for first round...
        self.button_colours_list = []

        # create colour buttons (in choice_frame)
        self.choice_frame = Frame(self.quest_frame)
        self.choice_frame.grid(row=2)

        # list to hold references for coloured buttons
        # so that they can be configured for new rounds etc
        self.choice_button_ref = []

        for item in range(0, 6):
            self.choice_button = Button(self.choice_frame, width=15,
                                        command=lambda i=item: self.to_compare(self.button_colours_list[i]))
            self.choice_button_ref.append(self.choice_button)
            self.choice_button.grid(row=item // 3, column=item % 3, padx=5, pady=5)

        # display computer choice (after user has chosen a colour)
        self.comp_choice_label = Label(self.quest_frame, text="Computer Choice will appear here",
                                       bg="#C0C0C0", width=51)
        self.comp_choice_label.grid(row=3, pady=10)

        # frame to include round result and next button
        self.rounds_frame = Frame(self.quest_frame)
        self.rounds_frame.grid(row=4, pady=5
                               )
        self.round_result_label = Label(self.rounds_frame, text="Round 1: User: - \t  Computer: - ", width=32,
                                        bg="#FFF2CC", font=("Arial", 10), pady=5)
        self.round_result_label.grid(row=0, column=0, padx=5)

        self.nex_button = Button(self.rounds_frame, text="Next Round", fg="#FFFFFF", bg="#008BFC",
                                 font=("Arial", 11, "bold"), width=10, state=DISABLED)
        self.nex_button.grid(row=0, column=1)

        # at start, get 'new round'
        self.new_round()

        # large label to show overall game results
        self.game_results_label = Label(self.quest_frame, text="Game Totals: User: - \t Computer: -", bg="#FFF2CC",
                                        padx=10, pady=10, font=("Arial", "10"), width=42)
        self.game_results_label.grid(row=5, pady=5)

        self.control_frame = Frame(self.quest_frame)
        self.control_frame.grid(row=6)

        control_buttons = [
            ["#CC6600", "Help", "get help"], ["#004C99", "Statistics", "get stats"],
            ["#808080", "Start Over", "start over"]
        ]

        for item in range(0, 3):
            self.make_control_button = Button(self.control_frame, fg="#FFFFFF", bg=control_buttons[item][0],
                                              text=control_buttons[item][1], width=11, font=("Arial", "16", "bold"),
                                              command=lambda i=item: self.to_do(control_buttons[i][2]))
            self.make_control_button.grid(row=0, column=item, pady=5, padx=5)

    # retrieve colours from csv file
    def get_all_colours(self):
        file = open("00_colour_list_hex_v3.csv", "r")
        var_all_colours = list(csv.reader(file, delimiter=","))
        file.close()

        # removes first entry in list (ie: the header row)
        var_all_colours.pop(0)
        return var_all_colours

    # randomly choose six colours for buttons
    def get_round_colours(self):
        round_colour_list = []
        color_scores = []

        # get six unique colours
        while len(round_colour_list) < 6:
            # choose item
            chosen_colour = random.choice(self.all_colours)
            index_chosen = self.all_colours.index(chosen_colour)

            # check score is not already in list
            if chosen_colour[1] not in color_scores:
                # add item to rounds list
                round_colour_list.append(chosen_colour)
                color_scores.append(chosen_colour[1])

                # remove item from master list
                self.all_colours.pop(index_chosen)

        return round_colour_list

    # work out who won and if the game is over
    # update win / loss lable and buttons
    def to_compare(self, user_score):
        print("Your score is", user_score)

    def new_round(self):


    # detects which 'control' button was pressed and
    # invokes necessary function. Can possible replace functions with
    # calls to classes in this section!
    def to_do(self, action):
        if action == "get help":
            self.get_help()
        elif action == "get stats":
            self.get_stats()
        else:
            self.close_play()

    def get_stats(self):
        print("You chose to get the statistics")

    def get_help(self):
        print("You chose to get the help")

    # DONT USE THIS FUNCTION IN BASE AS IT KILLS THE ROOT
    def close_play(self):
        root.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    ChooseRounds()
    root.mainloop()
