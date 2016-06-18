#!/usr/bin/python
import sys
import logging
import site

site.addsitedir('/home/neha/pyenvs/flaskdemo/lib/python3.5/site-packages')

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/neha/flaskdemo/")

#activate_this = '/home/neha/pyenvs/flaskdemo/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))

from main import app as application

