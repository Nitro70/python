import tkinter as tk
import pygetwindow as gw
import pyautogui

def get_running_processes():
    return [win.title for win in gw.getWindowsWithTitle('')]

def send_text(process_title, text):
    window = gw.getWindowsWithTitle(process_title)
    if window:
        window = window[0]
        window.activate()
        pyautogui.write(text)

def send_enter_key(process_title, text_to_type):
    window = gw.getWindowsWithTitle(process_title)
    if window:
        window = window[0]
        window.activate()
        pyautogui.write(text_to_type, interval=0.1)
        pyautogui.press('enter')

def send_space_key(process_title):
    window = gw.getWindowsWithTitle(process_title)
    if window:
        window = window[0]
        window.activate()
        pyautogui.press('space')

def refresh_process_list():
    process_listbox.delete(0, tk.END)
    process_list = get_running_processes()
    for process in process_list:
        process_listbox.insert(tk.END, process)

def close_selected():
    selected_process = process_listbox.get(process_listbox.curselection())
    window = gw.getWindowsWithTitle(selected_process)
    if window:
        window[0].close()

def minimize_selected():
    selected_process = process_listbox.get(process_listbox.curselection())
    window = gw.getWindowsWithTitle(selected_process)
    if window:
        window[0].minimize()

def maximize_selected():
    selected_process = process_listbox.get(process_listbox.curselection())
    window = gw.getWindowsWithTitle(selected_process)
    if window:
        window[0].maximize()

def process_selected():
    selected_process = process_listbox.get(process_listbox.curselection())
    text_to_type = text_entry.get()
    send_text(selected_process, text_to_type)

def press_enter_key(event):
    selected_process = process_listbox.get(process_listbox.curselection())
    text_to_type = text_entry.get()
    send_enter_key(selected_process, text_to_type)

def press_space_key():
    selected_process = process_listbox.get(process_listbox.curselection())
    send_space_key(selected_process)

app = tk.Tk()
app.title("Text Typer")
app.attributes("-topmost", True)

window_width = 600
window_height = 400
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
app.geometry(f"{window_width}x{window_height}+{x}+{y}")

process_list = get_running_processes()
process_listbox = tk.Listbox(app, selectmode=tk.SINGLE)
for process in process_list:
    process_listbox.insert(tk.END, process)

text_label = tk.Label(app, text="Enter text to type:")
text_entry = tk.Entry(app)
type_button = tk.Button(app, text="Type Text", command=process_selected)
refresh_button = tk.Button(app, text="Refresh List", command=refresh_process_list)
close_button = tk.Button(app, text="Close Process", command=close_selected)
minimize_button = tk.Button(app, text="Minimize Process", command=minimize_selected)
maximize_button = tk.Button(app, text="Maximize Process", command=maximize_selected)
space_button = tk.Button(app, text="Press Space", command=press_space_key)

process_listbox.pack()
text_label.pack()
text_entry.pack()
type_button.pack()
refresh_button.pack()
close_button.pack()
minimize_button.pack()
maximize_button.pack()
space_button.pack()

text_entry.bind('<Return>', press_enter_key)

app.mainloop()import tkinter as tk
import pygetwindow as gw
import pyautogui

def get_running_processes():
    return [win.title for win in gw.getWindowsWithTitle('')]

def send_text(process_title, text):
    window = gw.getWindowsWithTitle(process_title)
    if window:
        window = window[0]
        window.activate()
        pyautogui.write(text)

def send_enter_key(process_title, text_to_type):
    window = gw.getWindowsWithTitle(process_title)
    if window:
        window = window[0]
        window.activate()
        pyautogui.write(text_to_type, interval=0.1)
        pyautogui.press('enter')

def send_space_key(process_title):
    window = gw.getWindowsWithTitle(process_title)
    if window:
        window = window[0]
        window.activate()
        pyautogui.press('space')

def refresh_process_list():
    process_listbox.delete(0, tk.END)
    process_list = get_running_processes()
    for process in process_list:
        process_listbox.insert(tk.END, process)

def close_selected():
    selected_process = process_listbox.get(process_listbox.curselection())
    window = gw.getWindowsWithTitle(selected_process)
    if window:
        window[0].close()

def minimize_selected():
    selected_process = process_listbox.get(process_listbox.curselection())
    window = gw.getWindowsWithTitle(selected_process)
    if window:
        window[0].minimize()

def maximize_selected():
    selected_process = process_listbox.get(process_listbox.curselection())
    window = gw.getWindowsWithTitle(selected_process)
    if window:
        window[0].maximize()

def process_selected():
    selected_process = process_listbox.get(process_listbox.curselection())
    text_to_type = text_entry.get()
    send_text(selected_process, text_to_type)

def press_enter_key(event):
    selected_process = process_listbox.get(process_listbox.curselection())
    text_to_type = text_entry.get()
    send_enter_key(selected_process, text_to_type)

def press_space_key():
    selected_process = process_listbox.get(process_listbox.curselection())
    send_space_key(selected_process)

app = tk.Tk()
app.title("Text Typer")
app.attributes("-topmost", True)

window_width = 600
window_height = 400
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
app.geometry(f"{window_width}x{window_height}+{x}+{y}")

process_list = get_running_processes()
process_listbox = tk.Listbox(app, selectmode=tk.SINGLE)
for process in process_list:
    process_listbox.insert(tk.END, process)

text_label = tk.Label(app, text="Enter text to type:")
text_entry = tk.Entry(app)
type_button = tk.Button(app, text="Type Text", command=process_selected)
refresh_button = tk.Button(app, text="Refresh List", command=refresh_process_list)
close_button = tk.Button(app, text="Close Process", command=close_selected)
minimize_button = tk.Button(app, text="Minimize Process", command=minimize_selected)
maximize_button = tk.Button(app, text="Maximize Process", command=maximize_selected)
space_button = tk.Button(app, text="Press Space", command=press_space_key)

process_listbox.pack()
text_label.pack()
text_entry.pack()
type_button.pack()
refresh_button.pack()
close_button.pack()
minimize_button.pack()
maximize_button.pack()
space_button.pack()

text_entry.bind('<Return>', press_enter_key)

app.mainloop()
