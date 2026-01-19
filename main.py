import sys
import org2ical

def main():
    orgstr = ""
    with open(sys.argv[1]) as f:
        orgstr = f.read()
    ical, w = org2ical.loads(orgstr)
    assert w == []
    with open(sys.argv[2], mode='w') as f:
        f.write(ical)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(sys.argv[0] + " <org name> <ical name>")
        sys.exit(1)
    main()
