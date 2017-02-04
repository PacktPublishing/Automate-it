#Add a list of names and grades to a CSV file
import csv
names = ["John", "Eve", "Fate", "Jadon"]
grades = ["C", "A+", "A", "B-"]
f = open("newlist.csv", 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('Sr.', 'Names', 'Grades') )
    for i in range(4):
        writer.writerow( (i+1, names[i], grades[i]) )
finally:
    f.close()

#Read the CSV file and confirm if contents got added
print open("newlist.csv", 'rt').read()

#Understanding Delimiter and lineterminator
import csv
f=open("write.csv", 'wt')
csvWriter = csv.writer(f, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['abc', 'pqr', 'xyz'])
csvWriter.writerow(['123', '456', '789'])
f.close()
