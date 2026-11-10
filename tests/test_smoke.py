"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import codepulse


def test_version_is_set() -> None:
    assert codepulse.__version__
