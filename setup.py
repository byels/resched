import os
import setuptools

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools.setup(
    name="Resched",
    version="0.0.1",
    author="Kiril Savino",
    description="super simple Redis scheduling & queueing in Python",
    license="BSD",
    keywords="redis queue schedule",
    url="http://github.com/gamechanger/resched",
    packages="resched",
    long_description=read("README"),
    )