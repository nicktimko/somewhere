> TOTAL CHAOS...for now. Trying to merge the best of both.

# where

Locates absolute file paths like the Windows 'where' or the Linux 'which' utility.
Makes use of the PATH variable and the current directory.

## Usage

### where()
Returns all matching file paths in a list.

    >>> import where

    >>> where.where( "python" )
    ['C:\\Python27\\python.exe']


### first()
Returns first matching file path or None (if nothing found).

    >>> import where

    >>> where.first( "python" )
    'C:\\Python27\\python.exe'

    >>> where.first( "spaghetti-monster" )
    None


# which.py -- a portable GNU which replacement

Home            : http://code.google.com/p/which/
License         : MIT (see LICENSE.txt)
Platforms       : Windows, Linux, Mac OS X, Unix
Dev Status      : mature, has been heavily used in a commercial product for
                  a number of years
Requirements    : Python >= 2.3


`which.py` is a small GNU-which replacement. It has the following
features:

  * it is portable (Windows, Linux, Mac OS X, Un*x);
  * it understands PATHEXT and "App Paths" registration on Windows (i.e. it
    will find everything that `start` does from the command shell);
  * it can print all matches on the PATH;
  * it can note "near misses" on the PATH (e.g. files that match but may not,
    say, have execute permissions); and
  * it can be used as a Python module.
