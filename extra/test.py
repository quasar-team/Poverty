import time
import readline, rlcompleter
readline.parse_and_bind("tab: complete")
import Poverty
backend_config = '/home/pnikiel/gitProjects/PovertyTest2/bin/ServerConfig.xml'
config = '/home/pnikiel/gitProjects/PovertyTest2/bin/config.xml'
Poverty.Poverty.startServer(backend_config, config)
time.sleep(2)
t1=Poverty.Poverty.getTemperatureProbe('t1')
