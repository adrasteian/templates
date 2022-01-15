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

import argparse
import os
import pretty_log as p_l
import sys

#   set_argv()
#
#   Test helper function, allows tests to drive options into
#   main() as if from the command line
#
def set_argv(argv):
    sys.argv = argv

def process_file(path_name,file_name):
    full_name = os.path.join(path_name, file_name)
    if not os.path.isdir(full_name):
        p_l.out("f: <%s>:<%s>"%(path_name, file_name))

def process_dir(path_name,dir_name):
    p_l.out("d: <%s>:<%s>"%(path_name,dir_name))
    path_name = os.path.join(path_name,dir_name)
    dirlist=os.listdir(path_name)
    for file_name in dirlist:
        process_file(path_name,file_name)

def process_tree(tree_name):
    p_l.out("t: tree_name: <%s>"%(tree_name))
    process_dir('', tree_name)
    for path_name, dir_names, filenames in os.walk(tree_name):
        for dir_name in dir_names:
            process_dir(path_name,dir_name)

def main():

    parser = argparse.ArgumentParser(description='Process some folder trees.')

    parser.add_argument('-t', '--trees', nargs='+', help='paths of trees to process', required=True)
    parser.add_argument('-d', '--debug', help='output additional debug logs', action='store_true')
    parser.add_argument('-v', '--verbose', help='verbose output', action='store_true')

    args = parser.parse_args()

    p_l.init()
    p_l.set_db(args.debug)
    p_l.set_vb(args.verbose)

    p_l.out("Hello world!")
    p_l.out(args.trees)

    for tree in args.trees:
        process_tree(tree)

    p_l.print_info("Info!")
    p_l.print_debug("Debug!")
    p_l.print_success("Success!")
    p_l.print_warning("Warning!")
    p_l.print_error("Error!")

if __name__ == "__main__":
    main()
