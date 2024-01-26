#!/usr/bin/python2
"""
This module contains the `.json` parser functions and its utility functions
"""
import sys
import json
from datetime import datetime


def encoder(data):
    """Recursively encodes the data to a 'ascii' (removes the 'u' prefix)
    data: `dict` the parsed json
    """
    if isinstance(data, unicode):
        return data.encode('utf-8')
    elif isinstance(data, list):
        return [encoder(item) for item in data]
    elif isinstance(data, dict):
        return {encoder(key): encoder(value)
                for key, value in data.iteritems()}
    else:
        return data


def parse_json(filename):
    """
    Parses `.json` files to a uni-level dict

    filename: `str` name/path of file to be parsed
    """
    with open(filename, "r") as f:
        json_file = json.load(f)

    return_dict = encoder(json_file)["user"]

    # dob -> datetime()
    return_dict["date_of_birth"] =\
        datetime.strptime(return_dict["date_of_birth"], "%Y-%m-%d")
    # age -> int()
    return_dict["age"] = int(return_dict["age"])

    print(return_dict)


if __name__ == "__main__":
    if len(sys.argv[1:]):
        filename = sys.argv[1]
        print(parse_json(filename))
    else:
        print("usage: {} [filename]".format(sys.argv[0]))
        print("- This script parses '.json' files into a uni-level json dict")
