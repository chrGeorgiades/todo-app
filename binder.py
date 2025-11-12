import json
import os
from datetime import datetime
from pathlib import Path

from note import Note

script_dir = Path(__file__).parent.absolute()
# print('script_dir', script_dir)

save_directory = str(script_dir) + '/save/'

DEBUG = False


class Binder:
    filter_mode = "all"  # "all", "pending", "completed"

    def __init__(self, name = 'binder1', completed = False):
        self.name = name
        self.completed = completed
        self.notes = []

        print('Binder', self.name, 'created')


    def from_dict(self, data):
        data_split = data.split('}\n')[:-1]

        if DEBUG:
            print('data:', data)
            print('data split:', data_split)
        
        for i in range(len(data_split)):
            if data_split[i]:
                data_split[i] += '}'
        
        binder_data = data_split[0]
        binder_json = json.loads(binder_data)
        self.name=binder_json.get('name')
        self.completed=bool(binder_json.get('completed'))
        self.filter_mode = str(binder_json.get('filter_mode'))

        notes_data = data_split[1:]
        if DEBUG:
            print('notes_data:', notes_data)
        
        for note_data in notes_data:
            note = Note()
            note.from_dict(note_data)
            self.notes.append(note)

        if DEBUG:
            print('self.name:', self.name)
            print('notes:', self.notes)
            print()

        print('Loaded binder:', self.name)


    def to_dict(self):
        # Convert Note object to dictionary for serialization"""
        return {
            'name': self.name,
            'completed': self.completed,
            'filter_mode': self.filter_mode,
        }


    def get_filtered_notes(self):
        return self.notes
        # """Get notes based on current filter"""
        # if self.filter_mode == "pending":
        #     return [todo for todo in self.notes if not todo["completed"]]
        # elif self.filter_mode == "completed":
        #     return [todo for todo in self.notes if todo["completed"]]
        # return self.notes


    def add_note(self, name='', description='', priority="medium"):
        new_note = Note(name=name, description=description, priority=priority)
        self.notes.append(new_note)


    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            note = self.notes.pop(index)
            # if self.current_selection >= len(self.notes) and self.notes:
            #     self.current_selection = len(self.notes) - 1
            
            # note.delete(self.binder_directory)
            del note


    def delete(self):
        savefile = save_directory+str(self.name) + '.binder'
        print('Savefile to be deleted:', savefile)
        if os.path.exists(savefile):
            os.remove(savefile)
            print("File", savefile, "deleted successfully.")


    def __str__(self):
        #string ='Governor: ' + self.governor + '\n' + \
        #string = self.name + '\n' #+ '\n'.join(map(str, self.notes))
        string = str(self.name)
        return string