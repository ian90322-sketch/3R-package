

# 3R-package

A Python command-line tool for descriptive statistics.

## Features

- Count
- Mean
- Median
- Sample variance
- Sample standard deviation
- Minimum and maximum
- Range

## Installation

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install .
```

## Usage

```bash
three_r_package --numbers "10,20,30,40,50"
```

## Example Output

```text
Count               : 5
Mean                : 30.00
Median              : 30.00
Sample Variance     : 250.00
Sample Std Dev      : 15.81
Minimum             : 10.00
Maximum             : 50.00
Range               : 40.00
```

## Requirements

- Python 3.10 or above
- Click

## Author

Ian Shih
