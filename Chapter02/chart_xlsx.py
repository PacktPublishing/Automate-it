import xlsxwriter

#Create a workbook and add a worksheet
workbook = xlsxwriter.Workbook('chart_line.xlsx')
worksheet = workbook.add_worksheet()

#Data to be plotted as a chart in worksheet
data = [10, 40, 50, 20, 10, 50]

#Add the data to the columns A1-A6 in worksheet
worksheet.write_column('A1', data)

#Create a line chart object using data from cells A1-A6
chart = workbook.add_chart({'type': 'line'})
chart.add_series({'values': '=Sheet1!$A$1:$A$6'})

#Insert chart in the worksheet
worksheet.insert_chart('C1', chart)

#Close workbook object
workbook.close()
