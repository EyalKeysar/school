"""
Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.
"""

#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

from ctypes import WinError
import os
import sys
import urllib
import urllib.request

def read_urls(filename: str) -> list:
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    if("message" in filename):
        print("The program will download the Message")
    elif("logo" in filename):
        print("The program will download the Logo")
    else:
        print("The program will download Unknown")

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
            sys.exit(1)
        except Exception as err:
            print(f"Untracked: {err}\nin read_urls function")
            sys.exit(1)
    # Change the type of the list to a set and then back to list that so it will delete duplicates.
    files_names = list(set(files_names))
    # Sort list by the abc.

    files_names.sort(key=lambda x: x[len(x)-8:])

    return files_names


def download_images(img_urls: list, dest_dir: str) -> None:
    """
    Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    html_to_write = "<html><body>"  # Start of an html file.
    sum_of_images = 0
    download_images_not_finished = True
    dir_created = False
    while download_images_not_finished:
        try:
            for file in img_urls:
                url_to_get = r"https://data.cyber.org.il/python/logpuzzle/" + file
                data = urllib.request.urlretrieve(url_to_get, file)  # Get image from current url.

                # The image will be imported to the program directory
                # so it need to be replaced to dest_dir.
                os.replace(file, dest_dir + file)
                dir_created = True

                # Add img src to the html page.
                html_to_write += "<img src = \"" + dest_dir + file + "\">"
                sum_of_images += 1
                print(f"Image number: {sum_of_images} has been successfully downloaded.")
            download_images_not_finished = False
        except WindowsError as err:
            if(dir_created):
                print("Program can not handle " + err)
                sys.exit(1)
            print("Creating " + dest_dir)
            os.mkdir(dest_dir)
            dir_created = True
    html_to_write += "</body></html>"  # End of an html file.
    open("output.html", "w").write(html_to_write)  # Write to the html file.

def main() -> None:
    """
    This is the main function.
    """
    img_urls = read_urls(r"./message_data.cyber.org.il")
    dest_dir = "./images/"
    download_images(img_urls, dest_dir)
    sys.exit(0)

if __name__ == '__main__':
    main()
