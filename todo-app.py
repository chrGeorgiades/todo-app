import os

import curses

import tui.tui as tui
from binder import Binder

import serialization

save_directory = './save/'


def main():   
    binders = serialization.load_binders()
    if len(binders) == 0:
        binders.append(Binder())

    # print('Binders:', binders)

    app = tui.TUI(binders[0])
    curses.wrapper(app.run)

    serialization.save_binders(binders)

    print('Goodbye')

if __name__ == "__main__":
    main()