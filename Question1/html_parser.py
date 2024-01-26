#!/usr/bin/python2
"""
This module contains the `.html` parser functions and its utility functions
"""
import sys
from bs4 import BeautifulSoup
from txt_parser import txt_to_dict


def parse_html(filename):
    """
    Parses `html` files using bs4's Beautiful soup to a uni-level dict

    filename: `str` name/path of file to be parsed
    """
    text = ""

    with open(filename, "r") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, "html.parser")

    for p in soup.find_all(class_="section"):
        text += p.text.encode("ascii", "ingnore")

    return txt_to_dict(text.replace("\r", ""))


if __name__ == "__main__":
    if len(sys.argv[1:]):
        filename = sys.argv[1]
        print(parse_html(filename))
    else:
        print("usage: {} [filename]".format(sys.argv[0]))
        print("- This script parses '.html' files into a uni-level json dict")
