#!/usr/bin/python
# encoding: utf-8
import sys
from workflow import Workflow


def main(wf):
    # Get args from Workflow as normalized Unicode
    args = wf.args

    # Do stuff here ...
    hostname = args[0].split(' ')[0]
    connection = ' '.join(args[0].split(' ')[1:])
    wf.settings[hostname] = connection


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
