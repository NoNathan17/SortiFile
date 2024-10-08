import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
import main

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_path.set(directory)

def organize_files():
    directory = Path(directory_path.get())
    sort_by = sorting_method.get()
    if str(directory).strip() == '.':
        messagebox.showerror('Error', 'Please specific a directory.')
    else:
        try:
            main.determine_file(directory, sort_by)
            messagebox.showinfo('Success!', 'Files sorted successfully!')
        except FileNotFoundError:
            messagebox.showerror('Error', 'The specified directory does not exist.')
        except PermissionError:
            messagebox.showerror('Error', 'Permission denied. You do not have access to edit this directory.')
        except Exception as e:
            messagebox.showerror('Error', e)

root = tk.Tk()
root.title('File Organizer')
root.geometry('535x250')

directory_path = tk.StringVar()
sorting_method = tk.StringVar(value="extension")

label = ttk.Label(root, text="Select Directory:")
label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry = ttk.Entry(root, textvariable=directory_path, width=50)
entry.grid(row=0, column=1, padx=10, pady=10)

browse_button = ttk.Button(root, text="Browse", command=browse_directory)
browse_button.grid(row=0, column=2, padx=10, pady=10)

sort_by_label = ttk.Label(root, text="Sort files by:")
sort_by_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

sort_by_extension = ttk.Radiobutton(root, text="Extension", variable=sorting_method, value="extension")
sort_by_extension.grid(row=1, column=1, padx=10, pady=10, sticky="w")

sort_by_date = ttk.Radiobutton(root, text="Date Created", variable=sorting_method, value="date")
sort_by_date.grid(row=2, column=1, padx=10, pady=10, sticky="w")

organize_button = ttk.Button(root, text="Organize Files", command=organize_files)
organize_button.grid(row=3, column=0, columnspan=3, pady=20)
