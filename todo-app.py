import curses

import tui.tui as tui
from binder import Binder

import serialization
# if __name__ == "__main__":
#     new_note = note.Note(text="Hello Emily")
#     print(new_note)


#def create_binder():

save_directory = './save/'

import os

def main():   
    # binder = Binder()
    # print('binder:\n', binder)

    # # binder.add_todo('note3', 'hello')
    # # binder.add_todo('note4', 'yoo')
    # print('binder:\n', binder)

    # serialization.save_binder(binder)
    # binder_load = serialization.load_binder(binder.name)
    # print('binder_load:', binder_load)
    
    # # binder.save_todos()
    # # new_note = note.Note(text="Hello Emily")
    # # print(new_note)

    # binder.delete_note(0)

    binder = serialization.load_binder('binder1')
    if not binder:
        binder = Binder()

    app = tui.TUI(binder)
    curses.wrapper(app.run)

    serialization.save_binder(binder)

    print('Goodbye')

if __name__ == "__main__":
    main()