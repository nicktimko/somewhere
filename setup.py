import setuptools

setuptools.setup(
    name="where",
    packages=["where"],
    version="1.0.2",
    description=description,
    author='Henry Weickert',
    author_email='henryweickert@gmail.com',
    url='https://github.com/hweickert/where',
    keywords=['where', 'which'],
    entry_points={
        'console_scripts': [
            'where = where.__main__:main',
        ]
    },
)
#!/usr/bin/env python
# Copyright (c) 2002-2005 ActiveState Corp.
# Author: Trent Mick (TrentM@ActiveState.com)

"""Distutils setup script for 'which'."""

import sys
import os
import shutil


description = "Locates files like the Windows 'where' or the Linux 'which' utilities."

long_description = """\
This is a GNU which replacement with the following features:
- it is portable (Windows, Linux);
- it understands PATHEXT on Windows;
- it can print <em>all</em> matches on the PATH;
- it can note "near misses" on the PATH (e.g. files that match but
  may not, say, have execute permissions; and
- it can be used as a Python module.
"""

def _getBinDir():
    """Return the current Python's bindir."""
    if sys.platform.startswith("win"):
        bindir = sys.prefix
    else:
        bindir = os.path.join(sys.prefix, "bin")
    return bindir


setuptools.setup(
    name="somewhere",
    packages=['somewhere'],
    version=which.__version__,
    description=description,
    author="Nick Timkovich",
    author_email="prometheus235@gmail.com",
    url="http://github.com/nicktimko/",
    license="MIT License",
    platforms=["Windows", "Linux", "Mac OS X", "Unix"],
    long_description=long_description,
    keywords=["which", "find", "path", "where"],

)
