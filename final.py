"""
************************************************************************************************************************
*                                                                                                                      *
*   Program: final                                                                                                     *
*                                                                                                                      *
*   Definition: This program will allow the user to roll as many dice                                                  *
*               as they want and output their sum                                                                      *
*                                                                                                                      *
*   Author: Patrick Crowley                                                                                            *
*                                                                                                                      *
*   Date: 4/26/19                                                                                                      *
*                                                                                                                      *
*   History: [4/23/19] Document created and modified                                                                   *
*            [4/24/19] Document modified                                                                               *
*            [4/25/19] Document modified and tested                                                                    *
*            [4/26/19] Document modified, tested and finished                                                          *
*                                                                                                                      *
*                                                                                                                      *
************************************************************************************************************************
"""
# ====================================================== IMPORTS =======================================================
import tkinter
import random

# ===================================================== BEGIN CODE =====================================================


# Class that holds the data for the GUI
class Rolltk(tkinter.Tk):
    # ""Constructor"" that initiates the GUI
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    # ==================================================================================================================
    #
    #   Function: initialize
    #
    #   Definition: This function contains all of the graphic aspects of the software
    #
    #   Author: Patrick Crowley
    #
    #   Date: 4/23/19
    #
    #   History: [4/23/19] Function created and modified
    #            [4/24/19] Function tested and modified
    #            [4/25/19] unction tested and modified
    #            [4/26/19] Function tested, modified and finished
    #
    # ==================================================================================================================

    def initialize(self):

        # ================================================= ARRAYS =====================================================
        self.images = [tkinter.PhotoImage(file="images/die1.png"), tkinter.PhotoImage(file="images/die2.png"),
                       tkinter.PhotoImage(file="images/die3.png"), tkinter.PhotoImage(file="images/die4.png"),
                       tkinter.PhotoImage(file="images/die5.png"), tkinter.PhotoImage(file="images/die6.png")]

        self.resize = [self.images[0].subsample(6, 6), self.images[1].subsample(6, 6), self.images[2].subsample(6, 6),
                       self.images[3].subsample(6, 6), self.images[4].subsample(6, 6), self.images[5].subsample(6, 6)]

        # ============================================= TKINTER CODE ===================================================

        # Frame that the dice will display in after being rolled
        self.frame = tkinter.Frame(self, width = 1000, height = 110)
        self.frame.pack()

        # Label so the user knows this is where they input their desired amount of dice to roll
        tkinter.Label(self, text="Number of Dice:").pack()

        # Text box that accepts user input
        self.dienum = tkinter.Text(self, width=5, height=1)
        self.dienum.pack()

        # Button that will call function buttonclick to roll and display the dice
        tkinter.Button(self, text="Roll Dice", command=self.buttonclick).pack()

        # Label for the sum of all dice values
        tkinter.Label(self, text="Total: ").pack()

        # Variable that changes based on the sum of the dice values
        self.labelVariable = tkinter.IntVar()
        self.w = tkinter.Label(self, textvariable=self.labelVariable)
        self.w.pack()

    # ==================================================================================================================
    #
    #   Function: userinput
    #
    #   Definition: This function will accept input from the user as a string and converts is to an integer
    #
    #   Author: Patrick Crowley
    #
    #   Date: 4/23/19
    #
    #   History: [4/23/19] Function created and modified
    #            [4/25/19] Function tested, modified and finished
    #
    # ==================================================================================================================

    def userinput(self):
        # Converts the input from a string to an integer
        return int(self.dienum.get("1.0", tkinter.END))

    # ==================================================================================================================
    #
    #   Function: roll
    #
    #   Definition: This function will generate a random number 0 - 5 to pick a random index from array self.resize
    #               to display a random image
    #
    #   Author: Patrick Crowley
    #
    #   Date: 4/23/19
    #
    #   History: [4/23/19] Function created and modified
    #            [4/25/19] Function tested and modified
    #            [4/26/19] Function tested, modified and finished
    #
    # ==================================================================================================================

    def roll(self):
        # Generates a random number for a random index of array self.resize
        return random.randrange(0, 5)

    # ==================================================================================================================
    #
    #   Procedure: rollthedice
    #
    #   Definition: This function will delete the previous dice before generating new ones
    #
    #   Author: Patrick Crowley
    #
    #   Date: 4/23/19
    #
    #   History: [4/23/19] Procedure created and modified
    #            [4/24/19] Procedure tested and modified
    #            [4/26/19] Procedure tested, modified and finished
    #
    # ==================================================================================================================

    def rollthedice(self):
        # Resets the sum of the dice when the user rerolls
        self.totals = 0
        # Resets the die faces when the user rerolls
        for x in self.frame.winfo_children():
            x.destroy()

    # ==================================================================================================================
    #
    #   Function: buttonclick
    #
    #   Definition: This function will take the random number generated in function roll and display a die face and
    #               add the value of the die fac to a variable, then set variable labelVariable to the value of the sum
    #               of dice and return it.
    #
    #   Author: Patrick Crowley
    #
    #   Date: 4/24/19
    #
    #   History: [4/24/19] Function created and modified
    #            [4/25/19] Function tested and modified
    #            [4/26/19] Function tested, modified and finished
    #
    # ==================================================================================================================

    def buttonclick(self):
        # Calls rollthedice for the random number
        self.rollthedice()
        # For loop that will display a die value for the length of however many die the user wants to roll
        for x in range(0, self.userinput()):
            # Variable that will be used to find the sum of the die faces
            die = self.roll()
            # Displays a die face in a label
            tkinter.Label(self.frame, image=self.resize[die]).pack(side=tkinter.LEFT)
            # Since the random number is used to find the index it is one less than the die face. This will make each
            # value of the die face have the proper integer added to the total sum
            self.totals += (die + 1)
        # Sets the variable below the "Roll" button to the sum of the die faces
        self.labelVariable.set(self.totals)
        # Returns the value of the die faces
        return self.totals
        # print(self.totals)
        # return self.totals

# ======================================================================================================================
#
#   Program: Main
#
#   Definition: This program will initiate the main class "Rolltk" and loop the program so the GUI can operate
#
#   Author: Patrick Crowley
#
#   Date: 4/23/19
#
#   History: [4/23/19] Main program started, modified and finished
#
# ======================================================================================================================


if __name__ == "__main__":
    # Calls the main class "Rolltk
    app = Rolltk(None)
    # Sets the title of the window to "Dice Roller"
    app.title("Dice Roller")
    # Loops the program so the GUI can work
    app.mainloop()
