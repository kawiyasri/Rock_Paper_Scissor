
    # Import libraries
import random
from tkinter import *

# Initialize window
root = Tk()
root.title("ROCK, PAPER, SCISSOR GAME USING PYTHONGEEKS")
width = 650
height = 580
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
x = int((window_width / 2) - (width / 2))
y = int((window_height / 2) - (height / 2))
root.geometry(f"{width}x{height}+{x}+{y}")
root.resizable(0, 0)
root.config(bg="#e3f4f1")

# Initialize player option
player_option = 0

# Load images (use raw strings to avoid path issues)
Blank_img = PhotoImage(file=r"D:/Projects/RockPaperScissor/RPSG/resources/blank.png")
Player_Rock = PhotoImage(file=r"D:/Projects/RockPaperScissor/RPSG/resources/rock_player.png")
Player_Rock_ado = Player_Rock.subsample(3, 3)
Player_Paper = PhotoImage(file=r"D:/Projects/RockPaperScissor/RPSG/resources/paper_player.png")
Player_Paper_ado = Player_Paper.subsample(3, 3)
Player_Scissor = PhotoImage(file=r"D:/Projects/RockPaperScissor/RPSG/resources/scissor_player.png")
Player_Scissor_ado = Player_Scissor.subsample(3, 3)
Computer_Rock = PhotoImage(file=r"D:/Projects/RockPaperScissor/RPSG/resources/rock_computer.png")
Computer_Paper = PhotoImage(file=r"D:/Projects/RockPaperScissor/RPSG/resources/paper_computer.png")
Computer_Scissor = PhotoImage(file=r"D:/Projects/RockPaperScissor/RPSG/resources/scissor_computer.png")

# Function for player's choice
def Rock():
    global player_option
    player_option = 1
    Image_Player.configure(image=Player_Rock)
    Matching() 

def Paper():
    global player_option
    player_option = 2
    Image_Player.configure(image=Player_Paper)
    Matching() 

def Scissor():
    global player_option
    player_option = 3
    Image_Player.configure(image=Player_Scissor)
    Matching()

# Functions for computer choice outcomes
def Comp_Rock():
    if player_option == 1:
        Label_Status.config(text="Game Tie")
    elif player_option == 2:
        Label_Status.config(text="Player Wins")
    elif player_option == 3:
        Label_Status.config(text="Computer Wins")

def Comp_Paper():
    if player_option == 1:
        Label_Status.config(text="Computer Wins")
    elif player_option == 2:
        Label_Status.config(text="Game Tie")
    elif player_option == 3:
        Label_Status.config(text="Player Wins")
 
def Comp_Scissor():
    if player_option == 1:
        Label_Status.config(text="Player Wins")
    elif player_option == 2:
        Label_Status.config(text="Computer Wins")
    elif player_option == 3:
        Label_Status.config(text="Game Tie")

# Function to match player and computer choice
def Matching():
    computer_option = random.randint(1, 3)
    if computer_option == 1:
        Image_Computer.configure(image=Computer_Rock)
        Comp_Rock()
    elif computer_option == 2:
        Image_Computer.configure(image=Computer_Paper)
        Comp_Paper()
    elif computer_option == 3:
        Image_Computer.configure(image=Computer_Scissor)
        Comp_Scissor()

# Exit function
def Exit():
    root.destroy()
    exit()

# Layout
Image_Player = Label(root, image=Blank_img)
Image_Computer = Label(root, image=Blank_img)
Label_Player = Label(root, text="PLAYER", bg="#e8c1c7", fg="black", font=('Times New Roman', 18, 'bold'))
Label_Computer = Label(root, text="COMPUTER", bg="#e8c1c7", fg="black", font=('Times New Roman', 18, 'bold'))
Label_Status = Label(root, text="", fg="black", font=('Times New Roman', 20, 'bold','italic'))

Label_Player.grid(row=1, column=1, padx=20, pady=10)
Label_Computer.grid(row=1, column=3, padx=20, pady=10)
Image_Player.grid(row=2, column=1, padx=30, pady=20)
Image_Computer.grid(row=2, column=3, pady=20)
Label_Status.grid(row=3, column=2, pady=20)

# Buttons
rock = Button(root, image=Player_Rock_ado, command=Rock)
paper = Button(root, image=Player_Paper_ado, command=Paper)
scissor = Button(root, image=Player_Scissor_ado, command=Scissor)
button_quit = Button(root, text="Quit", bg="red", fg="white", font=('Times New Roman', 25, 'bold'), command=Exit)

rock.grid(row=4, column=1, pady=30)
paper.grid(row=4, column=2, pady=30)
scissor.grid(row=4, column=3, pady=30)
button_quit.grid(row=5, column=2, pady=20)

# Run the application
if __name__ == '__main__':
    root.mainloop()
