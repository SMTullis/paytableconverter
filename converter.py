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

def get_user_input_list(message):
    out = []
    while True:
        input(message)

        if message.lower() in ["quit", "q", "exit", "n", "no"]:
            return out

def get_data(filepath):
    with io.open(filepath, mode="r") as file:
        interim = [line for line in csv.reader(file)]
        data = [line for line in interim[1:]]

    return data

def write_to_csv(data, filepath):
    with io.open(filepath, mode = "w+") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def main():
    converted_paytables = PayTable("TABLE", "GRADE", "STEP", "ANNUAL", "HOURLY", "OVERTIME")

    file_list = get_user_input_list(
        "Please enter the filepath for each file or [q]uit to exit."
    )

    for file in file_list:
        data = get_data(file)
