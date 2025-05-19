
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
    ('Submit Post', 'https://salasblogf.fly.dev/'),
    ('New Archive', 'archives.html'),    
    ('Archive', '/archives.html'),
    ('Archive', 'archives.html'),
    ('Brandeis', 'brandeis.html'),
    ('About1','about.html'),
    ('About2','/about.html'),
    ('About3','pages/about.html'),
    ('About4','/pages/about.html'),
    ('Brandeis1','brandeis.html'),
    ('Brandeis2','/brandeis.html'),
    ('Brandeis3','pages/brandeis.html'),
    ('Brandeis4','/pages/brandeis.html'),
    ('Curacao1','curacao.html'),
    ('Curacao2','/curacao.html'),
    ('Curacao3','pages/curacao.html'),
    ('Curacao4','/pages/curacao.html')
]
