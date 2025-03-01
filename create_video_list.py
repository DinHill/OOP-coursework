import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
from video_library import show_name, increment_play_count
from tkinter import messagebox
import font_manager as fonts

class CreateVideoListFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.setup_ui_for_CVLW()


    def setup_ui_for_CVLW(self):
        top_lbl = tk.Label(self, text="Select all videos you want to add to a new list", font=("Helvetica", 12))
        top_lbl.grid(row=0, column=0, columnspan=3)

        self.top_list = tkst.ScrolledText(self, width=40, height=10, wrap="none")
        self.top_list.grid(row=2, column=0, columnspan=3, rowspan=11, padx=10, pady=5)

        self.bottom_list = tkst.ScrolledText(self, width=40, height=10, wrap="none")
        self.bottom_list.grid(row=15, column=0, columnspan=3, rowspan=11, padx=10, pady=10)
        self.bottom_list.insert("1.0", "There is no video in this list")

        bottom_lbl = tk.Label(self, text="Your Playlist", font=("Helvetica", 12))
        bottom_lbl.grid(row=14, column=0, columnspan=3, pady=5)

        enter_lbl = tk.Label(self, width=20, text="Enter Video Number", font=("Helvetica", 10))
        enter_lbl.grid(row=2, column=3)

        self.input_txt = tk.Entry(self, width=3)
        self.input_txt.grid(row=3, column=3)

        self.add_to_playlist_btn = tk.Button(self, width=20, text="Add Video to Playlist", command=self.add_to_playlist, font=("Helvetica", 10))
        self.add_to_playlist_btn.grid(row=6, column=3)

        create_video_list_btn = tk.Button(self, width=20, text="Reset Playlist", command=self.reset_playlist, font=("Helvetica", 10))
        create_video_list_btn.grid(row=12, column=3)

        videos_from_library = lib.list_all()
        for video in videos_from_library:
            self.top_list.insert(tk.END, video + "\n")

        play_playlist_btn = tk.Button(self, width=20, text="Play Playlist", command=self.play_playlist, font=("Helvetica", 10))
        play_playlist_btn.grid(row=20, column=3, sticky="W")

        back_button = tk.Button(self, text="Back to Home", command=self.back_to_home, font=("Helvetica", 10))
        back_button.grid(row=2, column=5, padx=10)


    def add_to_playlist(self):
        video_number = self.input_txt.get()
        video_name = show_name(video_number)
        message = "There is no video in this list"
        if message in self.bottom_list.get("1.0", tk.END):
            self.bottom_list.delete("1.0", tk.END)
        if video_name:        
            self.bottom_list.insert(tk.END, video_name + "\n")
        else:
            messagebox.showerror("Error", "Invalid Video Number. Video not found.")

    def reset_playlist(self):
        self.bottom_list.delete("1.0", tk.END)
        self.bottom_list.insert("1.0", "There is no video in this list")

    def play_playlist(self):
        playlist_content = self.bottom_list.get("1.0", tk.END)
    
        if playlist_content.strip() == "There is no video in this list":
            messagebox.showinfo("Error", "Playlist is empty. Add videos to the playlist first.")
            return

        playlist_lines = playlist_content.split("\n")
        for line in playlist_lines:
            if line.strip() != "There is no video in this list":
                if line.strip() != "":
                    increment_play_count(line)

        messagebox.showinfo("Success", "Playlist simulated. Play counts incremented.")

    def back_to_home(self):
        from main import VideoPlayerApp
        self.controller.back_to_home()


