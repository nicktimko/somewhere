import pytest

import where


def test_where_first_executes():
    where.first("python")


def test_where_where_executes():
    where.where("python")


def test_where_iwhere_executes():
    where.iwhere("python")


def test_windows_matches():
    assert 'python.exe' in list(where._gen_windows_matches('python'))


if __name__ == "__main__":
    pytest.main([__file__, "-s"])
