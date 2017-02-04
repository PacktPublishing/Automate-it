import csv

#Read a CSV file with reader() method
#Returns an expection for Mac OS
fh = open("mylist.csv", 'rt')
try:
    reader = csv.reader(fh)
    print "Data from the CSV:", list(reader)
except Exception as e:
    print "Exception is:", e
finally:
    fh.close()

print "Available Dialects:", csv.list_dialects()
# The standard library includes two dialects: excel, and excel-tabs.
# The excel dialect is for working with data in the default export format for Microsoft Excel,
# and also works with OpenOffice or NeoOffice.

#Read the CSV file with universal new line mode
try:
    reader = csv.reader(open("mylist.csv", 'rU'),
                        dialect=csv.excel_tab)
    print "Data from the CSV:"
    d = list(reader)
    print "\n".join("%-20s %s"%(d[i],d[i+len(d)/2]) for i in range(len(d)/2))

except Exception as e:
    print "Exception is:", e
finally:
    fh.close()

#Convert the file in Windows CSV format
#and then read the file contents cell by cell

fh = open("mylist_wincsv.csv", 'rt')
reader = csv.reader(fh)
data = list(reader)
print "Data cells from CSV:"
print data[0][1], data[1][1]
print data[0][2], data[1][2]
print data[0][3], data[1][3]


#Read data from CSV file with a for loop
import csv
f = open("mylist_wincsv.csv", 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        print row
finally:
    f.close()

#Read CSV file contents in Python dictionary
import csv
f = open("mylist_wincsv.csv", 'rt')
print "File Contents"
try:
    reader = csv.DictReader(f)
    for row in reader:
        print row['first_name'], row['last_name'], row['email']
finally:
    f.close()

#Understanding Reader Objects and Attributes
import csv
f = open("mylist_wincsv.csv", 'rt')
reader = csv.DictReader(f)
print "Columns in CSV file:", reader.fieldnames
print "Dialect used in CSV file:", reader.dialect
print "Current line number in CSV file:", reader.line_num
print "Moving the reader to next line with reader.next()"
reader.next()
print "Reading line number:", reader.line_num
f.close()
