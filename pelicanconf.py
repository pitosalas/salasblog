
AUTHOR = 'Pito Salas'
SITENAME = 'Salas Blog'
SITETITLE = 'Salas Blog'
SITEURL = 'https://pitosalas.github.io/salasblog' 

PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_PAGINATION = 10
LOAD_CONTENT_CACHE = False
USE_FOLDER_AS_CATEGORY = False

# Theme and Static Files
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
THEME = 'theme/notmyidea'
STATIC_PATHS = ['images', 'theme/css', 'theme/js', 'theme/fonts']

# Content Paths
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages/about', 'pages/brandeis', 'pages/curacao']

# Menu Items (shown in top nav bar)
MENUITEMS = [
    ('Home', '/'),
    ('About', '/about/overview.html'),
    ('Brandeis', '/brandeis/overview.html'),
    ('Curacao', '/curacao/curacao.html'),
    ('Archive', '/archives.html'),
    ('Submit Post', 'https://salasblogf.fly.dev/'),
]
# Feed generation (usually disabled during development)
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# Optional metadata
RELATIVE_URLS = True  # Set to False in production (overridden by publishconf.py)