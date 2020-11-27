# Prerequisite: at this stage, both quasar and Poverty should be already cloned, with respective branched.
./quasar.py set_build_config ./open62541_config.cmake ;
./quasar.py enable_module open62541-compat v1.3.6-rc0 ;
echo "set(CUSTOM_SERVER_MODULES Poverty )" >> ProjectSettings.cmake ;
echo "set(BUILD_SERVER_SHARED_LIB ON)" >> ProjectSettings.cmake ;
echo "set(POVERTY_STRICTLY_PYTHON3 ON)" >> ProjectSettings.cmake ;
echo "set(ADDITIONAL_BOOST_LIBS python3 )" >> ProjectSettings.cmake ;
echo "add_definitions(-fPIC)" >> open62541_config.cmake ;
./quasar.py build ;
cp Poverty/extra/test.py build/bin ;
cd build/bin ;
ln -s ../Poverty/Poverty.so . ;
python3 -i test.py ;
