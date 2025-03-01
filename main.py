import tkinter as tk
from tkinter import Button
from check_videos import CheckVideosFrame
from create_video_list import CreateVideoListFrame
from update_videos import UpdateVideosFrame
import font_manager as fonts

class VideoPlayerApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        fonts.configure()
        self.title("Video Player")
        self.geometry("800x600")

        self.frames = {}

        self.create_frames()
        self.show_frame(VideoPlayerFrame)

    def create_frames(self):
        self.frames[VideoPlayerFrame] = VideoPlayerFrame(self, self)
        self.frames[CheckVideosFrame] = CheckVideosFrame(self, self)
        self.frames[CreateVideoListFrame] = CreateVideoListFrame(self, self)
        self.frames[UpdateVideosFrame] = UpdateVideosFrame(self, self)

    def show_frame(self, frame_class):
        new_frame = self.frames.get(frame_class)
        if new_frame:
            if hasattr(self, 'current_frame') and hasattr(self.current_frame, '_w'):
                self.current_frame.pack_forget()  # Unpack the current frame
            new_frame.pack(fill=tk.BOTH, expand=True)
            self.current_frame = new_frame
        else:
            print(f"Frame {frame_class} not found in frames dictionary.")

    def back_to_home(self):
        self.show_frame(VideoPlayerFrame)

 
class VideoPlayerFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.setup_ui()

    def setup_ui(self):
        # Create title label
        self.title_label = tk.Label(self, text="Select an option by clicking one of the buttons below")
        self.title_label.grid(row=0, column=3, padx=10, pady=10)

        # Create GUI components
        self.check_videos_button = tk.Button(self, text="Check Videos", command=lambda: self.controller.show_frame(CheckVideosFrame))
        self.check_videos_button.grid(row=1, column=3, padx=10, pady=10)

        self.create_video_list_button = tk.Button(self, text="Create Video List", command=lambda: self.controller.show_frame(CreateVideoListFrame))
        self.create_video_list_button.grid(row=2, column=3, padx=10, pady=10)

        self.update_video_button = tk.Button(self, text="Update Videos", command=lambda: self.controller.show_frame(UpdateVideosFrame))
        self.update_video_button.grid(row=3, column=3, padx=10, pady=10)


if __name__ == "__main__":
    app = VideoPlayerApp()
    app.mainloop()
