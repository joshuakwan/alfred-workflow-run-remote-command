#!/usr/bin/python
# encoding: utf-8
import sys
from workflow import Workflow

def main(wf):
    # Get args from Workflow as normalized Unicode
    args = wf.args

    # Do stuff here ...
    hostname = args[0].split(' ')[0]
    command = ' '.join(args[0].split(' ')[1:])
    raw_conn = wf.settings[hostname]
    connection = raw_conn[1:(len(raw_conn) - 1)]
    wf.add_item(title='Execute %s on %s' % (command, hostname),
                subtitle='%s "%s"' % (connection, command),
                arg='%s "%s"' % (connection, command),
                valid=True)
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
