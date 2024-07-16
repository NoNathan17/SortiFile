import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import main


def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_path.set(directory)

def organize_files():
    directory = Path(directory_path.get())
    try:
        main.determine_file(directory)
        messagebox.showinfo('Success!', 'Files sorted successfully!')
    except FileNotFoundError:
        messagebox.showerror('File Not Found.', 'The directory given does not exist.')
    except Exception as e:
        messagebox.showerror('There was an error.', e)

root = tk.Tk()
root.title('File Organizer')
root.geometry('500x150')

directory_path = tk.StringVar()

label = tk.Label(root, text="Select Directory:")
label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry = tk.Entry(root, textvariable=directory_path, width=50)
entry.grid(row=0, column=1, padx=10, pady=10)

browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.grid(row=0, column=2, padx=10, pady=10)

organize_button = tk.Button(root, text="Organize Files", command=organize_files)
organize_button.grid(row=1, column=0, columnspan=3, pady=20)

root.mainloop()