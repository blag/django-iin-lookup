# django-iin-lookup

### For Django

[![pypi](https://img.shields.io/pypi/v/django-iin-lookup.svg)](https://pypi.python.org/pypi/django-iin-lookup/)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/blag/django-iin-lookup/main.svg)](https://results.pre-commit.ci/latest/github/blag/django-iin-lookup/main)
<!-- [![tests ci](https://github.com/blag/django-iin-lookup/workflows/tests/badge.svg)](https://github.com/blag/django-iin-lookup/actions) -->

**django-iin-lookup** provides a case-insensitive `IN` lookup (`.filter(myfield__iin=[...])`) for Django database queries


## Compatibility

- Python: >= **3.14**
- Django: >= **4.2**


## Installation

1. Install the latest version:

   ```sh
   pip install django-iin-lookup
   ```

   ```sh
   uv add django-iin-lookup
   ```

2. Add `iin` to `INSTALLED_APPS` in your project's `settings.py`.
