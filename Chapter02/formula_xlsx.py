import xlsxwriter

#Create a workbook and add worksheet
workbook = xlsxwriter.Workbook('formula.xlsx')
worksheet = workbook.add_worksheet()

#Create a formulae to add three numbers
#and store the sum in cell A1
worksheet.write_formula('A1', '=SUM(1, 2, 3)')

#Close the workbook object
workbook.close()
