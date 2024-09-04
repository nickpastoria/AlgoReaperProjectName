# main.py
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import json

file = open("config.json")
config = json.load(file)
file.close()


def write_config():
    with open("config.json", "w") as outfile:
        json.dump(config, outfile)


def find_temp_dir(*args):
    try:
        dirname = filedialog.askdirectory()
        template_dir.set(dirname)
    except ValueError:
        pass


def find_output_dir(*args):
    try:
        dirname = filedialog.askdirectory()
        output_dir.set(dirname)
    except ValueError:
        pass


root = Tk()
root.title("Project Maker")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

template_dir = StringVar()
template_dir.set(config["template_dir"])

output_dir = StringVar()
output_dir.set(config["project_dir"])

file_name = StringVar()
file_name.set(config["default_filename"])

is_demo = BooleanVar()
is_demo.set(config["isdemo"])

ttk.Label(mainframe, text="Template Directory:").grid(column=1, row=1, sticky=W)
template_entry = ttk.Entry(mainframe, width=75, textvariable=template_dir).grid(
    column=2, row=1, sticky=W
)

template_button = ttk.Button(mainframe, text="Find Dir", command=find_temp_dir).grid(
    column=3, row=1, sticky=W
)


root.mainloop()
