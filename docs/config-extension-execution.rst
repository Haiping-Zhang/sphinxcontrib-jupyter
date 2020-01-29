.. _config_extension_execution:

Executing Notebooks
===================

jupyter_execute_nb  (DEPRECATED)
------------------

Enables the execution of generated notebooks

.. list-table:: 
   :header-rows: 1

   * - Values
   * - False (**default**)
   * - True 

.. todo::

    deprecate this option in favour of jupyter_execute_notebooks

jupyter_execute_notebooks (DEPRECATED)
-------------------------

Enables the execution of generated notebooks

.. list-table:: 
   :header-rows: 1

   * - Values
   * - False (**default**)
   * - True 

``conf.py`` usage:

.. code-block:: python

    jupyter_execute_notebooks = True

jupyter_dependency_lists (MIGRATED -> jupyter_notebook_dependencies)
------------------------

Dependency of notebooks on other notebooks for execution can also 
be added to the configuration file above in the form of a dictionary. 
The key/value pairs will contain the names of the notebook files.

``conf.py`` usage:

.. code-block:: python

   # add your dependency lists here
   jupyter_dependency_lists = {
      'python_advanced_features' : ['python_essentials','python_oop'],
      'discrete_dp' : ['dp_essentials'],
   }


jupyter_dependencies (MIGRATED > jupyter_file_dependencies)
--------------------

Specify support (dependencies) for notebook collection at the `file` or 
the `directory` level.

``conf.py`` usage:

.. code-block:: python

   jupyter_dependencies = {
       <dir> : ['file1', 'file2'],
       {<dir>}/<file.rst> : ['file1']
   }

.. note::

    to specify a support file at the root level of the source directory
    the key should be `""`



