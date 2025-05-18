import os

AUTHOR = 'Pito Salas'
SITENAME = 'Salas Blog'
SITETITLE = 'Salas Blog'
SITEURL = 'https://pitosalas.github.io/salasblog' 

PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_PAGINATION = 10

# Theme and Static Files
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
THEME = 'theme/notmyidea'
STATIC_PATHS = ['images', 'theme/css', 'theme/js', 'theme/fonts']

# Content Paths
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']

# Menu Items (shown in top nav bar)
MENUITEMS = [
    ('Home', '/'),
    ('About', 'about.html'),
    ('Brandeis', 'brandeis.html'),    
    ('Submit Post', 'https://salasblogf.fly.dev/'),
    ("Archive", "/archives.html"),

]

# Feed generation (usually disabled during development)
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_ATOM = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'

# Optional metadata
RELATIVE_URLS = True  # Set to False in production (overridden by publishconf.py)