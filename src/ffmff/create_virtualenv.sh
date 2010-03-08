#!/bin/sh

virtualenv venv
. venv/bin/activate

# django ;)
pip install $1 django

# search
pip install $1 whoosh
pip install $1 django-haystack

# markdown
# if cElementTree does not compile
# it's possible to use ElementTree but
# the c version is faster of course.
pip install $1 cElementTree
pip install $1 Markdown
