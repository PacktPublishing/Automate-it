#Skip header row and read CSV data
import csv
f = open("mylist_wincsv.csv", 'rt')
fw = open("CA_Employees.csv", 'wt')

try:
    reader = csv.DictReader(f)
    csvWriter = csv.writer(fw)
    for row in reader:
        if reader.line_num == 1:
            continue
        if row['state'] == 'CA':
            csvWriter.writerow([row['email'], row['phone']])
finally:
    f.close()
    fw.close()

#Skip header and write data to CSV file
import csv
fr = open("mylist_wincsv.csv", 'rt')
fw = open("header_write.csv", 'wt')
try:
    reader = csv.reader(fr)
    csvWriter = csv.writer(fw)
    reader.next()
    for row in reader:
	csvWriter.writerow(row)
finally:
    fr.close()
    fw.close()
