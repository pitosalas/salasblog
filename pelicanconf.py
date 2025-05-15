import os

AUTHOR = 'Pito Salas'
SITENAME = 'Salas Blog'
SITETITLE = 'Salas Blog'
SITEURL = 'https://pitosalas.github.io/salasblog'

PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['images', 'theme/css', 'theme/js', 'theme/fonts']

THEME = 'notmyidea'
DEFAULT_PAGINATION = 5

# Enable page generation
PAGE_PATHS = ['pages']

# Add menu items manually
MENUITEMS = [
    ('Home', '/'),
    ('Curacao', '/curacao.html'),
    ('Links', '/links.html'),
    ('About', '/about.html'),
    ('Brandeis', '/brandeis.html'),
]