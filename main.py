from tkinter import *
from tkinter import filedialog
import pygame
from functions import load, play, pause, next_song, previous_song

root = Tk()
root.title("SpotiBot")
root.geometry("600x400")

pygame.mixer.init()
songlist = Listbox(root, bg="pink", fg="white", width=200, height=50)
songlist.pack()

play_button_image = PhotoImage(file='play.png')
pause_button_image = PhotoImage(file='pause.png')
next_button_image = PhotoImage(file='next.png')
previous_button_image = PhotoImage(file='previous.png')

control_frame = Frame(root)
control_frame.pack()

play_button = Button(control_frame, image=play_button_image, borderwidth=0, command=lambda: play(root))
pause_button = Button(control_frame, image=pause_button_image, borderwidth=0, command=pause)
next_button = Button(control_frame, image=next_button_image, borderwidth=0, command=lambda: next_song(root,songlist))
previous_button = Button(control_frame, image=previous_button_image, borderwidth=0, command=lambda: previous_song(root, songlist))

play_button.grid(row=0, column=1, padx=7, pady=10)
pause_button.grid(row=0, column=2, padx=7, pady=10)
next_button.grid(row=0, column=3, padx=7, pady=10)
previous_button.grid(row=0, column=0, padx=7, pady=10)

menu = Menu(root)
root.config(menu=menu)

menu_options = Menu(menu)
menu_options.add_command(label="Choose folder", command=lambda: load(root, songlist))
menu.add_cascade(label="Let's play some music", menu=menu_options)

root.mainloop()
