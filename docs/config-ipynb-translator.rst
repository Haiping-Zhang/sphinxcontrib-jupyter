.. _config_ipynb_translator:

IPYNB Notebook Translator
=========================

.. contents:: Options
    :depth: 1
    :local:

Options available when constructing Jupyter notebooks

jupyter_allow_html_only
-----------------------

Enable this option to allow ``.. only:: html`` pass through to the notebooks. 

.. list-table:: 
   :header-rows: 1

   * - Values
   * - False (**default**)
   * - True

``conf.py`` usage:

.. code-block:: python

    jupyter_allow_html_only = True

.. note::

   This is turned on by default in the HTMLTranslator


jupyter_images_html
-------------------

Force the inclusion of images as html objects in the notebook

.. list-table:: 
   :header-rows: 1

   * - Values
   * - False (**default**)
   * - True

.. note::

    this is useful to support the full suite of attributes associated
    with the image directive (i.e. scale).

``conf.py`` usage:

.. code-block:: python

    jupyter_images_html = True