import os
import json
import glob

from binder import Binder
from note import Note

DEBUG = True

from pathlib import Path


script_dir = Path(__file__).parent.absolute()
save_directory = str(script_dir) + '/save/'
# print('save_directory', save_directory)




def save_binder(binder):
    savefile = save_directory+str(binder.name) + '.binder'
    
    if DEBUG:
        print('\nSaving binder to:', savefile, '\n')
    try:
        with open(savefile, 'w') as f:
            json.dump(binder.to_dict(), f, indent=2)

            f.write('\n')

            for note in binder.notes:
                json.dump(note.to_dict(), f, indent=2)
                f.write('\n')
    except Exception as e:
        print('Saving binder Failed:', e)


def save_binders(binders):
    os.makedirs(save_directory, exist_ok=True)

    for binder in binders:
        save_binder(binder)


############


def load_binder(binder_filepath):
    if DEBUG:
        print('binder_filepath:', binder_filepath)

    try:
        with open(binder_filepath, 'r') as file:
            data = file.read()
            
            if DEBUG:
                print('Loaded Binder Data:\n', data)
    except Exception as e:
        print('Exception reading data:', e)

    print('data:', data)

    binder = Binder()
    binder.from_dict(data)

    return binder


def load_binders():
    binders = []

    binder_file_pattern = os.path.join(save_directory, '*.binder')
    binders_filelist = glob.glob(binder_file_pattern, recursive=True)

    if DEBUG:
        print('binders_filelist:', binders_filelist)

    for binder_filepath in binders_filelist:
        print('binder_filepath:', binder_filepath)
        binders.append(load_binder(binder_filepath))

    print('\nLoaded Binders:')
    for binder in binders:
        print(binder)
        print(binder.notes)

    return binders