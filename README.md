# QXBwcyBvbiBQb2ludCBMVEQ=

## Question 1

You have been provided with information about a certain imaginary party, John Doe, contained
within several different file types and data/presentation formats.
For EACH of the following file types, you are to create one python 2.7 script that reads in the
corresponding data file and returns all the metadata as a single level python dictionary (no
nested dictionaries)
**Important**:

1. Parse the dates into a datetime object
2. Age should be an integer
3. Use pypdf to read the PDF file, beautiful soup to parse HTML & any package of choice
   for the word document.
4. Submission for this question should be 4 (or 5 python scripts if you tackle bonus
   question) that on execution will ingest the relevant input file, and prints the user
   metadata as a python dictionary.
5. Download the zip folder and decompress it to access the individual files inside it.

### Answer

```bash
git clone https://github.com/FREDRICKKYEKI/VGVjaG5pY2FsSW50ZXJ2aWV3.git
cd VGVjaG5pY2FsSW50ZXJ2aWV3
```

---

- a. JSON (john.json)

output:

```bash
fredrick_ubuntu@FRED:/mnt/c/Users/FRED/Technical Interview$ python2 -m Question1.json_parser Question1/john/john.json
{'place_of_work': 'Creative Design Studio Inc.', 'pet_type': 'Dog', 'hobbies': ['Photography', 'Hiking', 'Reading'], 'social_media_Twitter': '@johnD_tweets', 'education': "Bachelor's in Fine Arts", 'occupation': 'Graphic Designer', 'location_city': 'San Francisco', 'location_country': 'United States', 'favorite_movies': ['Inception', 'The Grand Budapest Hotel'], 'social_media_Facebook': 'john.doe34', 'date_of_birth': datetime.datetime(1989, 7, 15, 0, 0), 'favorite_music': ['Jazz', 'Classical'], 'pet_breed': 'Golden Retriever', 'languages_spoken': ['English', 'Spanish'], 'location_state': 'California', 'pet_name': 'Buddy', 'name': 'John Doe', 'gender': 'Male', 'age': 34, 'location_zip_code': '94103', 'social_media_Instagram': 'john_the_designer'}
```

---

- b. Plain Text (john.txt)

output:

```bash
fredrick_ubuntu@FRED:/mnt/c/Users/FRED/Technical Interview$ python2 -m Question1.txt_parser Question1/john/john.txt
{'place_of_work': 'Creative Design Studio Inc.', 'pet_type': 'Dog', 'hobbies': ['Photography', 'Hiking', 'Reading'], 'social_media_Twitter': '@johnD_tweets', 'education': "Bachelor's in Fine Arts", 'occupation': 'Graphic Designer', 'location_city': 'San Francisco', 'location_country': 'United States', 'favorite_movies': ['Inception', 'The Grand Budapest Hotel'], 'social_media_Facebook': 'john.doe34', 'date_of_birth': datetime.datetime(1989, 7, 15, 0, 0), 'favorite_music': ['Jazz', 'Classical'], 'pet_breed': 'Golden Retriever', 'languages_spoken': ['English', 'Spanish'], 'location_state': 'California', 'pet_name': 'Buddy', 'name': 'John Doe', 'gender': 'Male', 'age': 34, 'location_zip_code': '94103', 'social_media_Instagram': 'john_the_designer'}
```

---

- c. HTML (john.html)

output:

```bash
fredrick_ubuntu@FRED:/mnt/c/Users/FRED/Technical Interview$ python2 -m Question1.html_parser Question1/john/john.html
{'place_of_work': 'Creative Design Studio Inc.', 'pet_type': 'Dog', 'hobbies': ['Photography', 'Hiking', 'Reading'], 'social_media_Twitter': '@johnD_tweets', 'education': "Bachelor's in Fine Arts", 'occupation': 'Graphic Designer', 'location_city': 'San Francisco', 'location_country': 'United States', 'favorite_movies': ['Inception', 'The Grand Budapest Hotel'], 'social_media_Facebook': 'john.doe34', 'date_of_birth': datetime.datetime(1989, 7, 15, 0, 0), 'favorite_music': ['Jazz', 'Classical'], 'pet_breed': 'Golden Retriever', 'languages_spoken': ['English', 'Spanish'], 'location_state': 'California', 'pet_name': 'Buddy', 'name': 'John Doe', 'gender': 'Male', 'age': 34, 'location_zip_code': '94103', 'social_media_Instagram': 'john_the_designer'}
```

