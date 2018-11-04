import csv
import os
import sys

def parse_csv(path):
    try:
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                name = row[0]
                phone = row[1]
                title = row[2]
                print(name, phone, title)
    except OSError as e:
        print('Error', e)

def test_parse_csv():
    parse_csv('testdata.csv')

if __name__ == '__main__':
    if 'TEST' in os.environ.keys():
        test_parse_csv()
    else:
        parse_csv(sys.argv[1])
