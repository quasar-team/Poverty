import time
import readline, rlcompleter
readline.parse_and_bind("tab: complete")
import Poverty
backend_config = '/home/pnikiel/gitProjects/OPCUA-1180_quasar_via_swig/bin/ServerConfig.xml'
config = '/home/pnikiel/gitProjects/OPCUA-1180_quasar_via_swig/build/bin/config.xml'
Poverty.Poverty.startServer(backend_config, config)
time.sleep(2)
t1=Poverty.Poverty_getTemperatureProbe('t1')
