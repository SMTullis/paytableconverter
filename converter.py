import csv
import io

class PayTable:

    def __init__(self, *header):
        self.data = [header, ]

    def append(self, row):
        self.data.extend(row)

    def output_to_csv(self):
        return self.data

def get_user_input_list(message):
    out = []
    while True:
        user_input = input(message)

        if user_input.lower() in ["quit", "q", "exit", "n", "no"]:
            return out

        out.append(user_input)

def get_data(filepath):
    with io.open(filepath, mode="r") as file:
        interim = [line for line in csv.reader(file)]
        data = [line for line in interim[1:]]

    return data

def write_to_csv(data, filepath):
    with io.open(filepath, mode = "w+") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def pivot_section(section):
    pivoted_table = []
    for line in section:
        pivot_point = line[:2]
        for x in range(3, 31, 3):
            pivoted_table.append(
                pivot_point + [x // 3,] + line[x - 1:x + 2]
            )

    return pivoted_table

def main():
    converted_paytables = PayTable("TABLE", "GRADE", "STEP", "ANNUAL", "HOURLY", "OVERTIME")

    file_list = get_user_input_list(
        "Please enter the filepath for each file or [q]uit to exit."
    )

    for file in file_list:
        data = get_data(file)
