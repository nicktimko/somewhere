from __future__ import absolute_import

import os
import platform
import itermate


WINDOWS_EXTENSIONS = ['', '.bat', '.com', '.exe']


def where(filename):
    """Returns all matching file paths."""
    return list(iwhere(filename))


def first(filename):
    """Returns first matching file path."""
    try:
        return next(iwhere(filename))
    except StopIteration:
        return None


def iwhere(filename):
    """Like where() but returns an iterator."""
    possible_paths = _gen_possible_matches(filename)
    existing_file_paths = (p for p in possible_paths if os.path.isfile(p))
    return existing_file_paths


def _gen_windows_matches(paths):
    for path in paths:
        for ext in WINDOWS_EXTENSIONS:
            yield path + ext


def _gen_possible_matches(filename):
    path_parts = os.environ.get("PATH", "").split(os.pathsep)
    path_parts = itertools.chain((os.curdir,), path_parts)
    possible_paths = (os.path.join(path_part, filename) for path_part in path_parts)

    if platform.system() == "Windows":
        possible_paths = itermate.imapchain(_gen_windows_matches, possible_paths)

    possible_paths = (os.path.abspath(p) for p in possible_paths)

    result = itermate.unique(possible_paths)

    return result
