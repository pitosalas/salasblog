import os
import sys

import pelicanconf
print(pelicanconf.TIMEZONE)

sys.path.insert(0, os.path.dirname(__file__))  # keeps relative imports working

pelicanconf.SITEURL = 'https://pitosalas.github.io/salasblog'
pelicanconf.RELATIVE_URLS = False