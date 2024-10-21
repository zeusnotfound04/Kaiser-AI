import os
import random

def play_random_song():
    music_dir = "F:\\Songs"
    songs = os.listdir(music_dir)
    random_song = random.choice(songs)
    os.startfile(os.path.join(music_dir, random_song))
