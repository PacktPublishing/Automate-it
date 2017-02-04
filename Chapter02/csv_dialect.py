import csv

#Register a new dialect with name and delimete
csv.register_dialect('pipes', delimiter='-')

#Read a CSV file with new dialect
with open('pipes.csv', 'r') as f:
    reader = csv.reader(f, dialect='pipes')
    for row in reader:
        print row

