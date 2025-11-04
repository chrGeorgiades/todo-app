from binder import Binder
from note import Note


import os
import glob

import json

save_directory = './save/'

DEBUG = True


def delete_note(note):
    # note.binder_directory = save_directory + binder.name + '/'
    savefile = note.binder_directory+str(note.name) + '.note'

    if os.path.exists(savefile):
        os.remove(savefile)
        print("File", savefile, "successfully.")


def _save_note(note, binder):
    savefile = binder.binder_directory+str(note.name) + '.note'
    
    print('\nSaving Note to:', savefile, '\n')
    try:
        with open(savefile, 'w') as f:
            json.dump(note.to_dict(), f, indent=2)   
    except Exception as e:
        print('Saving Note Failed:', e)


def save_binder(binder : Binder):
    os.makedirs(save_directory, exist_ok=True)
    os.makedirs(binder.binder_directory, exist_ok=True)

    savefile = binder.binder_directory+str(binder.name) + '.binder'
    
    print('\nSaving binder to:', savefile, '\n')
    try:
        with open(savefile, 'w') as f:
            json.dump(binder.to_dict(), f, indent=2)
    except Exception as e:
        print('Saving binder Failed:', e)

    for note in binder.notes:
        _save_note(note, binder)

############

def _load_note(note_filepath):

    with open(note_filepath, 'r') as file:
        data = json.load(file)
        print('Loaded note Data:', data)

    note = Note()
    note.from_dict(data)

    return note


def _load_notes(binder_directory):
    pattern = os.path.join(binder_directory, '*.note')
    print('pattern:', pattern)
    notes_files = glob.glob(pattern, recursive=True)
    
    notes = []
    for note_filepath in notes_files:
        note = _load_note(note_filepath)
        notes.append(note)
    
    return notes


def _load_binder(binder_name):
    binder_directory = save_directory + binder_name + '/'
    binder_filepath = binder_directory + binder_name + '.binder'

    try:
        with open(binder_filepath, 'r') as file:
            data = json.load(file)
            print('Loaded Binder Data:', data)
    except Exception as e:
        return None

    notes = _load_notes(binder_directory)
    print('Loaded notes:',notes)
    binder = Binder()
    print('Loaded binder:', binder)
    binder.from_dict(data, notes)
    print('Loaded binder:', binder)
    return binder


def load_binder(binder_name : str):
    binder = _load_binder(binder_name)

    return binder