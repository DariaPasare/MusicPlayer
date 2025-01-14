import pygame
import os
from tkinter import *
from tkinter import filedialog

songs = []
current_song = 0
directory = ""
paused = False

def load(root, songlist):
    global current_song, directory
    directory = filedialog.askdirectory()

    songs.clear()
    songlist.delete(0, END)

    for song in os.listdir(directory):
        if song.endswith(".mp3"):
            songs.append(song)
            songlist.insert(END, song)

    if songs:
        songlist.selection_set(0)
        current_song = songs[songlist.curselection()[0]]

def play(root):
    global current_song, paused, directory
    if not paused:
        pygame.mixer.music.load(os.path.join(directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
    paused = False

def pause():
    global paused
    pygame.mixer.music.pause()
    paused = True

def next_song(songlist):
    global current_song, paused
    current_song_index = songs.index(current_song)

    if current_song_index < len(songs) - 1:
        current_song = songs[current_song_index + 1]
        songlist.selection_clear(0, END)
        songlist.selection_set(current_song_index + 1)
        play()

def previous_song(songlist):
    global current_song, paused
    current_song_index = songs.index(current_song)

    if current_song_index > 0:
        current_song = songs[current_song_index - 1]
        songlist.selection_clear(0, END)
        songlist.selection_set(current_song_index - 1)
        play()