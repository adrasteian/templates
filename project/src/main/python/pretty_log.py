#!/usr/bin/env python2

###############################################################################
# The MIT License (MIT)
#
# Copyright (c) 2021 F. Bar
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
###############################################################################

printer = None

vb = False
db = False

num_debug = 0
num_error = 0
num_info = 0
num_success = 0
num_warning = 0

class Printer:

    def out(self,msg):
        print(msg)

class Esc:

    # Colors...

    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    ORANGE = "\033[38;5;166m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"

    # Styles...

    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"

    END = "\033[0m"

class Prefix:
    DEBUG   = "[DEBUG]  "
    ERROR   = "[ERROR]  "
    INFO    = "[INFO]   "
    NONE    = "         "
    SUCCESS = "[OK]     "
    WARNING = "[WARNING]"

    SEP     = " : "

def init():
    global num_debug
    global num_error
    global num_info
    global num_success
    global num_warning
    num_debug = 0
    num_error = 0
    num_info = 0
    num_success = 0
    num_warning = 0

def set_printer(p):
    global printer
    printer = p

def set_db(debug):
    global db
    db = debug

def set_vb(verbose):
    global vb
    vb = verbose

def out(msg):
    if None==printer:
        set_printer(Printer())
    printer.out(msg)

def print_escaped(color,prefix,msg):
    out(color+prefix+Esc.END+Prefix.SEP+msg)

def print_debug(msg):
    global num_debug
    if db:
        print_escaped(Esc.LIGHT_GRAY,Prefix.DEBUG,msg)
        num_debug = num_debug + 1

def get_num_debug():
    global num_debug
    return num_debug

def print_error(msg):
    global num_error
    if vb:
        print_escaped(Esc.RED,Prefix.ERROR,msg)
        num_error = num_error + 1

def get_num_error():
    global num_error
    return num_error

def print_info(msg):
    global num_info
    if vb:
        print_escaped(Esc.CYAN,Prefix.INFO,msg)
        num_info = num_info + 1

def get_num_info():
    global num_info
    return num_info

def print_success(msg):
    global num_success
    if vb:
        print_escaped(Esc.GREEN,Prefix.SUCCESS,msg)
        num_success = num_success + 1

def get_num_success():
    global num_success
    return num_success

def print_warning(msg):
    global num_warning
    if vb:
        print_escaped(Esc.ORANGE,Prefix.WARNING,msg)
        num_warning= num_warning + 1

def get_num_warning():
    global num_warning
    return num_warning

def main():
    pass

if __name__ == "__main__":
    main()
