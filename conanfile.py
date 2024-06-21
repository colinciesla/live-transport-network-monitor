from conan import ConanFile
from conan.tools.cmake import cmake_layout

class ConanPackage(ConanFile):
    name = 'live-transport-network-monitor'
    version = "0.1.0"

    settings = "os", "arch", "compiler", "build_type"

    generators = 'CMakeDeps', "CMakeToolchain"

    def requirements(self):
        self.requires("boost/1.85.0")

    def layout(self):
        cmake_layout(self)

    default_options = {
        "boost/*:shared": False
    }
