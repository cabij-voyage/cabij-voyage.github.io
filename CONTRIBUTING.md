# Contributing
A.k.a. how to edit the website.

Before you begin, you will need Python3 and git installed. You may also want to [setup SSH authentication for your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

## Clone the repository
`git clone `

## Environment and installations (`venv` and `pip`)
Make sure that you have navigated to the root directory, e.g.:
`cd cabij-voyage`

To create a new virtual environment using venv, run:
`python -m venv venv/`

To "activate" the environment, run:
`source venv/bin/activate`

Now you can install the website requirements:
`pip install -r requirements.txt`

## The website: Sphinx, MyST markdown, and Ablog
### Overview
The website uses [Sphinx](https://www.sphinx-doc.org/en/master/) with [MyST Markdown](https://jupyterbook.org/en/stable/content/myst.html) to generate the static site. 
Sphinx is a Python package, used mostly to create documentation for Python packages. 
Sphinx can be extended with additional Python packages, for example we use the [`ablog`](https://ablog.readthedocs.io/en/stable/) sphinx extension to handle the blog and the [`pydata-sphinx-theme`](https://pydata-sphinx-theme.readthedocs.io/en/stable/) sphinx extension to make the website prettier/more customisable.
The website's configuration settings for sphinx and it's extensions are all stored in the `site/conf.py` file - you're unlikely to need to edit these unless you are changing the overall look of the website.

### Blog
Blogposts are markdown `.md` files, stored in the `site/blog` directory (sub-organised by year). 
Markdown is a markup language that allows plain text to be easily converted to nicely formatted HTML, for display on websites. 
Markdown comes in different "flavours", each offering different options for formatting. 
This website uses [MyST Markdown](https://jupyterbook.org/en/stable/content/myst.html); it's a superset of the Markdown used on GitHub, which you may be more familiar with ([CommonMark](https://commonmark.org/)), so it allows a wider variety of options. 
This [MyST Markdown cheatsheet](https://jupyterbook.org/en/stable/reference/cheatsheet.html) may come in handy if you want to look up how to display something specific, e.g. a dropdown box, table, image, etc.

Each blog post has a [YAML](https://yaml.org/) header that contains the `ablog` blog metadata (not amazingly documented, see [here](https://ablog.readthedocs.io/en/stable/manual/markdown.html) and [here](https://ablog.readthedocs.io/en/stable/manual/posting-and-listing.html#directive-post)), for example the blog entry's author, tags, title, and date.

Summaries of recent blogposts are displayed on the front page of the website using ablog's [postlist](https://ablog.readthedocs.io/en/stable/manual/posting-and-listing.html#listing) directive.

### Creating a new blogpost
To create a new blogpost, create a new markdown file in the current year's directory within `site/blog`, and give it a descriptive file name e.g.:
`touch site/blog/2023/boatweek-day1.md`

Copy and paste in the following metadata and edit it:
```
---
tags: repair, lore, sailig
date: "YYYY-MM-DD"
---
```

### Building the website locally
`sphinx-build site site/_build`

## Git workflow

