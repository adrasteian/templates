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

def process_file(path_name,file_name):
    full_name = os.path.join(path_name, file_name)
    if not os.path.isdir(full_name):
        print("f: <%s>:<%s>"%(path_name, file_name))

def process_dir(path_name,dir_name):
    print("d: <%s>:<%s>"%(path_name,dir_name))
    path_name = os.path.join(path_name,dir_name)
    dirlist=os.listdir(path_name)
    for file_name in dirlist:
        process_file(path_name,file_name)

def process_tree(tree_name):
    print("t: tree_name: <%s>"%(tree_name))
    process_dir('', tree_name)
    for path_name, dir_names, filenames in os.walk(tree_name):
        for dir_name in dir_names:
            process_dir(path_name,dir_name)

def main():

    parser = argparse.ArgumentParser(description='Process some folder trees.')

    parser.add_argument('-t', '--trees', nargs='+', help='paths of trees to process', required=True)

    args = parser.parse_args()

    for tree in args.trees:
        process_tree(tree)

    print("Hello world!")

if __name__ == "__main__":

    main()
