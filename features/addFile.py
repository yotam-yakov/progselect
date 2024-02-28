import customtkinter as ctk
import subprocess


def add_file(file_path, master):

    if file_path:
        def open_file():
            subprocess.Popen(file_path)

        filename = file_path.split("/")
        file_frame = ctk.CTkFrame(master, fg_color="transparent")
        file_frame.pack()
        file = ctk.CTkButton(
            file_frame,
            width=150,
            height=150,
            corner_radius=30,
            text=filename[-1][:-4],
            command=open_file
        )
        file.pack(pady=5)
        file_label = ctk.CTkLabel(file_frame, text=filename[-1][:-4])
        file_label.pack()
