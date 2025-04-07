from tkinter import *
from tkinter import ttk

class DailyDigestGUI:
    # pyinstaller -w -F .\dd_gui.py
    # creates an app
    # -w : not opening console window
    # -F : One file bundlered executable created
    # .\dd_gui.py :  enterance of program 

    def __init__(self, root):
        pass # build the GUI

    """
    The GUI should enable the admin to...
        - configure which content sources to include in email
        - add recipients
        - remove recipients
        - schedule daily time to send email
        - configure sender credentials
    """

if __name__ == '__main__':
    root = Tk()
    app = DailyDigestGUI(root)
    root.mainloop()