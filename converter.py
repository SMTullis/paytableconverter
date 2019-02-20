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
    with io.open("C:/Users/stullis/Downloads/paytables.csv", mode="r") as file:
        data = [line for line in csv.reader(file)]

    return data



def main():
    pass
