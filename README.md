## Tax Report Generator

```
# Note: Install Python 3

# Note: install Poetry for Linux
$: curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Note: install Poetry for Windows
$: (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
# Note: do NOT update Poetry, it will break itself

$: python get-poetry.py --uninstall
```

```
$: poetry install  # install all dependencies
```

### dist

```
$: pip install dist/tax_report_generator-0.1.0-py3-none.any.whl

$: tax-report-generator
```

### docs

```
$: poetry shell
$: cd docs
# Note: review source/conf.py and source/index.rst
$: make html
# Note: see docs in docs/build/apidocs/index.html
```

### tax_report_generator

```
$: poetry run python ./tax_report_generator/runner.py
```

### tests

```
$: poetry run pytest --durations=0
```

```
$: poetry run pytest --cov=tax_report_generator --cov-report=html tests
#: Note: see coverage report in htmlcov/index.html
```

### poetry.lock

Dependencies, Python version and the virtual environment are managed by `Poetry`.

```
$: poetry search Package-Name
$: poetry add Package-Name[==Package-Version]
```

### pyproject.toml

Define project entry point and metadata.  

### setup.cfg

Configure Python libraries.  

### Linters

```
$: poetry run black .
```

### Publish

```
$: poetry config pypi-token.pypi PyPI-API-Access-Token

$: poetry publish --build
```

```
https://pypi.org/project/tax-report-generator/
```

# Extra

### Inputs

Data, settings and command line arguments.  
Data is supplied using well formed, tidy Excel tables.  
Settings specify the tax report metadata.  
Command line arguments tell the program which tax reports you want to generate.  

### Outputs

Tax reports.  

### Command Line Parsing

Python's "argparse" is responsible for extracting arguments and mapping them to Excel file names.

### Pathfinding

Python's "os" makes sure that file paths are constructed correctly.

### Data Wrangling

Using "pandas" and "openpyxl" Excel tables are loaded, filtered and inserted into a data frame wrapper.  
I went to great lengths not to have "magic numbers" around the code.  
Most literal values, that is constants, are in settings files.

### Generating XML Reports

Using "lxml" XML template files are parsed and loaded into memory as XML trees.  
XML trees are then filled with data from the data frame wrapper.  
Data filled XML trees are then connected together to form a larger XML tree.  
In the end, the XML tree is serialized into a XML file.  
