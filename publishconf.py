import os
import sys
sys.path.insert(0, os.path.dirname(__file__))  # keeps relative imports working

import pelicanconf

THEME = os.path.abspath(os.path.join(os.path.dirname(__file__), 'theme', 'notmyidea'))
SITEURL = 'https://pitosalas.github.io/salasblog'
RELATIVE_URLS = False