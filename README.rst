First of all, we use reStructuredText Markup instead of Markdown. Just because.


Directory Structure 
===================
The project's directory structure is recommended in `The Hitchhikers Guide to Python <http://docs.python-guide.org/en/latest/writing/structure/>`_.


.gitignore
==========
The ``.gitignore`` is populated from `gitignore.io <https://www.gitignore.io/>`_.


.editorconfig
=============
Use ``.editorconfig`` to define portable editor configuration. See also `editorconfig.org <http://editorconfig.org/>`_.


main() function
===============
Guido van Rossum proposes a ``main()`` function in the `blog post <http://www.artima.com/forums/flat.jsp?forum=106&thread=4829>`_. ``cli.py`` is modelled after GvR's idea, although the file is split into multiple files.


Source code encoding
====================
How the source code encoding has to be configured is recommended in `PEP 263 <https://www.python.org/dev/peps/pep-0263/>`_.


Docstring
=========
Use Google style docstrings.
http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html


Paver
=====
`Paver <https://github.com/paver/paver>`_ is a taskrunner like Make and Rake. 


TOX - Test automation
=====================
Automation and standardisation of tests are run by `Tox <https://testrun.org/tox/latest/>`_. that is configured in ``tox.ini``.


