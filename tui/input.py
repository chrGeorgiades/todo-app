import curses


class Input():
    def __init__(self, tui, renderer):
        self.tui = tui
        # self.open_binder = tui.open_binder
        self.renderer = renderer
        self.stdscr = None
    

    def handle_input(self, stdscr):
        # Handle input
        key = stdscr.getch()
        
        if key in [ord('q'), ord('Q')]:  # Quit
            self.tui.quit()
        elif key in [ord('a'), ord('A')]:  # Add todo
            self.renderer.show_add_note_dialog(stdscr)
        elif key in [curses.KEY_UP, ord('k')]:  # Move up
            filtered_len = len(self.tui.open_binder.get_filtered_notes())
            if filtered_len > 0:
                self.renderer.current_selection = (self.renderer.current_selection - 1) % filtered_len
        elif key in [curses.KEY_DOWN, ord('j')]:  # Move down
            filtered_len = len(self.tui.open_binder.get_filtered_notes())
            if filtered_len > 0:
                self.renderer.current_selection = (self.renderer.current_selection + 1) % filtered_len
        
        elif key in [ord(' '), curses.KEY_ENTER, 10, 13]:  # Toggle completion
            filtered_notes = self.tui.open_binder.get_filtered_notes()
            if filtered_notes:
                actual_index = self.tui.open_binder.notes.index(filtered_notes[self.renderer.current_selection])
                self.tui.open_binder.notes[actual_index].toggle_completion()
        elif key in [ord('d'), ord('D')]:  # Delete todo
            filtered_todos = self.tui.open_binder.get_filtered_notes()
            if filtered_todos:
                actual_index = self.tui.open_binder.notes.index(filtered_todos[self.renderer.current_selection])
                self.tui.open_binder.delete_note(actual_index)
        
        elif key in [ord('b'), ord('B')]:  # Create binder
            self.renderer.show_add_binder_dialog(stdscr)
        
        elif key in [ord('m'), ord('M')]:  # Create binder
            # self.renderer.show_add_binder_dialog(stdscr)
            self.tui.delete_binder()

        elif key in [curses.KEY_RIGHT]:  # Next binder
            index = self.tui.binders.index(self.tui.open_binder)
            
            new_index = (index + 1)
            if new_index > len(self.tui.binders) - 1:
                new_index = 0
            
            # print('new_index:', new_index)
            self.tui.open_binder = self.tui.binders[new_index]
        elif key in [curses.KEY_LEFT]:  # Previous Binder
            index = self.tui.binders.index(self.tui.open_binder)
            
            new_index = (index - 1)
            if new_index < 0:
                new_index = len(self.tui.binders) - 1
            
            self.tui.open_binder = self.tui.binders[new_index]