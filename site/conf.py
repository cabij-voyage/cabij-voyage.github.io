# outline for a myst_nb project with sphinx
# build with: sphinx-build -nW --keep-going -b html . ./_build/html

# load extensions
extensions = [
    "myst_nb",
    "ablog",
    "sphinx.ext.intersphinx",
    ]

# specify project details
master_doc = "index"
project = "Cabij Voyage"

# basic build settings
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]
nitpicky = True

# HTML theme (pydata sphinx theme)
html_theme = "pydata_sphinx_theme"
html_title = "Cabij Voyage"

# -- ABlog ---------------------------------------------------

blog_title = "Cabij Voyage"
blog_path = "blog"
blog_post_pattern = "blog/*/*"
blog_feed_fulltext = True
blog_feed_subtitle = "The adventures of the good 'ship' Cabij."
fontawesome_included = True
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

html_sidebars = {
   '**': [
    'ablog/recentposts.html',
    'ablog/tagcloud.html', 
    'ablog/archives.html', 
    ]
}