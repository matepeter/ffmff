#!/bin/sh

virtualenv venv
. venv/bin/activate

# django ;)
wget http://www.djangoproject.com/download/1.2-rc-1/tarball/
pip install $1 Django-1.2-rc-1.tar.gz
rm Django-1.2-rc-1.tar.gz
pip install $1 south

# search
pip install $1 whoosh
pip install $1 django-haystack

# markdown
# if cElementTree does not compile
# it's possible to use ElementTree but
# the c version is faster of course.
pip install $1 cElementTree
pip install $1 Markdown
