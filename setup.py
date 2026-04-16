from setuptools import setup
from setuptools.command.install import install
import os

class CustomInstall(install):
    def run(self):
        os.system("id")
        install.run(self)

setup(
    name='legitimate-package',
    version='1.0.0',
    cmdclass={'install': CustomInstall},
)
