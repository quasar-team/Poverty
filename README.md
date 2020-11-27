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

Note: tested with quasar version nebula.B1 (shall correspond to 1.5+)

1. Steps to do in your quasar project
   1. add `-fPIC` in the `add_definitions` of your build config
   1. in `ProjectSettings.cmake` (root of your quasar project):
      1. set `BUILD_SERVER_SHARED_LIB` to `ON`.
      1. add `Poverty` to `CUSTOM_SERVER_MODULES`.
      1. add `python3` to `ADDITIONAL_BOOST_LIBS`.
      1. set `POVERTY_STRICTLY_PYTHON3` in case your system can have both python2 and python3 (most      systems). I.e. your system needs to have `python3-config` command visible!
   1. Poverty current only works with open62541 backend of quasar. Thus if you are with UA-SDK, switch to open62541.
1. clone Poverty (this GitHub repo) in your quasar project, or add it as a git submodule,
1. build your OPC-UA server (e.g. `./quasar.py build`)

To test it:

1. in your quasar project, copy the test python script `Poverty/extra/test.py` into `build/bin`
1. copy, or symlink, `build/Poverty.so` into `build/bin`
1. run the test program: `python3 test.py`

Distributing your Poverty+quasar based OPC-UA server
----------------------------------------------------

You need the following files in your target application:
* Poverty.so (builds in build/Poverty)
* libOpcUaServer.so (builds in build/bin)
* the particular config file of the server (which has instanced of quasar objects ...), normally called config.xml
* the particular ServerConfig.xml where stuff like endpoints and OPC-UA certificates are defined.






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
