from tkinter import Tk
from view.main_window import MainWindow


def main():
    root = Tk()
    MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
