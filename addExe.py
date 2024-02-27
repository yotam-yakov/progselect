import customtkinter as ctk
import subprocess


def add_exe(file_path, master):

    if file_path:
        def open_file():
            subprocess.Popen(file_path)

        print(f"Selected file: {file_path}")
        filename = file_path.split("/")
        game_frame = ctk.CTkFrame(master, fg_color="transparent")
        game_frame.pack()
        game = ctk.CTkButton(
            game_frame,
            width=150,
            height=150,
            corner_radius=30,
            text="",
            command=open_file
        )
        game.pack(pady=5)
        game_label = ctk.CTkLabel(game_frame, text=filename[-1][:-4])
        game_label.pack()
