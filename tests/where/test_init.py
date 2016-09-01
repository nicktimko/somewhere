import pytest

import where


def test_where_first_executes():
    where.first("python")


def test_where_where_executes():
    where.where("python")


def test_where_iwhere_executes():
    where.iwhere("python")


def test_windows_matches():
    fake_paths = ['C:\\', 'C:\\Python35']
    paths = [fp + '\\python' for fp in fake_paths]
    win_paths = list(where._gen_windows_matches(paths))

    for fp in fake_paths:
        assert fp + '\\python.exe' in win_paths


if __name__ == "__main__":
    pytest.main([__file__, "-s"])
