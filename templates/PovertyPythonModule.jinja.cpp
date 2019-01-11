/*
 * PovertyBoost.cpp
 *
 *  Created on: 9 Jan 2019
 *      Author: pnikiel
 */

#include <boost/python.hpp>
using namespace boost::python;

#include <statuscode.h>
#include <uadatetime.h>

#include <Poverty.hpp>

enum StatusCode
{
    Good = OpcUa_Good,
    Bad = OpcUa_Bad
};

{% for className in classes_cachevariables.keys() %}
//! overloads for cachevariables of {{className}}
{% for cacheVarName in classes_cachevariables[className] %}
BOOST_PYTHON_MEMBER_FUNCTION_OVERLOADS(AS{{className}}_{{cacheVarName}}_overloads, set{{cacheVarName[0].upper()+cacheVarName[1:]}}, 2, 3);
{% endfor %}
{% endfor %}



BOOST_PYTHON_MODULE(PovertyBoost)
{
    enum_<StatusCode>("StatusCode")
        .value("Good", Good)
        .value("Bad", Bad);

    class_<UaDateTime>("UaDateTime")
        .def("now", &UaDateTime::now).staticmethod("now");

    class_<UaStatus>("UaStatus")
        .def("isGood", &UaStatus::isGood);



    {% for className in classes_cachevariables.keys() %}
    class_<AddressSpace::AS{{className}}>("AS{{className}}", no_init)
        {% for cacheVarName in classes_cachevariables[className] %}
        {% set varNameCamel = cacheVarName[0].upper()+cacheVarName[1:] %}
        .def("set{{varNameCamel}}", &AddressSpace::AS{{className}}::set{{varNameCamel}}, AS{{className}}_{{cacheVarName}}_overloads())
        {% endfor %}
        ;
    {% endfor %}

    class_<Poverty>("Poverty")
            .def("startServer", &Poverty::startServer).staticmethod("startServer")
            .def("stopServer", &Poverty::stopServer).staticmethod("stopServer")
            {% for className in classes_cachevariables.keys() %}
                .def("get{{className}}", &Poverty::get{{className}}, return_internal_reference<>()).staticmethod("get{{className}}")
            {% endfor %}

            ;
}
