#!/usr/bin/env python
# -*- encoding: ascii -*-
"""callvim.py

Demonstrates calling a text-editor (e.g. Vim) from within a Python script,
including passing input to the editor and reading output from the editor.
"""

import tempfile
import os
from subprocess import call

# Get the text editor from the shell, otherwise default to Vim
EDITOR = os.environ.get('EDITOR','vim')

# Set initial input with which to populate the buffer
initial_message = "Hello world!"

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
