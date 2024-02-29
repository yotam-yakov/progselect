import customtkinter as ctk


def add_canvas(window):
    # Make the window borderless
    window.overrideredirect(True)

    # Create a canvas
    canvas = ctk.CTkFrame(window, corner_radius=50, bg_color="transparent")
    canvas.pack(fill=ctk.BOTH, expand=True)

    return canvas
