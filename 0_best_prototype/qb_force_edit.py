import yaml


"""callvim.py

Demonstrates calling a text-editor (e.g. Vim) from within a Python script,
including passing input to the editor and reading output from the editor.
"""

import tempfile
import os
from subprocess import call


def edit_with_micro(str_record):
    # Get the text editor from the shell, otherwise default to Vim
    EDITOR = os.environ.get('EDITOR','micro')

    # Set initial input with which to populate the buffer
    initial_message = str_record

    # Open a temporary file to communicate through (`tempfile` should avoid any filename conflicts)
    #
    # NOTE: Don't autodelete the file on close!
    #       We want to reopen the file incase the editor uses a swap-file.
    #
    with tempfile.NamedTemporaryFile(suffix=".tmp", mode='w', encoding="utf-8", delete=False) as tf:

        # Write the initial content to the file I/O buffer
        tf.write(initial_message)

        # Flush the I/O buffer to make sure the data is written to the file
        tf.flush()

        # Open the file with the text editor
        call([EDITOR, tf.name])

    # Reopen the file to read the edited data
    with open(tf.name, 'r') as tf:

        # Read the file data into a variable
        edited_message = tf.read()

        # Output the data
        print(edited_message)
        return edited_message



def make_edit_dict(full_dict):
    lil = {}
    lil['Vendor'] = full_dict['Vendor']
    lil['Company'] = full_dict['Company']
    lil['Street Address'] = full_dict['Street Address']
    lil['City'] = full_dict['City']
    lil['State'] = full_dict['State']
    lil['Zip'] = full_dict['Zip']
    return lil


def force_edit(broken_dict):

    edit_dict = make_edit_dict(broken_dict)
    yaml_to_edit = yaml.dump(edit_dict, default_flow_style=False, sort_keys=False)
    new_improved_yaml = edit_with_micro(yaml_to_edit)

    print(new_improved_yaml)


import sys

try:
    # Try to import msvcrt for Windows
    import msvcrt
    getch = msvcrt.getch
except ImportError:
    # If ImportError, import termios for Unix-like systems
    import termios
    import tty
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def edit_or_quit(broken_dict):
    while True:
        print("Press 'e' to edit, 'q' to quit:")
        char = getch().lower()

        if char == 'e':
            print("Editing...")
            # Add your editing logic here
            force_edit(broken_dict)
            break
        elif char == 'q':
            print("Quitting...")
            sys.exit(0)
        else:
            print("Invalid input. Press 'e' to edit, 'q' to quit.")


