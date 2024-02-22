import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
import subprocess


import screen


def browse_file():
    filetypes = (
        ('exe', '*.exe'),
    )
    file_path = filedialog.askopenfilename(filetypes=filetypes)
    if file_path:
        print(f"Selected file: {file_path}")
        filename = file_path.split("/")
        label = ctk.CTkLabel(frame, text=filename[-1][:-4])
        label.pack()
        # subprocess.Popen(filename)


# Set App Frame
ctk.set_appearance_mode("System")
app = ctk.CTk()
app.geometry(f"{screen.window_width}x{screen.window_height}+{screen.x_coordinate}+{screen.y_coordinate}")
app.title("ProgSelect")
# app.overrideredirect(True)

frame = ctk.CTkFrame(app, corner_radius=20)
frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
button = ctk.CTkButton(
    app,
    width=100,
    height=100,
    text_color="black",
    fg_color="grey",
    text="+",
    font=("Ariel", 80),
    corner_radius=20,
    command=browse_file
)
button.pack(pady=20)

# Run Loop
app.mainloop()
