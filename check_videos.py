import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
from tkinter import Listbox
import tkinter.scrolledtext as tkst
from video_library import list_all, show_name, show_video_info_by_id, list_videos_by_director
import font_manager as fonts


class CheckVideosFrame(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.setup_ui_for_CVW()


    def setup_ui_for_CVW(self):
        self.top_list = tkst.ScrolledText(self, width=40, height=10, wrap="none")
        self.top_list.grid(row=2, column=0, columnspan=3, rowspan=11, padx=10, pady=5)

        self.bottom_list = tkst.ScrolledText(self, width=40, height=10, wrap="none")
        self.bottom_list.grid(row=15, column=0, columnspan=3, rowspan=11, padx=10, pady=10)

        enter_text_lbl = Label(self, width=20, text="Enter Video Director", font=("Helvetica", 10))
        enter_text_lbl.grid(row=2, column=3)

        self.input_txt = Entry(self, width=15)
        self.input_txt.grid(row=3, column=3)

        self.add_to_playlist_btn = Button(self, width=15, text="List Videos", command=self.list_videos, font=("Helvetica", 10))
        self.add_to_playlist_btn.grid(row=6, column=3)

        create_video_list_btn = Button(self, width=15, text="List All Videos", command=self.list_all_videos, font=("Helvetica", 10))
        create_video_list_btn.grid(row=12, column=3)

        enter_number_lbl = Label(self, width=20, text="Enter Video Number", font=("Helvetica", 10))
        enter_number_lbl.grid(row=18, column=3)

        self.input_num = Entry(self, width=15)
        self.input_num.grid(row=20, column=3)

        play_playlist_btn = Button(self, width=15, text="Check Video", command=self.check_video, font=("Helvetica", 10))
        play_playlist_btn.grid(row=22, column=3)

        back_button = tk.Button(self, text="Back to Home", command=self.back_to_home, font=("Helvetica", 10))
        back_button.grid(row=2, column=5, padx=10)

    def list_all_videos(self):
        # Handle the "List All Video" button click event
        self.top_list.delete("1.0", tk.END)
        videos = list_all()
        for video in videos:
            self.top_list.insert(tk.END, video + "\n")

        # Display status label
        status_lbl = tk.Label(self, text="List videos button was clicked!", font=("Helvetica", 10))
        status_lbl.grid(row=26, column=0, columnspan=4, sticky="W", padx=10, pady=10) 
        return

    def list_videos(self):
        director_name = self.input_txt.get()

        if director_name != "":
                self.top_list.delete("1.0", tk.END)
                director_videos = list_videos_by_director(director_name)

                if director_videos != []:
                    for video in director_videos:
                        self.top_list.insert(tk.END, video + "\n")
                else:
                    self.top_list.delete(1.0, tk.END)
                    self.top_list.insert(1.0, "Videos not found" )
        else:
            messagebox.showwarning("Warning", f"Please enter video director")

    def check_video(self):
        # Handle the "Check Video" button click event
        video_id = self.input_num.get()

        if video_id != "":
            video_name = show_name(video_id)

            if video_name is not None:
                self.bottom_list.delete("1.0", tk.END)
                video_info = show_video_info_by_id(video_id)
                arr = []
                for info in video_info:
                    arr.append(info)
                self.bottom_list.insert(tk.END, "Video name: " + arr[0] + "\n")
                self.bottom_list.insert(tk.END, "Director: " + arr[1] + "\n")
                self.bottom_list.insert(tk.END, "Rating: " + str(arr[2]) + "\n")
                self.bottom_list.insert(tk.END, "Play count: " + str(arr[3]) + "\n")
            else: 
                self.bottom_list.delete(1.0, tk.END)
                self.bottom_list.insert(1.0, "Video not found" )
        else: 
            messagebox.showwarning("Warning", f"Please enter video number")
        
        # Display status label
        status_lbl = tk.Label(self, text="Check videos button was clicked!", font=("Helvetica", 10))
        status_lbl.grid(row=26, column=0, sticky="W", padx=10, pady=10) 
        return
    
    def back_to_home(self):
        from main import VideoPlayerApp
        self.controller.back_to_home()
    


