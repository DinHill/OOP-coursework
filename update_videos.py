import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
import video_library as lib
import font_manager as fonts
from video_library import update_video_rating, show_video_info_by_id

class UpdateVideosFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.setup_ui_for_UVW()


    def setup_ui_for_UVW(self):
        self.video_number_label = Label(self, text="Enter Video Number:")
        self.video_number_label.grid(row=0, column=0, padx=10, pady=10)

        self.video_number_entry = Entry(self,width=10)
        self.video_number_entry.grid(row=0, column=1, padx=10, pady=10)

        self.rating_label = Label(self, text="Enter New Rating:")
        self.rating_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        self.rating_entry = Entry(self, width=10)
        self.rating_entry.grid(row=1, column=1, padx=10, pady=10)

        self.update_button = Button(self, text="Update Video", command=self.update_video)
        self.update_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        back_button = tk.Button(self, text="Back to Home", command=self.back_to_home, font=("Helvetica", 10))
        back_button.grid(row=0, column=5, padx=10)


    def update_video(self):
        video_number = self.video_number_entry.get()
        new_rating = self.rating_entry.get()

        if not video_number or not new_rating:
            messagebox.showerror("Error", "Please enter both Video Number and New Rating.")
            return

        try:
            video_info = show_video_info_by_id(video_number)
            if video_info:
                video_name = video_info[0]  
                play_count = video_info[3]  
                update_video_rating(video_number, new_rating)

                messagebox.showinfo("Success", f"Video Name: {video_name}\nNew Rating: {new_rating}\nPlay Count: {play_count}")
            else:
                messagebox.showerror("Error", "Invalid Video Number. Video not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def back_to_home(self):
        from main import VideoPlayerApp
        self.controller.back_to_home()


