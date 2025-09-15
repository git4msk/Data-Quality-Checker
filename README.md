 
# Data-Quality-Checker

A lightweight Python command-line interface (CLI) tool that scans CSV and Excel files to check for common data quality issues. It generates a clean, user-friendly HTML report summarizing missing values, duplicate rows, and data types.

## Features

  * **File Compatibility**: Works with both `.csv` and `.xlsx` files.
  * **Missing Value Detection**: Identifies and reports the count of missing values per column.
  * **Duplicate Row Check**: Counts the number of duplicate rows in the dataset.
  * **HTML Report Generation**: Creates a visually appealing and easy-to-read report, ready to be viewed in a web browser.
  * **Packaged as a Library**: Can be installed and used as a command-line tool from any directory.

-----

## Installation

To get started, first clone the repository and then install the package in an editable mode within your Python virtual environment.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/<your-username>/Data-Quality-Checker.git
    cd Data-Quality-Checker
    ```

2.  **Install the package:**

    ```bash
    pip install -e .
    ```

-----

## Usage

Run the tool from your terminal with the path to your data file as an argument.

```bash
data_quality_checker your_data_file.csv
```

A report named `your_data_file_report.html` will be generated in the same directory where you ran the command.

-----

## Skills Showcased

  * **Python Programming**: Core logic for data analysis and application development.
  * **Pandas**: Utilized for efficient data manipulation and validation.
  * **Argparse**: Implemented a custom command-line interface (CLI) for easy use.
  * **Jinja2**: Used as a templating engine to generate the HTML report.
  * **setuptools**: Packaged the project as a reusable and distributable Python library.
  * **Git & GitHub**: Employed for version control, collaboration, and project hosting.
