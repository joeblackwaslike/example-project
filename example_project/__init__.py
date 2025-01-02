"""This is a template repository for Python projects that use uv for their dependency management."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("example_project")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
