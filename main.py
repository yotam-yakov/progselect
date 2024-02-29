import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk

from setup import setScreen, drawCanvas
from features import addFile


def browse_file():
    filetypes = (
        ('exe', '*.exe'),
    )
    file_path = filedialog.askopenfilename(filetypes=filetypes)

    print(f"Selected file: {file_path}")

    addFile.add_file(file_path, frame)


# Set App Frame
ctk.set_appearance_mode("System")
app = ctk.CTk()
app.geometry(f"{setScreen.window_width}x{setScreen.window_height}+{setScreen.x_coordinate}+{setScreen.y_coordinate}")
app.title("ProgSelect")
app.overrideredirect(True)

canvas = drawCanvas.add_canvas(app)

frame = ctk.CTkFrame(canvas, corner_radius=20)
frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

button = ctk.CTkButton(
    canvas,
    width=100,
    height=100,
    text_color="black",
    fg_color="grey",
    hover_color="lightblue",
    border_color="black",
    border_width=4,
    text="+",
    font=("Ariel", 80),
    corner_radius=20,
    command=browse_file
)
button.pack(pady=20)

# Run Loop
app.mainloop()
