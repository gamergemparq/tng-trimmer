
import pandas as pd
import sys
import getopt
import pathlib
import configparser


def check_files(argv):

    # Get arguments.
    opts, args = getopt.getopt(argv, "hi:o:s:", ["ifile=", "ofile="])
    for opt, arg in opts:
        if opt == '-h':
            print('trim.py -i <input_file_ms_excel> -o <output_file>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg

    # Exit if no input file or output file.
    if len(input_file) < 2 or len(output_file) < 2:
        print('Please specify input file or output file.')
        sys.exit()

    # Exit if input file is not excel files.
    input_file_extension = pathlib.Path(input_file).suffix

    if input_file_extension not in ['.xlsx', '.xls']:
        print('Please specify an Excel file as input')
        sys.exit()

    # Force append .xlsx extension.
    output_file = pathlib.Path(output_file).stem + '.xlsx'

    # Return only sanitized input and output filenames.
    return input_file, output_file


def main(argv):
    # Read config file.
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Getting config values.
    lst_cols_to_keep = config['DEFAULT']['columns_to_keep'].split(',')
    col_to_calc_sum = config['DEFAULT']['column_to_calc_sum']

    filter_col_name = config['FILTER']['column_name']

    # Remove whitespace from values in config file.
    original_value_to_filter = config['FILTER']['value_to_filter'].split(',')
    lst_filter_value_to_filter = [
        elem.strip() for elem in original_value_to_filter]

    # Supply input and output filenames to be sanitized.
    argv_list = ['-i', config['DEFAULT']['source_file_name'], '-o', config['DEFAULT']
                 ['output_file_name']]
    input_file, output_file = check_files(argv_list)

    # Read by default, 1st sheet of an excel file.
    df = pd.read_excel(input_file)

    # Keeping only the columns needed.
    trimmed_df = df[lst_cols_to_keep]

    # Ensure records left are the ones that need processing, removing the others.
    col_to_be_processed_df = trimmed_df[trimmed_df[filter_col_name].isin(
        lst_filter_value_to_filter)]

    # Show proof to user.
    print(col_to_be_processed_df.tail())

    # Calculate the sum of the targetted column.
    total_sum = sum(col_to_be_processed_df[col_to_calc_sum])

    # Convert df to list, for next step.
    lst_from_df = col_to_be_processed_df.values.tolist()

    # Append new row.
    new_row = ['', '', 'Total = ', total_sum]
    lst_from_df.append(new_row)

    # Convert to df, for next step.
    df_to_excel = pd.DataFrame(lst_from_df, columns=lst_cols_to_keep)

    # Save as Excel.
    df_to_excel.to_excel(output_file, index=False)

    # Print to screen to be easily copied by user
    print(F'TOTAL: {total_sum}')


if __name__ == "__main__":
    main(sys.argv[1:])
