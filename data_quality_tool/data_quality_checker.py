import pandas as pd
import argparse
import sys
from jinja2 import Environment, FileSystemLoader


def check_data_quality(file_path):
    """
    Checks the data quality of a CSV or Excel file and generates an HTML report.
    """
    file_path_str = str(file_path)

    try:
        if file_path_str.endswith('.csv'):
            df = pd.read_csv(file_path_str)
        elif file_path_str.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file_path_str)
        else:
            raise ValueError("Unsupported file format. Please provide a .csv, .xlsx, or .xls file.")
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file '{file_path_str}' was not found.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {e}")

    # Gather data quality metrics
    missing_values = df.isnull().sum().to_dict()
    duplicates_count = df.duplicated().sum()
    dtypes = df.dtypes.to_dict()

    # Render the HTML report
    from pkg_resources import resource_filename

    # Use pkg_resources to find the template file within the installed package
    template_path = resource_filename('data_quality_tool', 'templates')
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template('report_template.html')

    report_data = {
        'file_name': file_path_str,
        'shape': df.shape,
        'missing_values': {k: v for k, v in missing_values.items() if v > 0},
        'duplicates_count': duplicates_count,
        'dtypes': dtypes
    }

    html_report = template.render(report_data)

    # Save the report to a file
    report_file_name = file_path_str.split('.')[0] + '_report.html'
    with open(report_file_name, 'w') as f:
        f.write(html_report)

    print(f"Data quality report generated successfully: {report_file_name}")


def main():
    """
    Main function to handle command-line arguments.
    """
    parser = argparse.ArgumentParser(description='A simple data quality checker for CSV and Excel files.')
    parser.add_argument('file_path', help='Path to the input CSV or Excel file.')

    args = parser.parse_args()

    try:
        check_data_quality(args.file_path)
    except (FileNotFoundError, ValueError, Exception) as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()