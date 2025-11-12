import os

import curses

import tui.tui as tui
from binder import Binder

import serialization


def main():   
    # binders = serialization.load_binders()
    # if len(binders) == 0:
    #     binders.append(Binder())
    # print('Binders:', binders)

    # binders = serialization.load_binders()
    # binders[0].add_note(name='Hello')
    # serialization.save_binders(binders)

    app = tui.TUI()
    curses.wrapper(app.run)

    # serialization.save_binders(binders)

    print('Goodbye')


if __name__ == "__main__":
    main()