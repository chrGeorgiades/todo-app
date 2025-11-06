import os
import json
from datetime import datetime

import curses

DEBUG = False


class Note:
    def __init__(self, name = 'note1', description="", priority="medium", completed=False):
        self.name = name
        self.description = description
        self.priority = priority  # "low", "medium", "high"
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    

    def from_dict(self, data):
        if DEBUG:
            print('data:', data)
        
        data = json.loads(data)
        self.name=data.get('name')
        self.description=data.get('description')
        self.priority = data.get('priority')
        self.completed = data.get('completed')
        self.created_at = data.get('created_at')


    def to_dict(self):
        """Convert Note object to dictionary for serialization"""
        return {
            'name': self.name,
            'description': self.description,
            'priority': self.priority,
            'completed': self.completed,
            'created_at': self.created_at
        }

    
    def toggle_completion(self):
        self.completed = not self.completed


    def delete(self, binder_directory):
        savefile = binder_directory+str(self.name) + '.note'
        print('Savefile to be deleted:', savefile)
        if os.path.exists(savefile):
            os.remove(savefile)
            print("File", savefile, "deleted successfully.")

        # del self


    def __str__(self):
        # Completion status
        status = "✓" if self.completed else "○"
        # Format the todo line
        todo_line = f" {status} {self.name} \t {self.description} \t {self.priority} {self.created_at}"
        string = todo_line
        
        return string