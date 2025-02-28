import tkinter as tk
from tkinter import font, messagebox

def reset_timer(event):
    global typing_active, red_id, orange_id, yellow_id, clear_id
    typing_active = True

    if yellow_id is not None:
        root.after_cancel(yellow_id)
    if orange_id is not None:
        root.after_cancel(orange_id)
    if red_id is not None:
        root.after_cancel(red_id)
    if clear_id is not None:
        root.after_cancel(clear_id)

    text_box.tag_remove("yellow", "1.0", "end")
    text_box.tag_remove("orange", "1.0", "end")
    text_box.tag_remove("red", "1.0", "end")

    start_countdown()  # Restart the countdown

def start_countdown():
    global typing_active, red_id, orange_id, yellow_id, clear_id
    typing_active = False
    yellow_id = root.after(1000, yellow_text)
    orange_id = root.after(3000, orange_text)
    red_id = root.after(5000, red_text)
    clear_id = root.after(6000, clear_text)

def yellow_text():
    if not typing_active:
        text_box.tag_add("yellow", "1.0", "end")

def orange_text():
    if not typing_active:
        text_box.tag_add("orange", "1.0", "end")

def red_text():
    if not typing_active:
        text_box.tag_add("red", "1.0", "end")

def clear_text():
    if not typing_active:
        text_box.delete("1.0", tk.END)
        messagebox.showinfo("Oops!", "Your text was wiped away! Do not stop writing!")

root = tk.Tk()
root.title("Do Not Stop Writing!")

typing_active = False
yellow_id = None
orange_id = None
red_id = None
clear_id = None

custom_font = font.Font(family="Helvetica", size=14, weight="bold")
text_box = tk.Text(root, wrap="word", font=custom_font)
text_box.pack(expand=True, fill="both")

text_box.tag_configure("yellow", foreground="yellow")
text_box.tag_configure("orange", foreground="orange")
text_box.tag_configure("red", foreground="red")

text_box.bind("<KeyPress>", reset_timer)

root.mainloop()

