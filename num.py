#!/usr/local/bin/python

import datetime;
import cgi;
import cgitb; cgitb.enable();  # for troubleshooting
import vin

def PrintHeaders():
        print "Content-Type: text/html" # HTML is following
        print # blank line, end of headers
        print "<html><body>"
        print """<meta name="viewport" content="width=440, initial-scale=1.0, user-scalable=no"/>"""


def PrintFooter():
        print "</body></html>"


def Main():

        PrintHeaders()

        print "<strong>Random Vins:</strong><p/>"
        for i in range(5):
                print "<p>%s</p>" % (vin.getRandomVin())


        PrintFooter()

Main()
