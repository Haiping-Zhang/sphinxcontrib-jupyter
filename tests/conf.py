#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# sphinxcontrib-jupyter.minimal documentation build configuration file, created by
# sphinx-quickstart on Tue Jan 30 14:46:58 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxcontrib.jupyter', 'sphinx.ext.mathjax']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'sphinxcontrib-jupyter.testcases'
copyright = '2018, QuantEcon Development Team'
author = 'QuantEcon Development Team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = '0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'rst2ipynb']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'sphinxcontrib-jupytertestcasedoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'sphinxcontrib-jupytertestcases.tex', 'sphinxcontrib-jupyter.testcases Documentation',
     'QuantEcon Development Team', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'sphinxcontrib-jupytertestcases', 'sphinxcontrib-jupyter.testcases Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'sphinxcontrib-jupytertestcases', 'sphinxcontrib-jupyter.testcases Documentation',
     author, 'sphinxcontrib-jupytertestcases', 'One line description of project.',
     'Miscellaneous'),
]

# --------------------------------------------
# sphinxcontrib-jupyter Configuration Settings
# --------------------------------------------

# Conversion Mode Settings
# If "all", convert codes and texts into jupyter notebook
# If "code", convert code-blocks only
jupyter_conversion_mode = "all"

jupyter_write_metadata = False

# Location for _static folder
jupyter_static_file_path = ["_static"]

#allow execution of notebooks
jupyter_execute_notebooks = False

#make website
jupyter_make_site = False

#path to download notebooks from 
jupyter_download_nb_urlpath = "https://lectures.quantecon.org"

#allow downloading of notebooks
jupyter_download_nb = False

# Location of template folder for coverage reports
jupyter_template_coverage_file_path = "theme/templates/error_report_template.html"

# generate html from IPYNB files
jupyter_generate_html = False

jupyter_html_template = "theme/templates/lectures-nbconvert.tpl"

jupyter_dependency_lists = {
    'code_blocks' : ['code_synonyms','ignore'],
    'exercises' : ['footnotes'],
}

# Configure Jupyter Kernels
jupyter_kernels = {
    "python3": {
        "kernelspec": {
            "display_name": "Python",
            "language": "python3",
            "name": "python3"
        },
        "file_extension": ".py",
    },
    "julia": {
        "kernelspec": {
            "display_name": "Julia 0.6.0",
            "language": "julia",
            "name": "julia-0.6"
        },
        "file_extension": ".jl"
    }
}

# Default language for Jupyter notebooks
jupyter_default_lang = "python3"

# Prepend a Welcome Message to Each Notebook
jupyter_welcome_block = "welcome.rst"

# Solutions Configuration
jupyter_drop_solutions = True

# Tests configurations 
jupyter_drop_tests = True

# Add Ipython as Synonym for tests
jupyter_lang_synonyms = ["ipython"]

# Image Prefix (enable web storage references)
# jupyter_images_urlpath = "https://github.com/QuantEcon/sphinxcontrib-jupyter/raw/master/tests/_static/"


