#!/usr/bin/python2
"""
This module contains the docx functions and its utility functions
"""
import sys
from docx import Document
from txt_parser import txt_to_dict


def parse_docx(filename):
    """
    Parses `.docx` files to a uni-level dict object
    filename: the name/path of the .docx file to be parsed
    """
    doc = Document(filename)

    text = ("".join([p.text.encode("ascii", "ignore") + "\n"
                     for p in doc.paragraphs]))
    return txt_to_dict(text)


if __name__ == "__main__":
    if len(sys.argv[1:]):
        filename = sys.argv[1]
        print(parse_docx(filename))
    else:
        print("usage: {} [filename]".format(sys.argv[0]))
        print("- This script parses 'docx' files into a uni-level json dict")
