# Variables defined in this file will be passed to the 'config' attribute of the
# Flask instance used by the Dash app. They must be in UPPER CASE in order to
# take effect. For more information see http://flask.pocoo.org/docs/config.

# 
# Config for the Dash instance 
#

# Your App's title. The value of this parameter will be propagated into
# `app.title`
TITLE = 'Slapdash'

# The value of this parameter will be propagated into both
# `app.scripts.config.serve_locally` and `app.css.config.serve_locally`
SERVE_LOCALLY = True

# Prefix for Dash URL routes. Passed into Dash's `routes_pathname_prefix`
# keyword argument.
ROUTES_PATHNAME_PREFIX = '/'

# Custom CSS files go in here. Passed into Dash's `external_stylesheets`
# keyword argument.  If you want to use Bootstrap from a CDN, Dash Bootstrap
# Components contains links to bootstrapcdn:
#
# import dash_bootstrap_components as dbc
# EXTERNAL_STYLESHEETS = [dbc.themes.BOOTSTRAP]
# 
# or if you want to use a Bootswatch theme: 
# import dash_bootstrap_components as dbc
# EXTERNAL_STYLESHEETS = [dbc.themes.CYBORG]
EXTERNAL_STYLESHEETS = []

# Custom CSS files go in here. Passed into Dash's `external_scripts` keyword
# argument
EXTERNAL_SCRIPTS = []


#
# Layout config
#

# The ID of the element used to inject each page of the multi-page app into
CONTENT_CONTAINER_ID = 'dash-container'

NAVBAR_CONTAINER_ID = 'header'

# Ordered iterable of navbar items: tuples of (route, name), where 'route' is a
# string corresponding to path of the route (will be prefixed with
# URL_BASE_PATHNAME) and 'name' is a string corresponding to the name of the nav
# item.
NAV_ITEMS = (
    ('page1', 'Page 1'),
    ('page2', 'Page 2'),
    ('page3', 'Page 3'),
)

