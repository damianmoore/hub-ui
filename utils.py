"""
Based on: https://docs.python.org/2/faq/library.html#how-do-i-get-a-single-keypress-at-a-time
"""

from contextlib import contextmanager
import os
import sys
import sys
import time

import fcntl
import termios


@contextmanager
def stdin_setup():
    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

    try:
        yield
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

def getch(timeout=0):
    while True:
        c = None
        start = time.time()
        with stdin_setup():
            while True:
                duration = time.time() - start
                if timeout and timeout < duration:
                    break
                try:
                    c = sys.stdin.read(1)
                except IOError:
                    pass
                if c:
                    break
        yield c
