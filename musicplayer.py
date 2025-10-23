import pygame
import time
import threading
import random
import os
from mutagen.mp3 import MP3
pygame.mixer.init()
#enter mp3 file paths here
path = [{"path": r"/workspaces/music-player-system/Tame Impala - Borderline (Official Audio).mp3","name": "Borderline - Tame Impala"},
        {"path": r"/workspaces/music-player-system/Dua Lipa - Levitating (Lyrics).mp3","name": "Levitating"}]

running = False
global_var = {"atTime": 0,"file_num": 0, "loop": True}
paused = False
changed = False
def play_music():
    if global_var["loop"] == False:
        time.sleep(3)
        pygame.mixer.music.stop()
        thread.join()
    while global_var["loop"] == True:
        random.shuffle(path)
        for i in range(len(path)):
            global audio, duration
            global_var["file_num"] = i
            try:
                pygame.mixer.music.load(path[i]["path"])
                audio = MP3(path[global_var["file_num"]]["path"])
                duration = int(audio.info.length)
                pygame.mixer.music.play()
                time.sleep(5)
                while pygame.mixer.music.get_busy() or running == True:
                    time.sleep(1)
                    if paused == False:
                        global_var["atTime"] += 1
            except:
                print(f"Error. {path[i]["name"]} does not exist. ")
thread = threading.Thread(target = play_music)
thread.start()
while True:
    os.system("cls")
    if changed:
        global_var["atTime"] = 0
        changed = False
    print("Loading",end="")
    for i in range(3):
        print(".",end="",flush=True)
        time.sleep(0.25)
    os.system("cls")
    print(f"Duration: {duration // 60}:{duration % 60:02d}")
    print(path[global_var["file_num"]]["name"])
    print("Play: 'play'\nReplay from beginning: 'replay'\nPause: 'pause'\nNext: [ENTER]\nExit program: 'exit'\nLoop: ",global_var["loop"], "(Type 'loop' to toggle)\nFast-forward by 10s: '>>'\nRewind by 10s: '<<'")
    command = input("Enter a command: ")
    if command.lower() == None:
        continue
    if command.lower() == "play":
        pygame.mixer.music.unpause()
    if command.lower() == "replay":
        pygame.mixer.music.play()
        running = False
    if command.lower() == "pause":
        pygame.mixer.music.pause()
        running = True
        paused = True
    if command.lower() == "":
        pygame.mixer.music.pause()
        running = False
        changed = True
        time.sleep(3)
    if command.lower() == "<<":
        global_var["atTime"] -= 10
        if global_var["atTime"] < 0:
            global_var["atTime"] = 0
        pygame.mixer.music.play(start = global_var["atTime"])
    if command.lower() == ">>":
        global_var["atTime"] += 10
        pygame.mixer.music.play(start = global_var["atTime"])

    if command.lower() == "loop":
        global_var["loop"] = False
    if command.lower() == "exit":
        pygame.mixer.music.pause()
        thread.join()
        break
    
