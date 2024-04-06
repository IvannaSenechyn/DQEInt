# AdventureWorks Database Testing with PyTest

## Overview

This project aims to perform basic testing of the AdventureWorks2017 database using pytest. 
The tests are designed to check various aspects of the database tables such as column count, maximum/minimum values,
average value, unique values, data existence, and values within a range.

## Prerequisites

Before running the tests, ensure you have the following installed:

- Python 3.x
- pytest
- pymssql

```bash
pip install pytest
pip install pymssql
pip install pytest-html
```

## Setup

1. Clone the project repository to your local machine
2. Modify the database connection settings in test.py


## Run the tests:

```bash
pytest test.py
```

## Generate an HTML report (optional):

```bash
pytest test.py --html=report.html
```
