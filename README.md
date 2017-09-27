# SETUP
To set up this project I ran:
  - `mkdir docs`
  - `cd docs`
  - `sphinx-quickstart`
  
When it asks to separate the source and build directories, I type `y` and press `enter`. When it asks for the autodoc 
extension, I type `y` and `press enter`.

Then I open the docs/source/conf.py file to change the configuration. I uncommented the following lines and replaced 
them with this to add `mymodule` to the `PYTHONPATH`:

  - `import os`
  - `import sys`
  - `sys.path.insert(0, os.path.abspath('../..'))`
  
Then I auto-generated all the .rst files for the very small module:
  - sphinx-apidoc -f -o source/ ../mymodule/
  
At this point the docs get generated fine, I do get the following warnings when I run `make html` however:

```

make html

Running Sphinx v1.6.3
loading pickled environment... done
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 0 source files that are out of date
updating environment: 0 added, 1 changed, 0 removed
reading sources... [100%] mymodule
C:\dev\local_spinx_test\docs\source\mymodule.rst:10: **WARNING: error while formatting arguments for mymodule.class_a
.AClass: name 'B' is not defined**
looking for now-outdated files... none found
pickling environment... done
checking consistency... C:\dev\local_spinx_test\docs\source\modules.rst: **WARNING: document isn't included in any 
toctree**
done
preparing documents... done
writing output... [100%] mymodule
generating indices... genindex py-modindex
writing additional pages... search
copying static files... done
copying extra files... done
dumping search index in English (code: en) ... done
dumping object inventory... done
build succeeded, 2 warnings.

Build finished. The HTML pages are in build\html.
```

# ISSUE
If I now:
  - `pip install sphinx-autodoc-typehints`
  
and change my `conf.py` extensions variable from:
  - `extensions = ['sphinx.ext.autodoc']` -> `extensions = ['sphinx.ext.autodoc', 'sphinx_autodoc_typehints']`
  
  I get the following error:
  
  C:\dev\local_spinx_test\docs\source\mymodule.rst:10: WARNING: error while formatting arguments for mymodule.class_a.AClass: name 'B' is not defined

```
Exception occurred:
  File "<string>", line 1, in <module>
NameError: name 'B' is not defined
The full traceback has been saved in C:\Users\HENRY~1.TAN\AppData\Local\Temp\sphinx-err-wnuuyq83.log, if you want to report the issue to the developers.
Please also report this if it was a user error, so that a better error message can be provided next time.
A bug report can be filed in the tracker at <https://github.com/sphinx-doc/sphinx/issues>. Thanks!
```

