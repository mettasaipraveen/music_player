import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pygame

# Initialize the pygame mixer
pygame.mixer.init()

# Directory to store music files
music_directory = "music_files"

# Check if the directory exists, if not, create it
if not os.path.exists(music_directory):
    os.makedirs(music_directory)

# Function to load and play the selected music file
def load_music():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3"), ("WAV files", "*.wav")])
    if file_path:
        # Copy the file to the music directory
        file_name = os.path.basename(file_path)
        destination = os.path.join(music_directory, file_name)
        
        # If the file doesn't already exist in the music folder, copy it
        if not os.path.exists(destination):
            os.rename(file_path, destination)
            messagebox.showinfo("Music Added", f"Music file {file_name} added to the music library.")
        
        # Update the listbox with the new music file
        update_music_list()

# Function to update the listbox with available music files in the music directory
def update_music_list():
    # Clear the listbox
    music_listbox.delete(0, tk.END)
    
    # Add all music files from the music directory to the listbox
    for music_file in os.listdir(music_directory):
        if music_file.endswith(('.mp3', '.wav')):
            music_listbox.insert(tk.END, music_file)

# Function to play the selected music from the listbox
def play_music():
    selected_music = music_listbox.get(tk.ACTIVE)
    if selected_music:
        file_path = os.path.join(music_directory, selected_music)
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        song_label.config(text=f"Now Playing: {selected_music}")

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()
    song_label.config(text="Music Stopped")

# Function to pause the music
def pause_music():
    pygame.mixer.music.pause()

# Function to unpause the music
def unpause_music():
    pygame.mixer.music.unpause()

# Create the main window
window = tk.Tk()
window.title("Music Player with Playlist")
window.geometry("500x400")

# Song Label
song_label = tk.Label(window, text="No Song Playing", font=("Arial", 12))
song_label.pack(pady=20)

# Button to load music
load_button = tk.Button(window, text="Load Music", command=load_music)
load_button.pack(pady=5)

# Listbox to display stored music files
music_listbox = tk.Listbox(window, height=10, width=50, selectmode=tk.SINGLE)
music_listbox.pack(pady=10)

# Update music list
update_music_list()

# Play Music Button
play_button = tk.Button(window, text="Play", command=play_music)
play_button.pack(pady=5)

# Control Buttons
pause_button = tk.Button(window, text="Pause", command=pause_music)
pause_button.pack(pady=5)

unpause_button = tk.Button(window, text="Unpause", command=unpause_music)
unpause_button.pack(pady=5)

stop_button = tk.Button(window, text="Stop", command=stop_music)
stop_button.pack(pady=5)

# Run the GUI loop
window.mainloop()
