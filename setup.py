import setuptools


description = r"""Locates absolute file paths like the Windows 'where' or the Linux 'which' utility.
Makes use of the PATH variable and the current directory."""

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
