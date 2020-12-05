#!/usr/bin/env python3

"""Usage: rv FILE [options]

Arguments:
  FILE                     File to display.

Options:
  -h, --help               Show this helpful message.
"""

from docopt import docopt


def main():
    args = docopt(__doc__)
    retval = 0

    return retval
