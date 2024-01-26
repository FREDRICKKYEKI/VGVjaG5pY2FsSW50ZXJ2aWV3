#!/usr/bin/python2
"""
This module contains the `.pdf` parser function and its utility functions
"""
import sys
from pypdf import PdfReader
from .txt_parser import txt_to_dict


def parse_pdf(filename):
    """
    Parses pdf files to a uni-level dict object
    """
    with open(filename, "rb") as f:
        reader = PdfReader(f)
        text = ""
        for page_num in range(reader._get_num_pages()):
            page = reader.pages[page_num]
            text += page.extract_text(extraction_mode="layout",
                                      layout_mode_space_vertically=False)

        return txt_to_dict(text.replace("\r", ""))


if __name__ == "__main__":
    if len(sys.argv[1:]):
        filename = sys.argv[1]
        print(parse_pdf(filename))
    else:
        print("usage: {} [filename]".format(sys.argv[0]))
        print("- This script parses 'pdf' files into a uni-level json dict")
