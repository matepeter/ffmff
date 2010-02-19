#!/bin/sh

virtualenv venv
. venv/bin/activate
easy_install django
easy_install whoosh
easy_install django-haystack
