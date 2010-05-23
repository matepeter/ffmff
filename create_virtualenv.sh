#!/bin/sh

rm -r venv
virtualenv venv
. venv/bin/activate

# django ;)
pip install $1 django
pip install $1 south

# search
pip install $1 whoosh
pip install $1 django-haystack

# markdown
# if cElementTree does not compile
# it's possible to use ElementTree but
# the c version is faster of course.
pip install $1 cElementTree
if [ $? -gt 0 ]; then
	pip install $1 ElementTree
	echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	echo "Installed ElementTree instead of cElementTree because"
	echo "of errors during installation of cElementTree."
	echo "This may cause a slight slowdown."
	echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
fi
pip install $1 Markdown
