import xlsxwriter

#Create workbook and add a worksheet
workbook = xlsxwriter.Workbook('cell_format.xlsx')
worksheet = workbook.add_worksheet()

#Tuple showing all expenses 
expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)

row = 0
col = 0

#Iterate through all the expenses
#and add the data in the worksheet cells
for item, cost in (expenses):
    worksheet.write(row, col, item)
    worksheet.write(row, col + 1, cost)
    row += 1

#Create a format to update cells
format1 = workbook.add_format({'bg_color': 'blue',
                               'font_color': 'red'})

#Apply formatting to the cells that match the criteria
worksheet.conditional_format('B1:KB5', {'type':     'cell',
                                        'criteria': '>=',
                                        'value':    150,
                                        'format':   format1})

#Close the workbook object
workbook.close()
