# functions for managing files
import common
import csv
import os


def get_data_from_file(file_name):
    data_dict = []
    with open(file_name, 'r+') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_dict.append(dict(row))
        return data_dict


def add_data_to_file(file_name, new_data, labels):
    exists = os.path.isfile(file_name)
    prepared_new_data = common.prepare_data_for_dictwriter(new_data)

    with open(file_name, 'a+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=labels, delimiter=',')
        if not exists:
            writer.writeheader()
        writer.writerow(prepared_new_data)


def check_labels_in_csv(file_name, labels):
    bytes_of_row_in_csv_line = 72
    with open(file_name, 'r+') as csvfile:
        first_line = csvfile.readline(bytes_of_row_in_csv_line)
        if not first_line == ','.join(labels):
            csvfile.write(','.join(labels))
