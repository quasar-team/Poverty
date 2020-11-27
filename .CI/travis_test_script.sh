./quasar.py set_build_config ./open62541_config.cmake ;
./quasar.py enable_module open62541-compat v1.3.6-rc0 ;
git clone -b OPCUA-2081_CI_test_Poverty https://github.com/quasar-team/Poverty.git ;
echo "set(CUSTOM_SERVER_MODULES Poverty )" >> ProjectSettings.cmake ;
echo "set(BUILD_SERVER_SHARED_LIB ON)" >> ProjectSettings.cmake ;
echo "add_definitions(-fPIC)" >> open62541_config.cmake ;
./quasar.py build ;
