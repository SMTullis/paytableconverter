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
    with io.open(filepath, mode = "w+", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def pivot_section(section):
    return [
        line[:2] + [x // 3,] + line[x - 1:x + 2]
        for line in section for x in range(3, 31, 3)
    ]

def main():
    converted_paytables = PayTable("TABLE", "GRADE", "STEP", "ANNUAL", "HOURLY", "OVERTIME")

    file_list = get_user_input_list(
        "Please enter the filepath for each file or [q]uit to exit."
    )

    for file in file_list:
        data = get_data(file)
        converted_paytables.append(pivot_section(data))

    write_to_csv(converted_paytables.output_to_csv(), file_list[0].replace(".csv", "_2.csv"))
