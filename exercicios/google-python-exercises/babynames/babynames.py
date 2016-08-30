#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import fnmatch

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    file_text = open(filename, 'r').read()
    p = re.compile(r'Popularity in (\d*)|<td>(\d*)<\/td><td>(\w*)<\/td><td>(\w*)<\/td>')
    lp = p.findall(file_text)

    l = [lp.pop(0)[0]]
    for _, rank, male_name, female_name in lp:
        l.append('{0} {1}'.format(male_name, rank))
        l.append('{0} {1}'.format(female_name, rank))
    l.sort()
    return l


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

        l = []
        for f in args:
            if f.count('*'):
                for file in os.listdir('.'):
                    if fnmatch.fnmatch(file, f):
                        if summary:
                            new_file = open(file + '.summary', 'w')
                            new_file.write('\n'.join(extract_names(file)))
                        else:
                            l += extract_names(file)
            else:
                if summary:
                    new_file = open(f + '.summary', 'w')
                    new_file.write('\n'.join(extract_names(f)))
                else:
                    l += extract_names(f)

        if not summary:
            print('\n'.join(l))

if __name__ == '__main__':
    main()
