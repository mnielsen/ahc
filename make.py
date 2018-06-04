"""make.py
~~~~~~~~~~

Read in the files in the configuration variables `files` and processes
them, putting the results into the subdirectory `directory`.

The processing is to take strings like {% name %} and replace them by
the file named `name`.

Note that name must be unique - it can only occur once in the file.

This is a good way of factoring out common elements like headers,
footers, and sidebars.

"""

import re

files = ["ltm.html"]
directory = "public"

for name in files:
    f = open(name, "r")
    text = f.read()
    matches = re.findall(r'\{\%.+?\%\}', text)
    for match in matches:
        subfilename = match[2:-2].strip()
        g = open(subfilename, "r")
        subfile_text = g.read()
        g.close()
        text = text.replace(match, subfile_text)
    f.close()
    h = open(directory+"/"+name, "w")
    h.write(text)
        
