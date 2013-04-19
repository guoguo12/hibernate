#!/usr/bin/env python

"""hibernate.py: Engages Windows Hibernate after a given period of time."""

__author__  = "Allen Guo"
__license__ = "GNU GPLv3"
__version__ = "1.0"

from os import system
from time import sleep

HEADER = "** Windows Hibernate Countdown **"

def countdown(duration):
    system('color c')
    while duration > 0:
        system('cls')
        print HEADER
        print "This computer is scheduled to hibernate in", duration, "seconds."
        sleep(1)
        duration -= 1
    system('cls')
    print HEADER
    print "Countdown complete."

def main():
    system('color a && cls')
    print HEADER
    countdown(int(raw_input("Seconds until hibernation? ")))
    system('shutdown -h')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print "Python exception:", str(e) + '.'
    except:
        system('cls')
        print HEADER
    system('color f')
    print "Windows Hibernate Countdown terminated."
