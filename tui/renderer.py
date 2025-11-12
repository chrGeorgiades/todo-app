import curses


class Renderer():
    def __init__(self, tui):
        self.tui = tui
        
        self.cursor_height = 0
        self.cursor_width = 0
        
        self.stdscr = None

        self.current_selection = 0


    def write_line(self, text, middle_align=False, right_align=False, use_bold=False, increment_cursor=True):
        height, width = self.stdscr.getmaxyx()
        
        # self.cursor_width = 0
        if middle_align:
            self.cursor_width = (width - len(text)) // 2
        elif right_align:
            self.cursor_width = (width - len(text))

        if use_bold:
            self.stdscr.addstr(self.cursor_height, self.cursor_width, text, curses.A_BOLD)
        else:
            # self.cursor_height = 0
            print('Cursor Height:', self.cursor_height)
            print('Text:', text)
            self.stdscr.addstr(self.cursor_height, self.cursor_width, text)

        if increment_cursor:
            self.cursor_height += 1
            self.cursor_width = 0
        else:
            self.cursor_width += len(text)


    def draw_binder_header(self):
        # self.write_line(self.tui.open_binder.name)

        for binder in self.tui.binders:
            if binder == self.tui.open_binder:
                self.write_line(binder.name + ' | ', increment_cursor=False, use_bold=True)
            else:
                self.write_line(binder.name + ' | ', increment_cursor=False)
        
        self.write_line('')

        for binder in self.tui.binders:
            if binder == self.tui.open_binder:
                self.write_line((len(binder.name) + 3) * '-', increment_cursor=False, use_bold=True)
            else:
                self.write_line((len(binder.name) + 3) * '-', increment_cursor=False)
        
        self.write_line('')


    # def draw stat
    # def draw_statisti
    def draw_header(self):
        """Draw the application header"""
        height, width = self.stdscr.getmaxyx()

        print('self.cursor_height:', self.cursor_height)
        
        # Arch Linux themed header
        header_text = "todo-app"
        #self.stdscr.addstr(self.cursor_height, (width - len(header_text)) // 2, header_text, curses.A_BOLD)
        self.write_line(header_text, increment_cursor = False)

        
    #     # Filter info
    #     # filter_text = f"Filter: {self.filter_mode.upper()}"
    #     # self.stdscr.addstr(1, 2, filter_text, curses.A_UNDERLINE)
        
        # Statistics
        total = len(self.tui.open_binder.notes)
        completed = len([t for t in self.tui.open_binder.notes if t.completed])
        stats_text = f"Tasks: {total} | Completed: {completed} | Pending: {total - completed}"
        #self.stdscr.addstr(self.cursor_height, width - len(stats_text) - 2, stats_text)
        self.write_line(stats_text, right_align=True)
        
        #self.cursor_height += 1
        self.draw_help_text()

        ## Separator
        #self.stdscr.addstr(self.cursor_height+2, 0, "=" * width, curses.A_BOLD)
        #self.cursor_height += 1
        #self.stdscr.addstr(self.cursor_height, 0, "=" * width, curses.A_BOLD)
        self.write_line("=" * width, use_bold=True)
        #self.cursor_height += 1
    #     self.cursor_height = self.cursor_height + 4

        self.draw_binder_header()


    def draw_todo_list(self):
        height, width = self.stdscr.getmaxyx()
        #filtered_notes = self.open_binder.get_filtered_notes()
        filtered_notes = self.tui.open_binder.notes
        
        # print('filtered_notes:\n', filtered_notes)

        if not filtered_notes:
            no_tasks_msg = "No tasks found. Press 'a' to add a new task!"
            #self.stdscr.addstr(self.cursor_height, (width - len(no_tasks_msg)) // 2, no_tasks_msg)
            self.write_line(no_tasks_msg, middle_align=True)
            return 

        # self.write_line(self.tui.open_binder.name)
        for i, note in enumerate(filtered_notes):
            # if self.cursor_height > height:
            #     break

            # # Priority colors
            # priority_color = curses.color_pair(1)  # Default (medium)
            # if note.priority == "high":
            #     priority_color = curses.color_pair(2) | curses.A_BOLD  # Red
            # elif note.priority == "low":
            #     priority_color = curses.color_pair(3)  # Green

            if i == self.current_selection:
                self.write_line(str(note), use_bold = True)
            else:
                self.write_line(str(note))

            if self.cursor_height >= height:
                break
        #     if len(todo_line) > width - 10:
        #         todo_line = todo_line[:width-13] + "..."
            
        #     # # Display priority badge
        #     # priority_badge = f"[{note.priority[0].upper()}]"
        #     # self.stdscr.addstr(row, 2, priority_badge, priority_color | attr)
            
        #     # Display todo item
        #     self.stdscr.addstr(row, 6, status, status_color | attr)
        #     self.stdscr.addstr(row, 8, todo_line[8:], attr)
            
        #     # Show creation date for completed tasks
        #     if note.completed:
        #         date_str = f" ({note.created_at})"
        #         if len(todo_line) + len(date_str) < width - 2:
        #             self.stdscr.addstr(row, len(todo_line) + 8, date_str, curses.A_DIM)

        # return self.cursor_height + len(filtered_notes) + 1


    # def draw_footer(self, self.stdscr, cursor_height):
    #     """Draw the application footer with help"""
    #     height, width = self.stdscr.getmaxyx()
        
    #     # Separator
    #     self.stdscr.addstr(height - 4, 0, "=" * width, curses.A_BOLD)
        
        
        # help_text = " | ".join([f"{key}: {desc}" for key, desc in help_items])
        # if len(help_text) < width:
        #     self.stdscr.addstr(height - 2, (width - len(help_text)) // 2, help_text, curses.A_DIM)


    def draw_help_text(self):
        height, width = self.stdscr.getmaxyx()

        # Help text
        help_items = [
            ("a", "Add Task"),
            ("d", "Delete Task"),
            ("Space", "Toggle Complete"),
            ("f", "Change Filter"),
            ("b", "Add Binder"),
            ("m", "Delete Binder"),
            ("q", "Quit")
        ]
        
        help_text = " | ".join([f"{key}: {desc}" for key, desc in help_items])
        print(help_text)
        if len(help_text) < width:
            self.write_line(help_text, middle_align = True)
            #self.stdscr.addstr(self.cursor_height, (width - len(help_text)) // 2, help_text, curses.A_DIM) 


    def show_add_note_dialog(self, stdscr):
        """Show dialog to add new todo"""
        height, width = stdscr.getmaxyx()
        
        # Create a border for the dialog
        dialog_height = 8
        dialog_width = 60
        start_y = (height - dialog_height) // 2
        start_x = (width - dialog_width) // 2
        
        # Draw dialog box
        dialog_win = curses.newwin(dialog_height, dialog_width, start_y, start_x)
        dialog_win.box()
        dialog_win.addstr(1, 2, "Add new Note - " + self.tui.open_binder.name, curses.A_BOLD)
        # self.write_line('Add new Note', use_bold=True)
        dialog_win.addstr(2, 2, "Name:")
        dialog_win.refresh()

        # name = dialog_win.getstr().decode('utf-8')
        
        
        curses.echo()
        dialog_win.addstr(3, 2, " " * (dialog_width - 4))
        dialog_win.addstr(3, 2, "")
        name = dialog_win.getstr().decode('utf-8')
        curses.noecho()
        

        dialog_win.addstr(4, 2, "Description: ")


        # Get description
        curses.echo()
        dialog_win.addstr(5, 2, " " * (dialog_width - 4))
        dialog_win.addstr(5, 2, "")
        description = dialog_win.getstr().decode('utf-8')
        curses.noecho()
        
        if name.strip():
            # Priority selection
            dialog_win.addstr(6, 2, "Priority (h)igh/(m)edium/(l)ow [m]: ")
            dialog_win.refresh()
            priority_key = dialog_win.getch()
            
            priority_map = {ord('h'): 'high', ord('l'): 'low', ord('m'): 'medium'}
            priority = priority_map.get(priority_key, 'medium')
            
            self.tui.open_binder.add_note(name.strip(), description.strip(), priority)


    def show_add_binder_dialog(self, stdscr):
        """Show dialog to add new todo"""
        height, width = stdscr.getmaxyx()
        
        # Create a border for the dialog
        dialog_height = 8
        dialog_width = 60
        start_y = (height - dialog_height) // 2
        start_x = (width - dialog_width) // 2
        
        # Draw dialog box
        dialog_win = curses.newwin(dialog_height, dialog_width, start_y, start_x)
        dialog_win.box()
        dialog_win.addstr(1, 2, "Add new open_binder", curses.A_BOLD)
        # self.write_line('Add new Note', use_bold=True)
        dialog_win.addstr(2, 2, "Name:")
        dialog_win.refresh()

        # name = dialog_win.getstr().decode('utf-8')
        
        
        curses.echo()
        dialog_win.addstr(3, 2, " " * (dialog_width - 4))
        dialog_win.addstr(3, 2, "")
        name = dialog_win.getstr().decode('utf-8')
        curses.noecho()
        

        # dialog_win.addstr(4, 2, "Description: ")


        # # Get description
        # curses.echo()
        # dialog_win.addstr(5, 2, " " * (dialog_width - 4))
        # dialog_win.addstr(5, 2, "")
        # description = dialog_win.getstr().decode('utf-8')
        # curses.noecho()
        name_strip = name.strip()
        if name_strip:
            for binder in self.tui.Binders:
                if name_strip == binder.name:
                    return
            # Priority selection
            # dialog_win.addstr(6, 2, "Priority (h)igh/(m)edium/(l)ow [m]: ")
            # dialog_win.refresh()
            # priority_key = dialog_win.getch()
            
            # priority_map = {ord('h'): 'high', ord('l'): 'low', ord('m'): 'medium'}
            # priority = priority_map.get(priority_key, 'medium')
            
            # self.open_binder.add_todo(name.strip(), description.strip(), priority)
            self.tui.add_binder(name.strip())