"""org2ical

Usage:
    org2ical <org_name> [<ics_name>]
    org2ical -i <org_name> [-o <ics_name>]

Options:
    -i <org_name>   : target org file
    -o <ics_name>   : output ics file
"""
import os
from datetime import datetime
import org2ical
from docopt import docopt

def main(org_name, ics_name):
    orgstr = ""
    with open(org_name) as f:
        orgstr = f.read()
    tz = datetime.now().astimezone().tzinfo
    ical, w = org2ical.loads(orgstr, to_tz=tz)
    assert w == []
    with open(ics_name, mode='w') as f:
        f.write(ical)


def get_org_name(args):
    res = ""
    if args["-i"]:
        res = args["-i"]
    elif args["<org_name>"]:
        res = args["<org_name>"]
    name, ext = os.path.splitext(res)
    if ext != ".org":
        res = name + ".org"
    return res


def get_ical_name(args):
    res = ""
    if args["-o"]:
        res = args["-o"]
    elif args["<ics_name>"]:
        res = args["<org_name>"]
    else:
        res = get_org_name(args)
    name, ext = os.path.splitext(res)
    if ext != ".ics":
        res = name + ".ics"
    return res


if __name__ == "__main__":
    args = docopt(__doc__)
    org_name = get_org_name(args)
    ics_name = get_ical_name(args)
    main(org_name, ics_name)
