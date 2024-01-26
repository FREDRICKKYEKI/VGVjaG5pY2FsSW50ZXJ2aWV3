#!/usr/bin/python2
"""
This module contains the `.txt` parser functions and its utility functions
"""
import re
import copy
from datetime import datetime
import sys
from .utils import reg_dict, flatten_dict


def txt_to_dict(text):
    """
    Uses regex matching to parse text to a `dict` obj

    `text`: `str` - text to be parsed
    """

    # text should have content
    if not text or not len(text) > 0:
        raise ValueError("`text` argument cannot be empty for" +
                         "`def txt_to_dict(text)`")

    return_dict = copy.deepcopy(reg_dict)

    for key, val in reg_dict.items():
        # match patterns using regex
        if not isinstance(val, dict):
            return_dict[key] = re.search(val, text).group(1).strip()\
                if re.search(val, text) else ""

        else:
            for sub_key, sub_val in val.items():
                return_dict[key][sub_key] = re.search(sub_val, text)\
                    .group(1).strip() if re.search(sub_val, text) else ""

        # "dob" -> datetime()
        if key == "date_of_birth":
            return_dict[key] = ", ".join(return_dict[key].split(","))
            return_dict[key] = datetime.strptime(return_dict[key], "%B %d, %Y")
        # "age" -> int()
        elif key == "age":
            return_dict[key] = int(return_dict[key])
        # listify
        elif key in ["hobbies", "hobbies", "favorite_music", "favorite_movies",
                     "languages_spoken"]:
            return_dict[key] = [w.strip() for w in return_dict[key].split(",")]

    return flatten_dict(return_dict)


def parse_txt(filename):
    """Parses `.txt` files to a uni-level dict object
    filename: name/path of .txt file to be parsed
    """
    with open(filename, "r") as f:
        text = f.read()

    return txt_to_dict(text.replace("\r", ""))


if __name__ == "__main__":
    if len(sys.argv[1:]):
        filename = sys.argv[1]
        print(parse_txt(filename))
    else:
        print("usage: {} [filename]".format(sys.argv[0]))
        print("- This script parses '.txt' files into a uni-level json dict")
