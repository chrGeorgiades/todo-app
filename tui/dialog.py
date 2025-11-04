import curses
   
# def show_add_todo_dialog(self, stdscr):
#         """Show dialog to add new todo"""
#         height, width = stdscr.getmaxyx()
        
#         # Create a border for the dialog
#         dialog_height = 8
#         dialog_width = 60
#         start_y = (height - dialog_height) // 2
#         start_x = (width - dialog_width) // 2
        
#         # Draw dialog box
#         dialog_win = curses.newwin(dialog_height, dialog_width, start_y, start_x)
#         dialog_win.box()
#         dialog_win.addstr(1, 2, "Add new Note", curses.A_BOLD)
#         dialog_win.addstr(2, 2, "Name: ")
#         dialog_win.refresh()
        
#         curses.echo()
#         dialog_win.addstr(4, 2, " " * (dialog_width - 4))
#         dialog_win.addstr(4, 2, "")
#         name = dialog_win.getstr().decode('utf-8')
#         curses.noecho()
        

#         dialog_win.addstr(4, 2, "Description: ")


#         # Get description
#         curses.echo()
#         dialog_win.addstr(6, 2, " " * (dialog_width - 4))
#         dialog_win.addstr(6, 2, "")
#         description = dialog_win.getstr().decode('utf-8')
#         curses.noecho()
        
#         if description.strip():
#             # Priority selection
#             dialog_win.addstr(6, 2, "Priority (h)igh/(m)edium/(l)ow [m]: ")
#             dialog_win.refresh()
#             priority_key = dialog_win.getch()
            
#             priority_map = {ord('h'): 'high', ord('l'): 'low', ord('m'): 'medium'}
#             priority = priority_map.get(priority_key, 'medium')
            
#             self.binder.add_todo(description.strip(), priority)