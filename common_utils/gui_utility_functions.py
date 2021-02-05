#######################################################################
#   The advantage of Tk that it is included with the Python standard library, due to this, you don’t need to install it.
#   Create a Tkinter GUI follow the step
#   1)  To start firstly Import the module – Tkinter
#   2)  Create the main window which is done by two methods.
#   3)  When the main window is created add a number of widgets to it.
#   4)  Implement the function trigger on the widgets.
########################################################################
import platform
import tkinter as tk
from tkinter import *
from tkinter import messagebox

os_name = platform.system()


def message_box_only(title, message):
    messagebox.showinfo(title, message)


class GuiUtility:
    window: tk

    def __init__(self, title_name, text_font, text_size, col, row, win_size, logging):
        self.WinTitle = title_name  # Window title name
        self.font = (text_font, text_size)
        self.gridCol = col
        self.gridRow = row
        self.window_size = win_size
        self.entries_dict = {}
        self.buttons_dict = {}
        self.logging = logging
        self.logging.dbg_logging("INFO::GUI object created:{gui_name}".format(gui_name=title_name))

    def collect_entries_texts(self, entries):
        str_list = entries.keys()
        self.entries_dict.clear()
        for key in str_list:
            entry = entries.get(key)
            text = entry.get()
            self.entries_dict.update({key: text})
            self.logging.dbg_logging('INFO::%s: "%s"' % (key, text))
        self.window.destroy()

    def create_entries(self, str_dict):
        entries = {}
        str_list = str_dict.keys()
        for entry in str_list:
            row = tk.Frame(self.window)
            lab = tk.Label(row, width=15, text=entry, anchor='w')
            ent = tk.Entry(row)
            ent.insert(10, str_dict.get(entry))
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries.update({entry: ent})
        return entries

    def create_buttons(self, root, str_list, ent_dict):
        btn_list = []
        for btn in str_list:
            btn = tk.Button(self.window, text=btn, command=(lambda e=ent_dict: self.collect_entries_texts(e)))
            btn.pack(side=tk.LEFT, padx=5, pady=5)
            btn_list.append(btn)
        return btn_list

    # This window will close by itself depends on the timeout, if timeout is 0, then user close needed
    def open_info_window(self, message, timeout):
        self.window = tk.Tk()
        self.window.geometry(self.window_size)  # Let Tk to auto-size the window
        self.window.title(self.WinTitle)
        lbl = Label(self.window, text=message, font=self.font)
        lbl.grid(column=self.gridCol, row=self.gridRow)
        if timeout != 0:
            self.window.after(timeout, lambda: self.window.destroy())  # Destroy the widget after 30 seconds
        self.logging.dbg_logging('INFO::%s is called with :"%s"' % (__name__, message))
        self.window.mainloop()

    # This window will close after it get the entry data
    def open_entry_window(self, entry_texts_dict, button_texts):
        self.window = tk.Tk()
        ent_dict = self.create_entries(entry_texts_dict)
        self.window.bind('<Return>', (lambda event, e=ent_dict: self.collect_entries_texts(e)))
        butts = self.create_buttons(self.window, button_texts, ent_dict)
        self.window.mainloop()
        return self.entries_dict

    def close_this_window(self):
        frame = Frame(self.window)
        frame.pack()
        # destroy all widgets from frame
        for widget in frame.winfo_children():
            widget.destroy()
        # this will clear frame and frame will be empty
        # if you want to hide the empty panel then
        frame.pack_forget()
