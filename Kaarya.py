import tkinter as tk
from tkinter import ttk, filedialog
from datetime import datetime
import threading
import time

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

def mark_as_completed():
    selected_task = task_list.curselection()
    if selected_task:
        task = task_list.get(selected_task)
        completed_list.insert(tk.END, f"{task} - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        task_list.delete(selected_task)

def export_list():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            tasks = completed_list.get(0, tk.END)
            for task in tasks:
                file.write(task + "\n")

def start_timer(minutes):
    global countdown, is_running
    countdown = minutes * 60  # Convert minutes to seconds
    is_running = True

    # Start the countdown in a separate thread
    timer_thread = threading.Thread(target=run_timer)
    timer_thread.daemon = True  # Daemonize the thread so it stops with the main program
    timer_thread.start()

def run_timer():
    global countdown, is_running
    while countdown > 0 and is_running:
        minutes, seconds = divmod(countdown, 60)
        time_display = f'{minutes:02d}:{seconds:02d}'
        timer_label.config(text=time_display)
        time.sleep(1)  # Update the display every second
        countdown -= 1
    if is_running:
        timer_label.config(text='00:00')  # Update the display to show '00:00' when timer completes

def toggle_timer():
    global is_running
    is_running = not is_running

root = tk.Tk()
root.title("To-do list w/ focus session")

# Create a notebook-style theme
style = ttk.Style()
style.theme_use('alt')

# Create the notebook appearance
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True, padx=10, pady=10)

# Notebook tab for tasks
task_frame = ttk.Frame(notebook)
notebook.add(task_frame, text='Tasks')

# Add Label for 'Kaarya'
label = tk.Label(text='!z6', font=('Wingdings',25), pady=2)
label1 = tk.Label(text='Kaarya', font=('Freestyle Script',30), pady=5)
label.pack()
label1.pack()

# Create a task list with checkboxes and a scrollbar
task_list = tk.Listbox(task_frame, selectmode=tk.SINGLE, width=80, bd=4, relief=tk.GROOVE)
task_list.pack(pady=5, padx=5)

tasks = ["Enter", "your", "kaarya here"]  # Example tasks
for task in tasks:
    task_list.insert(tk.END, task)

# Entry for adding new tasks
entry = tk.Entry(task_frame,font =('Consolas',15), width=40)
entry.pack()

# Buttons for task actions (in a single row)
action_frame = ttk.Frame(task_frame)
action_frame.pack()

add_button = tk.Button(action_frame, text='Add Kaarya', command=add_task, bg='lightblue')
add_button.pack(side=tk.LEFT, padx=10, pady=10)

remove_button = tk.Button(action_frame, text='Remove', command=remove_task, bg='lightcoral')
remove_button.pack(side=tk.LEFT, padx=10, pady=10)

completed_button = tk.Button(action_frame, text='Mark as Done', command=mark_as_completed, bg='lightgreen')
completed_button.pack(side=tk.LEFT, padx=10, pady=10)

# Notebook tab for completed tasks
completed_frame = ttk.Frame(notebook)
notebook.add(completed_frame, text='Done Tasks')

# Create a completed tasks list with a scrollbar
completed_list = tk.Listbox(completed_frame, selectmode=tk.SINGLE, width=80, bd=2, relief=tk.GROOVE)
completed_list.pack(pady=5, padx=5)

# Additional buttons and elements (in the Done Tasks tab)
extra_frame = ttk.Frame(completed_frame)
extra_frame.pack(pady=10)

# Create a frame for the Export button
export_frame = ttk.Frame(completed_frame)
export_frame.pack()

# Create the Export List button
export_button = tk.Button(export_frame, text='Export List', command=export_list)
export_button.pack(side=tk.BOTTOM, padx=5, pady=5)

# Timer tab
timer_frame = ttk.Frame(notebook)
notebook.add(timer_frame, text='Timer')

# Timer buttons
timer_buttons_frame = ttk.Frame(timer_frame)
timer_buttons_frame.pack(pady=20)


def start_10_minutes():
    start_timer(10)

def start_25_minutes():
    start_timer(25)

def start_30_minutes():
    start_timer(30)

button_10_minutes = tk.Button(timer_buttons_frame, text='10 minutes', command=start_10_minutes)
button_10_minutes.pack(side=tk.LEFT, padx=10)

button_25_minutes = tk.Button(timer_buttons_frame, text='25 minutes', command=start_25_minutes)
button_25_minutes.pack(side=tk.LEFT, padx=10)

button_30_minutes = tk.Button(timer_buttons_frame, text='30 minutes', command=start_30_minutes)
button_30_minutes.pack(side=tk.LEFT, padx=10)

# Display timer label (replace with a countdown timer)
timer_label = tk.Label(timer_frame, text='00:00', font=('Consolas', 60), pady=50)
start_pause_button = tk.Button(timer_frame, text='Start/Pause', command=toggle_timer)
start_pause_button.pack()
timer_label.pack()

root.mainloop()
