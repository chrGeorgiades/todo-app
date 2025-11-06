import curses

from tui.renderer import Renderer
from tui.input import Input

from pathlib import Path

from binder import Binder
from note import Note


class TUI:
    def __init__(self, binder = None):
        if binder == None:
            self.binder = Binder()
        else:
            self.binder = binder 

        self.renderer = Renderer(self.binder)
        self.input = Input(self, self.renderer)


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
            self.renderer.cursor_height = 0

            stdscr.clear()
            height, width = stdscr.getmaxyx()
            
            self.cursor_height = 0

            # Draw UI components
            self.renderer.draw_header()
            list_end_row = self.renderer.draw_todo_list()
            # self.renderer.draw_footer(self, stdscr, list_end_row)
            
            stdscr.refresh()
            
            self.input.handle_input(stdscr)