#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

from hashlib import new
from logging import exception
import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename: str) -> list:
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    try:
        open(filename)
        txt = open(filename, "r").read()
    except:
        print("file not found")
        sys.exit(1)
    lines = txt.split("\n")
    files_name = []
    for line in lines:
        words = line.split(" ")
        try:
            path = words[words.index("\"GET") + 1]
            path_dir_names = path[1:].split("/")
            if(path_dir_names[0] == "python" and path_dir_names[1] == "logpuzzle"):
                files_name.append(path_dir_names[2])
        except Exception as e:
            print(f"err: {e} \n {words}")
    files_name = list(set(files_name))
    files_name.sort(key=str.lower)
    return files_name


def download_images(img_urls: list, dest_dir: str):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """

# 10.254.254.65 - - [06/Aug/2007:00:09:21 -0700] "GET /python/logpuzzle/p-bfhh-bahj.jpg HTTP/1.0" 302 528 "-" "googlebot-mscrawl-moma (enterprise; bar-XYZ; foo123@facebook.com)"
def main() -> None:
    print(read_urls(r"./logo_data.cyber.org.il"))
    sys.exit(0)
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[:2]
    img_urls = read_urls(args[0])
    
    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))

if __name__ == '__main__':
    main()
