#!/usr/bin/env python
"""Basic script to print hostname using nxtoolkit1."""

import nxtoolkit as NX
import sys

username = 'admin'
password = 'Cisc0123'
device = 'http://192.168.1.103/'


def main():
    """Simple main method to retrieve hostname."""
    session = NX.Session(device, username, password)
    session.login()
    print("This NX-OS device has the following hostname:")
    print(session.get('/api/mo/sys.json').json()
          ['imdata'][0]['topSystem']['attributes']['name'])


if __name__ == '__main__':
    sys.exit(main())

