import csv
import json


def get_keys(filename, dialect):
    """
    Returns headers for a given CSV file.
    :param filename: CSV file to get the headers for.
    :param dialect: The dialect of the CSV file.
    :return: Python list of headers.
    """
    with open(filename, 'r') as ifile:
        reader = csv.DictReader(ifile, dialect=dialect)
        for row in reader:
            print(row.keys())
            break


def read_aventura(filename, dialect):
    """
    Returns a Python ordered dict for a CSV file.
    :param filename: CSV file to open and read.
    :param dialect: The dialect of the CSV file.
    :return: All content of the CSV file is printed to stdout.
    """
    with open(filename, 'r') as ifile:
        reader = csv.DictReader(ifile, dialect=dialect)
        for row in reader:
            print(row)


def create_ini_file(csvfilename, dialect, inifilename):
    """
    Creates an ini file for BankCSVtoQif to prepare transactions with the correct categories.
    :param csvfilename: CSV file to open and read.
    :param dialect: The dialect of the CSV file.
    :param inifilename: The INI file that contains the rules to map PAYEES to GnuCash ACCOUNTS.
    :return: None
    """
    ## Open CSV file for reading
    with open(csvfilename, 'r') as ifile:
        ## Open INI file (truly a JSON file) for writing
        with open(inifilename, 'w') as ofile:
            reader = csv.DictReader(ifile, dialect=dialect)
            new_list = []
            new_dict = {'cibc_aventura': new_list}

            ## Add entries to INI file dict
            for row in reader:
                a_list = []
                a_list.append(row['2words'])
                a_list.append("")
                a_list.append(row['account'])
                a_list.append(0)
                new_list.append(a_list)

            ## Save JSON text in INI file
            text = json.dumps(new_dict)
            ofile.write(text)


if __name__ == "__main__":
    _ = r'../do_not_commit/aventura_2018jul.csv'
    csv.register_dialect('aventura', delimiter='\t', quoting=csv.QUOTE_MINIMAL)
    #get_keys(_, 'aventura')
    #read_aventura(_, 'aventura')
    create_ini_file(_, 'aventura', '../do_not_commit/aventura.ini')

