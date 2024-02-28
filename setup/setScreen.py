import tkinter

root = tkinter.Tk()
root.withdraw()

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

window_height = screen_height // 2
window_width = screen_width // 2

x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
