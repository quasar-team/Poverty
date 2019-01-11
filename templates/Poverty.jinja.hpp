/*
 * Poverty.h
 *
 *  Created on: 17 Dec 2018
 *      Author: pnikiel
 */

#ifndef __POVERTY_HEADER__
#define __POVERTY_HEADER__

#include <string>
{% for className in classes_cachevariables.keys() %}
#include <AS{{className}}.h>
{% endfor %}

class Poverty
{

public:
    //! Starts up a quasar server in Poverty mode.
    static bool startServer(
            const std::string& backendConfigPath,
            const std::string& configPath);

    //! Return true when server is considered stopped.
    static bool stopServer();

    {% for className in classes_cachevariables.keys() %}
    static AddressSpace::AS{{className}}* get{{className}}(const std::string& address);
    {% endfor %}

};



#endif /* __POVERTY_HEADER__ */
