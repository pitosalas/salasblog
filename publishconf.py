import sys
import os
sys.path.insert(0, os.path.dirname(__file__))  # ← this makes relative imports work

import pelicanconf
SITEURL = 'https://pitosalas.github.io/salasblog'
RELATIVE_URLS = False