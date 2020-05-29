Poverty, a quasar extension module
==================================

by Piotr P. Nikiel <piotr@nikiel.info>

What is this?
-------------

[Quasar](https://github.com/quasar-team/quasar) is an open-source framework for rapid creation
of OPC-UA software components.

Poverty (this project) is an extension module of Quasar. 
It solves the problem of loading your quasar-made OPC-UA servers from a Python program with
a Python interface which supports:

* controlling the server (start it, stop it, etc ...)
* "operate" its Address-Space, i.e. publish data via OPC-UA from that Python program or read the
cached data.

Basic usage mode
----------------

1. clone this module in your quasar project, or add it as a git submodule,
2. go to the cloned directory (Poverty)
3. mkdir output
4. run python py/generate_poverty.py --design ../Design/Design.xml --output_dir output
5. the files in output directory can be built (include and link against boost-python) and you get your Python wrapper


Why Poverty and not a custom, pure Python OPC-UA solution?
----------------------------------------------------------

There are reasons to use Poverty rather than a pure-Python OPC-UA solution:

* by embedding a quasar made server, you enter the quasar ecosystem which will bring you benefits of
other quasar modules. For example, you could quickly do WinCC OA integration (Cacophony quasar module)
or generate C++ clients (UaObjects for Quasar) or so.

* by making a quasar-based OPC-UA you use carefully tested OPC-UA components, same as these used
in for example LHC experiments controls at CERN.

Why not to use Poverty?
-----------------------

There are also reasons that might prevent you from using Poverty:

* currently, there is no possibly of any call-backs into Python.
* some data types are not supported from Python yet, for example OPC-UA arrays.
