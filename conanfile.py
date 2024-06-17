from conan import ConanFile

class ConanPackage(ConanFile):
    name = 'live-transport-network-monitor'
    version = "0.1.0"

    settings = "os", "arch", "compiler", "build_type"

    generators = 'CMakeDeps'

    requires = [
    ]
