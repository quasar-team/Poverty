

add_custom_command(
OUTPUT
${PROJECT_BINARY_DIR}/Poverty/output/Poverty.hpp
${PROJECT_BINARY_DIR}/Poverty/output/Poverty.cpp
${PROJECT_BINARY_DIR}/Poverty/output/PovertyPythonModule.cpp
WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
COMMAND ${CMAKE_COMMAND} -E make_directory ${PROJECT_BINARY_DIR}/Poverty/output
COMMAND ${PYTHON_COMMAND} Poverty/py/generate_poverty.py --output_dir ${PROJECT_BINARY_DIR}/Poverty/output
DEPENDS ${DESIGN_FILE} templates/Poverty.hpp.jinja templates/Poverty.cpp.jinja templates/PovertyPythonModule.cpp.jinja py/generate_poverty.py
)

include_directories(${PROJECT_BINARY_DIR}/Poverty/output)

# the following target will simply be included quasar server
add_library(Poverty OBJECT
  ${PROJECT_BINARY_DIR}/Poverty/output/Poverty.hpp
  ${PROJECT_BINARY_DIR}/Poverty/output/Poverty.cpp
  )

add_dependencies(Poverty AddressSpace)

# --- from this line on, we deal with building the Python extension and no longer with anything related to quasar.
if(POVERTY_STRICTLY_PYTHON3)
  set(python_config_command "python3-config")
else(POVERTY_STRICTLY_PYTHON3)
  set(python_config_command "python-config")
endif(POVERTY_STRICTLY_PYTHON3)
execute_process(COMMAND ${python_config_command} --cflags OUTPUT_VARIABLE python_config_cflags RESULT_VARIABLE return_code)
if (NOT ${return_code} EQUAL 0)
  message(FATAL_ERROR "${python_config_command} tool returned ${return_code}, that is non-zero! Can't obtain information on python headers ...")
endif ()
message("NOTE: running ${python_config_command} --cflags returned: ${python_config_cflags}")
add_definitions(${python_config_cflags})

execute_process(COMMAND ${python_config_command} --libs OUTPUT_VARIABLE python_config_libs OUTPUT_STRIP_TRAILING_WHITESPACE)
message("NOTE: running ${python_config_command} --libs returned: ${python_config_libs}")
execute_process(COMMAND ${python_config_command} --ldflags OUTPUT_VARIABLE python_config_ldflags OUTPUT_STRIP_TRAILING_WHITESPACE)
message("NOTE: running ${python_config_command} --ldflags returned: ${python_config_ldflags}")

set( SERVER_SHARED_LIB_TARGET ${EXECUTABLE}Object )

set (CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} ${python_config_ldflags}")

add_library( PovertyPython SHARED
        ${PROJECT_BINARY_DIR}/Poverty/output/PovertyPythonModule.cpp
        )
target_link_libraries(PovertyPython boost_python-mt ${python_config_libs} ${SERVER_SHARED_LIB_TARGET})
set_target_properties(PovertyPython PROPERTIES PREFIX "" OUTPUT_NAME "Poverty")
add_dependencies(PovertyPython ${SERVER_SHARED_LIB_TARGET})
