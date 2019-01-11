/*
 * Poverty.cpp
 *
 *  Created on: 17 Dec 2018
 *      Author: pnikiel
 */

#include <thread>

#include <QuasarServer.h>
#include <shutdown.h>

#include <Poverty.hpp>

#include <ASNodeQueries.h>

static std::thread s_serverThread;
static QuasarServer* s_quasarServer = nullptr;

int serverThread (
        const std::string& backendConfigPath,
        const std::string& configPath
        )
{
    QuasarServer quasarServer;
    s_quasarServer = &quasarServer;
    char thisPath[] = ".";
    char backendConfigOpt[] = "--opcua_backend_config";
    const char* argv [] = {thisPath, backendConfigOpt, backendConfigPath.c_str(), configPath.c_str()};
    int returnCode = quasarServer.startApplication(sizeof argv / sizeof argv[0], (char**)argv);
    s_quasarServer = nullptr;
    return returnCode;
}

bool Poverty::startServer(
        const std::string& backendConfigPath,
        const std::string& configPath
        )
{
    s_serverThread = std::thread( serverThread, backendConfigPath, configPath );
    return true;
}

bool Poverty::stopServer()
{
    if (!s_quasarServer)
        return true;
    g_ShutDown = true;
    g_RunningFlag = false;
    s_serverThread.join();
    return true;
}

{% for className in classes_cachevariables.keys() %}
AddressSpace::AS{{className}}* Poverty::get{{className}}(const std::string& address)
{
    if (!s_quasarServer)
        throw std::runtime_error("Server not started, cant get node!");
    auto result = AddressSpace::findByStringId<AddressSpace::AS{{className}}>(s_quasarServer->getNodeManager(), address);
    if (!result)
        throw std::runtime_error("Object not existing, check your server config file"); // TODO print which object was searched
    return result;
}
{% endfor %}
