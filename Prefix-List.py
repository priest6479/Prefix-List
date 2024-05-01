import csv


def generate_prefix_list(csv_file, prefix_list_name):
    prefix_list = []

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            prefix_list.append(row[0])

    config = ""
    seq_num = 10  # Starting sequence number
    for prefix in prefix_list:
        config += "ip prefix-list {} seq {} permit {}\n".format(prefix_list_name, seq_num, prefix)
        seq_num += 10  # Increment sequence number by 10

    return config


def main():
    csv_file = "prefixes.csv"  # Path to your CSV file
    prefix_list_name = input("Enter the Name of your Prefix-List: ")  # Name of your prefix-list

    config = generate_prefix_list(csv_file, prefix_list_name)

    with open("prefix_list_config.txt", "w") as output_file:
        output_file.write(config)

    print("Prefix-list configuration generated successfully.")


if __name__ == "__main__":
   main()