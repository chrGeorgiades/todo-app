import curses

from tui.renderer import Renderer
from tui.input import Input

from pathlib import Path

from binder import Binder
from note import Note

import serialization

class TUI:
    def __init__(self):
        self.binders = serialization.load_binders()

        if len(self.binders) > 0:
            self.open_binder = self.binders[0]
        else:
            self.open_binder = Binder()
            self.binders.append(self.open_binder)

        self.renderer = Renderer(self)
        self.input = Input(self, self.renderer)


    def add_binder(self, name):
        new_binder = Binder(name=name)
        self.binders.append(new_binder)


    def delete_binder(self):
        index = self.binders.index(self.open_binder)
        binder_del = self.binders.pop(index)

        binder_del.delete()
        del binder_del

        if index - 1 > 0:
            
            self.open_binder = self.binders[index-1]
        else:
            if len(self.binders) == 0:
                self.open_binder = Binder()
                self.binders.append(self.open_binder)
            else:
                self.open_binder = self.binders[index]


    def quit(self):
        self.running = False


    def run(self, stdscr):
        """Main application loop"""
        # Initialize colors
        curses.curs_set(0)  # Hide cursor
        stdscr.keypad(True)  # Enable special keys

        self.renderer.stdscr = stdscr
        self.input.stdscr = stdscr
        
        self.running = True
        while self.running:
            stdscr.clear()
            height, width = stdscr.getmaxyx()
            
            self.renderer.cursor_height = 0
            self.cursor_height = 0

            # Draw UI components
            self.renderer.draw_header()
            self.renderer.draw_todo_list()
            
            stdscr.refresh()
            
            self.input.handle_input(stdscr)

        serialization.save_binders(self.binders)