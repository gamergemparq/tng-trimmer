# TnG Trimmer (and Totaller)

## Overview

The `TnG Trimmer (and Totaller)` python module serves two related purposes:

- `Trim` out unwanted columns in an EXCEL file (set via `config.ini`).
- `Total` (or sum up) the values of a target column.

## Use

1. Download your source EXCEL file and put it in the same folder as `trim.py`

   1.1 Specify it's filename and extension in the `config.ini` file

1. The rest of the configurations in `config.ini` are self-explanatory.
1. Run:

   ```shell
   # Setup your virtualenv however you please.
   # For ease of development, I recommend Python Environment Manager for VS Code.
   $ python -m venv env

   # Install dependencies
   $ pip install -r requirements.txt

   # Run the trimmer
   $ python trim.py
   ```

## Test

```shell
$ pytest
```
