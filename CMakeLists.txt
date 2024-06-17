cmake_minimum_required(VERSION 3.17 FATAL_ERROR)

project(live-transport-network-monitor)

set(SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp")

add_executable(live-transport-network-monitor ${SOURCES})
target_compile_features(live-transport-network-monitor
    PRIVATE
        cxx_std_23
)