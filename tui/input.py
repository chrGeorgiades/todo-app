import curses

import tui.dialog as Dialog

class Input():
    def __init__(self, tui, renderer):
        self.tui = tui
        self.binder = tui.binder
        self.renderer = renderer
        self.stdscr = None
    

    def handle_input(self, stdscr):
        # Handle input
        key = stdscr.getch()
        
        if key in [ord('q'), ord('Q')]:  # Quit
            self.tui.quit()
        elif key in [ord('a'), ord('A')]:  # Add todo
            self.renderer.show_add_todo_dialog(stdscr)
        elif key in [curses.KEY_UP, ord('k')]:  # Move up
            filtered_len = len(self.binder.get_filtered_notes())
            if filtered_len > 0:
                self.renderer.current_selection = (self.renderer.current_selection - 1) % filtered_len
        elif key in [curses.KEY_DOWN, ord('j')]:  # Move down
            filtered_len = len(self.binder.get_filtered_notes())
            if filtered_len > 0:
                self.renderer.current_selection = (self.renderer.current_selection + 1) % filtered_len
        
        elif key in [ord(' '), curses.KEY_ENTER, 10, 13]:  # Toggle completion
            filtered_notes = self.binder.get_filtered_notes()
            if filtered_notes:
                actual_index = self.binder.notes.index(filtered_notes[self.renderer.current_selection])
                self.binder.notes[actual_index].toggle_completion()
        elif key in [ord('d'), ord('D')]:  # Delete todo
            filtered_todos = self.binder.get_filtered_notes()
            if filtered_todos:
                actual_index = self.binder.notes.index(filtered_todos[self.renderer.current_selection])
                self.binder.delete_note(actual_index)
        # elif key in [ord('f'), ord('F')]:  # Change filter
        #     self.show_filter_menu(stdscr)