---

- d. PDF (john.pdf)\*\*

\***\*Note\*\***

- The `pdf_parser` is not compatible with `python 2.7.x` so it does not extract anything (it will raise an exception on runtime), but it runs on `python3`. Please refer to the link below.
  > **pypdf requires Python 3.7+ to run.** [https://pypdf.readthedocs.io/en/stable/user/installation.html#pip](https://pypdf.readthedocs.io/en/stable/user/installation.html#pip)
- The `pypdf` alternative which is compatible to python `python 2.7.x` is `pyPDF2` whose `extract_text()` function is not stable yet. Please refer to the link below.

  [https://realpython.com/pdf-python/#how-to-extract-document-information-from-a-pdf-in-python](https://realpython.com/pdf-python/#how-to-extract-document-information-from-a-pdf-in-python)

  > While PyPDF2 has .extractText(), which can be used on its page objects (not shown in this example), it does not work very well. Some PDFs will return text and some will return an empty string. When you want to extract text from a PDF, you should check out the PDFMiner project instead. PDFMiner is much more robust and was specifically designed for extracting text from PDFs.

output:

```bash
fredrick_ubuntu@FRED:/mnt/c/Users/FRED/Technical Interview$ python3 -m Question1.pdf_parser Question1/john/john.pdf
{'name': 'John Doe', 'date_of_birth': datetime.datetime(1989, 7, 15, 0, 0), 'age': 34, 'gender': 'Male', 'occupation': 'Graphic  Designer', 'place_of_work': 'CreativeDesign  Studio Inc.', 'education': "Bachelor'sin Fine Arts", 'hobbies': ['Photography', 'Hiking', 'Reading'], 'favorite_music': ['Jazz', 'Classical'], 'favorite_movies': ['Inception', 'The Grand   Budapest  Hotel'], 'languages_spoken': ['English', 'Spanish'], 'location_country': 'United States', 'location_state': 'California', 'location_city': 'San Francisco', 'location_zip_code': '', 'pet_type': 'Dog', 'pet_name': 'Buddy', 'pet_breed': 'Golden  Retriever', 'social_media_Facebook': 'john.doe34', 'social_media_Instagram': 'john_the_designer', 'social_media_Twitter': '@johnD_tweets'}
```

---

- e. DOCX (john.docx) - BONUS, not mandatory to attempt

output

```bash
fredrick_ubuntu@FRED:/mnt/c/Users/FRED/Technical Interview$ python2 -m Question1.docx_parser_ Question1/john/john.docx
{'place_of_work': 'Creative Design Studio Inc.', 'pet_type': 'Dog', 'hobbies': ['Photography', 'Hiking', 'Reading'], 'social_media_Twitter': '@johnD_tweets', 'education': "Bachelor's in Fine Arts", 'occupation': 'Graphic Designer', 'location_city': 'San Francisco', 'location_country': 'United States', 'favorite_movies': ['Inception', 'The Grand Budapest Hotel'], 'social_media_Facebook': 'john.doe34', 'date_of_birth': datetime.datetime(1989, 7, 15, 0, 0), 'favorite_music': ['Jazz', 'Classical'], 'pet_breed': 'Golden Retriever', 'languages_spoken': ['English', 'Spanish'], 'location_state': 'California', 'pet_name': 'Buddy', 'name': 'John Doe', 'gender': 'Male', 'age': 34, 'location_zip_code': '94103', 'social_media_Instagram': 'john_the_designer'}
```

---

## Question 2

This html file contains a list of 20 cases with some of their related metadata. Parse it in
beautiful soup and capture, for each case, all the relevant labeled metadata as well as
the categories, title and summary according to this pictographic guide.
Important:
a. Download the html file locally to read it, no need to download it in code.
b. Submission for this question is a single python file that prints to the terminal an
array of 20 dictionaries, each encapsulating metadata from an individual case.

### Answer

> ```bash
>    python2 -m Question2.qn2 Question2/ftc.mhtml
> ```

---

output: in this [file](./Question2/output.json).
