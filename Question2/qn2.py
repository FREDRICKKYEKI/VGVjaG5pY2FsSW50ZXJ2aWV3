#!/usr/bin/python2
"""
Question 2:
===========
This html file contains a list of 20 cases with some of their related
metadata. Parse it in beautiful soup and capture, for each case, all the
relevant labeled metadata as well as the categories, title and summary
according to this pictographic guide.
Important:
    a. Download the html file locally to read it, no need to download it in
       code.
    b. Submission for this question is a single python file that prints to the
       terminal an array of 20 dictionaries, each encapsulating metadata from
       an individual case.
"""
import json
import sys
from bs4 import BeautifulSoup


def scrape_cases(filename):
    """Extract cases from the given html page
    filename: `str` name/path of file to be parsed
    """
    return_list = []

    with open(filename, "r") as f:
        html_file = f.read()

    # general clean up
    html_file = html_file.replace(" =20 ", "").replace("=20 =20", "")
    html_file = html_file.replace("<=", "<").replace("=20", "")

    # soupify
    soup = BeautifulSoup(html_file, "html.parser")

    for el in soup.find_all(class_='3D"group"'):
        try:
            case_dict = {"categories": None,
                         "title": None,
                         "summary": None,
                         "meta": None
                         }
            # categories
            proceedings = el.find(attrs={
                "field--name-field-legal-library-record-types": True})
            cats = [a.text.replace("\r\n", "") for a in proceedings
                    .find_all("a")]
            cats = [a.strip("</a>") for a in cats]
            case_dict["categories"] = [a.encode("ascii", "ignore")
                                       for a in cats]

            # title
            title = el.find(class_='3D"node-title"').text
            case_dict["title"] = title.encode("ascii", "ignore")\
                .replace("\r\n", "")

            # summary
            summary = el.find(attrs={"field--type-text-with-summary": True})
            if summary:
                summary = summary.text
                summary = summary.replace("\r\n", "").replace("=", "")\
                    .replace("\n\n", "")
                case_dict["summary"] = summary.encode("ascii", "ignore")\
                    .strip("\n")
            else:
                case_dict["summary"] = ""
            # metas
            fields = el.find_all(class_='3D"field')
            metas = fields[2:]
            metas = {meta.find(class_='3D"field__label"').text:
                     meta.find(class_='3D"field__item"').text
                     for meta in metas
                     }
            metas = {key.encode("ascii", "ignore").strip():
                     val.encode("ascii", "ignore").strip()
                     for key, val in metas.items()
                     }
            case_dict["meta"] = metas

            return_list.append(case_dict)
        except Exception as e:
            return_list.append(case_dict)
            continue

    return return_list


if __name__ == "__main__":
    if len(sys.argv[1:]):
        filename = sys.argv[1]
        print(json.dumps(scrape_cases(filename)).replace("=\r\n", ""))
    else:
        print("usage: {} [filename]".format(sys.argv[0]))
        print("- This script parses 'ftc.mhtml' file into a dict")
