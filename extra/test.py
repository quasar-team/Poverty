# This is just for testing Poverty.
# Copy or symlink it into build/bin of your quasar OPC-UA server project.

import sys
import os
import time
import readline, rlcompleter

if not os.path.isfile('Poverty.so'):
    raise Exception("Probably running from a wrong directory. Put this script in the dir where Poverty.so is")
sys.path.append('') # add current dir, as it is where Poverty probably is.

import Poverty

# the thing below is for interactive python usage.
readline.parse_and_bind("tab: complete")

backend_config = os.path.sep.join(['..', 'bin', 'ServerConfig.xml'])
config = os.path.sep.join(['..', 'bin', 'config.xml'])



Poverty.Poverty.startServer(backend_config, config)
time.sleep(2)
#t1=Poverty.Poverty.getTemperatureProbe('t1')
