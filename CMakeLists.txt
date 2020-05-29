

add_custom_command(
OUTPUT 
${PROJECT_BINARY_DIR}/Poverty/output/Poverty.hpp
${PROJECT_BINARY_DIR}/Poverty/output/Poverty.cpp
${PROJECT_BINARY_DIR}/Poverty/output/PovertyPythonModule.cpp
WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
COMMAND ${CMAKE_COMMAND} -E make_directory ${PROJECT_BINARY_DIR}/Poverty/output
COMMAND ${PYTHON_COMMAND} Poverty/py/generate_poverty.py --design ${DESIGN_FILE} --output_dir ${PROJECT_BINARY_DIR}/Poverty/output
DEPENDS ${DESIGN_FILE} templates/Poverty.hpp.jinja templates/Poverty.jinja.cpp templates/PovertyPythonModule.jinja.cpp py/generate_poverty.py
)

include_directories(${PROJECT_BINARY_DIR}/Poverty/output)

# the following target will simply be included quasar server
add_library(Poverty OBJECT
        ${PROJECT_BINARY_DIR}/Poverty/output/Poverty.hpp
        ${PROJECT_BINARY_DIR}/Poverty/output/Poverty.cpp
        )       
    
add_dependencies(Poverty AddressSpace)    
    
# --- from this line on, we deal with building the Python extension and no longer with anything related to quasar.    
  
execute_process(COMMAND python-config --cflags OUTPUT_VARIABLE python_config_cflags)
add_definitions(${python_config_cflags})

set( SERVER_SHARED_LIB_TARGET ${EXECUTABLE}Object )

add_library( PovertyPython SHARED
        ${PROJECT_BINARY_DIR}/Poverty/output/PovertyPythonModule.cpp
        )
target_link_libraries(PovertyPython boost_python-mt ${SERVER_SHARED_LIB_TARGET})
set_target_properties(PovertyPython PROPERTIES PREFIX "" OUTPUT_NAME "Poverty") 
add_dependencies(PovertyPython ${SERVER_SHARED_LIB_TARGET})
