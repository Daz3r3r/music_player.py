import tkinter as tk
from tkinter import filedialog
import pygame


pygame.init()
pygame.mixer.init()

def load_music():
    global current_file
    current_file = filedialog.askopenfilename(filetypes=[("Music Files", "*.mp3;*.wav")])
    if current_file:
        pygame.mixer.music.load(current_file)
        status_label.config(text=f"Відтворюється: {current_file.split('/')[-1]}")

def play_music():
    if current_file:
        pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()


root = tk.Tk()
root.title("Music Player")
root.geometry("400x300")
root.configure(bg="lightblue")

current_file = None


load_button = tk.Button(root, text="Завантажити музику", command=load_music, bg="yellow", fg="black", font=("Helvetica", 12))
load_button.pack(pady=10)

play_button = tk.Button(root, text="Відтворити", command=play_music, bg="green", fg="black", font=("Helvetica", 12))
play_button.pack(pady=10)

pause_button = tk.Button(root, text="Пауза", command=pause_music, bg="orange", fg="black", font=("Helvetica", 12))
pause_button.pack(pady=10)

unpause_button = tk.Button(root, text="Продовжити", command=unpause_music, bg="blue", fg="white", font=("Helvetica", 12))
unpause_button.pack(pady=10)

stop_button = tk.Button(root, text="Зупинити", command=stop_music, bg="red", fg="black", font=("Helvetica", 12))
stop_button.pack(pady=10)

status_label = tk.Label(root, text="Музика не завантажена", bg="lightblue", fg="black", font=("Helvetica", 12))
status_label.pack(pady=10)

root.mainloop()
