import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def getExtension(file):
    return os.path.splitext(file)[1][1:]

def organizeAll():
    path = path_entry.get()
    
    if not os.path.isdir(path):
        messagebox.showerror("Error", "Invalid Directory Path")
        return

    all_files = os.listdir(path)
    ext_list = []
    file_no = 0

    for file in all_files:
        cur_ext = getExtension(file)
        new_path = os.path.join(path, cur_ext)
        if cur_ext != "":
            if cur_ext not in ext_list and not os.path.exists(new_path):
                os.mkdir(new_path)
                ext_list.append(cur_ext)
            shutil.move(os.path.join(path, file), os.path.join(new_path, file))
            file_no += 1

    messagebox.showinfo("Success", f"{file_no} files organized!")

def browseFolder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, folder_selected)

app = tk.Tk()
app.title("File Organizer")

path_label = tk.Label(app, text="Enter Path or Browse:")
path_label.pack(pady=5)

path_entry = tk.Entry(app, width=50)
path_entry.pack(pady=5)

browse_button = tk.Button(app, text="Browse", command=browseFolder)
browse_button.pack(pady=5)

organize_button = tk.Button(app, text="Organize Files", command=organizeAll)
organize_button.pack(pady=20)

app.geometry("400x200")
app.mainloop()  