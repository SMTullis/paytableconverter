import csv
import decimal
import io

class PayTable:

    def __init__(self, *header):
        data = [header, ]

    def append(self, *row):
        data.append(row)

    def output_to_csv(self):
        return data


def get_data(filepath):
    with io.open(filepath, mode="r") as file:
        data = [line for line in csv.reader(file)]

    return data

def write_to_csv(data, filepath):
    with io.open(filepath, mode = "w+") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def main():
    pass
