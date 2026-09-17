import tkinter as tk
import random
import os
import sys
import pygame

def resource_path(relative_path):
    """ Trova il percorso del file mp3 sia in modalità script che dentro l'EXE """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class IdiotWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("You Are An Idiot!")
        self.root.attributes('-topmost', True)
        
        self.window_width = 400
        self.window_height = 300
        
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        self.x = random.randint(0, max(0, self.screen_width - self.window_width))
        self.y = random.randint(0, max(0, self.screen_height - self.window_height))
        
        self.dx = random.choice([-6, -4, 4, 6])
        self.dy = random.choice([-6, -4, 4, 6])
        self.is_white = True
        
        self.setup_ui()
        self.move_window()
        self.flash_screen()
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def setup_ui(self):
        self.label_text = tk.Label(
            self.root, 
            text="You are an idiot!\n☺ ☺ ☺", 
            font=("Arial", 26, "bold"), 
            fg="black", 
            bg="white"
        )
        self.label_text.pack(expand=True, fill="both")
        self.root.configure(bg="white")
        self.root.geometry(f"{self.window_width}x{self.window_height}+{self.x}+{self.y}")

    def move_window(self):
        self.x += self.dx
        self.y += self.dy
        
        if self.x <= 0 or self.x >= (self.screen_width - self.window_width):
            self.dx = -self.dx
        if self.y <= 0 or self.y >= (self.screen_height - self.window_height):
            self.dy = -self.dy
            
        self.root.geometry(f"+{self.x}+{self.y}")
        self.root.after(10, self.move_window)

    def flash_screen(self):
        if self.is_white:
            self.root.configure(bg="black")
            self.label_text.configure(fg="white", bg="black")
            self.is_white = False
        else:
            self.root.configure(bg="white")
            self.label_text.configure(fg="black", bg="white")
            self.is_white = True
        self.root.after(150, self.flash_screen)

    def on_closing(self):
        self.root.destroy()
        spawn_windows(2)

def spawn_windows(count):
    for _ in range(count):
        window = IdiotWindow()
        windows_list.append(window)

if __name__ == "__main__":
    windows_list = []
    
    # Inizializzazione audio
    pygame.mixer.init()
    audio_file = resource_path("idiot.mp3")
    
    if os.path.exists(audio_file):
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play(-1)
    
    spawn_windows(1)
    tk.mainloop()
