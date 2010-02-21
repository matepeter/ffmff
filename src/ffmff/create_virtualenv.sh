#!/bin/sh

virtualenv venv
. venv/bin/activate

# django ;)
easy_install django

# search
easy_install whoosh
easy_install django-haystack

# markdown
# if cElementTree does not compile
# it's possible to use ElementTree but
# the c version is faster of course.
easy_install cElementTree
easy_install Markdown
