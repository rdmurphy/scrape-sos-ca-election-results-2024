import csv


def csv_to_aria2_input(csv_filename, aria2_input_filename):
    with open(csv_filename, 'r') as csv_file, open(aria2_input_filename, 'w') as aria2_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            aria2_file.write(row['api_url'] + '\n')
            aria2_file.write('  out=' + row['label'] + ".json" + '\n\n')

csv_to_aria2_input('endpoints.csv', 'input.txt')
