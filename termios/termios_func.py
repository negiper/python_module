#!/usr/bin/env python

import os
import sys

def wait_key():
    '''Wait for an any key press on the console and return it.'''
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getch()

    else:
        import termios
        fd = sys.stdin.fileno()

        oldattr = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldattr)

    return result


__all__ = ['wait_key']
