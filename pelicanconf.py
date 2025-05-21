import os

THEME = os.path.abspath(os.path.join(os.path.dirname(__file__), 'theme', 'notmyidea'))
AUTHOR = 'Pito Salas'
SITENAME = 'Salas Blog'
SITETITLE = 'Salas Blog'
SITEURL = '' 

PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_PAGINATION = 10
LOAD_CONTENT_CACHE = False
USE_FOLDER_AS_CATEGORY = False
RELATIVE_URLS = True

# Theme and Static Files
STATIC_PATHS = ['images', 'theme/css', 'theme/js', 'theme/fonts']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives', 'archivers']

# Content Paths
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages/about', 'pages/brandeis', 'pages/curacao','pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Menu Items (shown in top nav bar)
MENUITEMS = [
    ('Home', '/'),
    ('Submit Post', 'https://salasblogf.fly.dev/'),
    ('Brandeis', 'brandeis.html'),
    ('About','about.html'),
    ('Curacao','curacao.html'),
    ('Posts by year', 'archives/index.html'),
    ('All Posts', 'archives.html'),

]
