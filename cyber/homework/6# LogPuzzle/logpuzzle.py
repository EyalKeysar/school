#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import urllib.request

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
        txt = open(filename, "r").read()  # Read text from file

    except FileNotFoundError:
        print("File not found")
        sys.exit(1)  # Exit program.

    except Exception as err:
        print("Untracked: " + err)
        sys.exit(1)  # Exit program.

    lines = txt.split("\n")  # Split text into lines.
    files_names = []  # This list will contain all valid files names.
    for line in lines:
        words = line.split(" ")  # Split line into words and arguments.
        try:
            # In http GET request the wanted file location on the
            # server is after the "GET" statement, (ספר גבהים רשתות עמוד 93).
            path = words[words.index("\"GET") + 1]
            # Split path to directories and files (from index 1 to avoid the first "/").
            path_dir_names = path[1:].split("/")

            if(path_dir_names[0] == "python" and path_dir_names[1] == "logpuzzle"):
                files_names.append(path_dir_names[2])  # Add this file name to the list.

        except IndexError:
            print(f"Index error:\nwords = {words}")
        except Exception as err:
            print(f"Untracked: {err}")
    # Change the type of the list to a set and then back to list that so it will delete duplicates.
    files_names = list(set(files_names))
    # Sort list by the abc.
    
    files_names.sort(key=lambda x: x[len(x)-8:])

    return files_names


def download_images(img_urls: list, dest_dir: str) -> None:
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    html_to_write = "<html><body>"
    for file in img_urls:
        url_to_get = r"https://data.cyber.org.il/python/logpuzzle/" + file
        data = urllib.request.urlretrieve(url_to_get, file)
        os.replace(file, dest_dir + file)
        html_to_write += "<img src = \"" + dest_dir + file + "\">"
    html_to_write += "</body></html>"
    html_file = open("output.html", "w").write(html_to_write)

# 10.254.254.65 - - [06/Aug/2007:00:09:21 -0700] "GET /python/logpuzzle/p-bfhh-bahj.jpg HTTP/1.0" 302 528 "-" "googlebot-mscrawl-moma (enterprise; bar-XYZ; foo123@facebook.com)"
def main() -> None:
    img_urls = read_urls(r"./logo_data.cyber.org.il")
    dest_dir = "./images/"
    download_images(img_urls, dest_dir)
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
