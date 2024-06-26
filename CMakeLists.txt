cmake_minimum_required(VERSION 3.17 FATAL_ERROR)

project(live-transport-network-monitor)

# Dependencies
# If dependencies are managed with conan, we prepend the current build folder
# to the CMake module path, where CMake looks for dependencies.
if(EXISTS ${CMAKE_CURRENT_BINARY_DIR}/conaninfo.txt)
    list(PREPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_BINARY_DIR}")
endif()

find_package(Boost REQUIRED COMPONENTS system)

set(SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp")

add_executable(live-transport-network-monitor ${SOURCES})
target_compile_features(live-transport-network-monitor
    PRIVATE
        cxx_std_23
)
target_link_libraries(live-transport-network-monitor
    PRIVATE
        Boost::boost
)
