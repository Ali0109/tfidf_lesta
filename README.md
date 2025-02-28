# TFIDF Test Project Lesta Games

A Django web application TFIDF Analyzer that allows users to upload a text file and computes TF (Term Frequency) and
IDF (Inverse Document Frequency) for words in the text. The application then displays a table with the top 50 words
sorted by IDF.

## Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Conclusion](#conclusion)

## Getting Started

First clone the repository from Github and switch to the new directory:

```bash
    git clone https://github.com/Ali0109/tfidf_lesta
    cd tfidf_lesta
```

Create and activate the virtualenv, install dependencies, apply migrations and run server on Linux.

```bash
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 manage.py migrate
    python3 manage.py runserver
```

Create and activate the virtualenv, install dependencies, apply migrations and run server on Windows.

```bash
    python -m venv venv
    venv/Scripts/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
```

## Project Structure

A simple-organized project structure.

## Conclusion
This project was developed as a test for the Python Developer position at Lesta Games.

[Task link.](https://gist.github.com/nonamenix/651852a8943e6a84abdf03ed82dc7518)
