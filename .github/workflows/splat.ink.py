steps:
- uses: actions/checkout@v2
- uses: actions/setup-python@v2
  with:
    python-version: '3.x' # Version range or exact version of a Python version to use, using SemVer's version range syntax
    architecture: 'x64' # optional x64 or x86. Defaults to x64 if not specified
- run: python my_script.py
