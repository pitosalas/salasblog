import os

AUTHOR = 'Pito Salas'
SITENAME = 'Salas Blog'
SITETITLE = 'Salas Blog'
SITEURL = 'https://pitosalas.github.io/salasblog'  # Update to '' for local dev

PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_PAGINATION = 5

# Theme and Static Files
THEME = 'notmyidea'
STATIC_PATHS = ['images', 'theme/css', 'theme/js', 'theme/fonts']

# Content Paths
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages', 'curacao', 'links', 'about', 'brandeis']

# Menu Items (shown in top nav bar)
MENUITEMS = [
    ('Home', '/'),
    ('Curacao', '/curacao.html'),
    ('Brandeis', '/brandeis.html'),
    ('Submit Post', 'https://salasblogf.fly.dev/')  # 👈 Link to your FastAPI form
]

# Feed generation (usually disabled during development)
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_ATOM = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'

# Optional metadata
RELATIVE_URLS = True  # Set to False in production (overridden by publishconf.py)