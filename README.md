## $5 Tech Unlocked 2021!
[Buy and download this product for only $5 on PacktPub.com](https://www.packtpub.com/)
-----
*The $5 campaign         runs from __December 15th 2020__ to __January 13th 2021.__*

# Automate it
This is the code repository for [Automate it!](https://www.packtpub.com/application-development/automate-it), published by Packt. It contains all the necessary code files.

##About the Book

This book gives you a great selection of recipes to automate your business processes with Python, and provides a platform for you to understand how Python is useful to make time consuming and repetitive business tasks more efficient. Python is a mature high level language, has object-oriented programming features, powers various apps, has a huge set of modules, and great community support. Python is extremely easy to use, can help you get complex tasks done efficiently and is an apt choice for our needs. 

With a classic problem-solution based approach and real-world examples, you will delve into things that automate your business processes. You will begin by learning about the Python modules to work with Web, Worksheets, Presentations and PDFs. You’ll leverage Python recipes to automate processes in HR, Finance and making them efficient and reliable. For instance, company payroll — an integral process in HR will be automated with Python recipes. 

A few chapters of this book will also help you gain knowledge on working with bots and computer vision. You will learn how to build bots for automating business use cases by integrating artificial intelligence. You’ll also understand how Python is helpful in face detection and building a scanner of your own. You will see how to effectively and easily use Python code to manage SMS and voice notifications, opening a world of possibilities using cloud telephony to solve your business needs. Moving forward, you will learn to work with APIs, Webhooks and Emails to automate Marketing and Customer Support processes. Finally, using the various Python libraries, this book will arm you with knowledge to customize data solutions and generate reports to meet your business needs. 
This book will help you up-skill and make your business processes efficient with the various Python recipes covered in this book.

##Instructions and Navigation
All of the code is organized into folders. For example, Chapter02.



The code will look like the following:
```
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
```

##Related Python Products:
* [Beginning Python](https://www.packtpub.com/application-development/beginning-python-video)
* [Python Machine Learning](https://www.packtpub.com/big-data-and-business-intelligence/python-machine-learning)
* [Mastering Object-oriented Python](https://www.packtpub.com/application-development/mastering-object-oriented-python)
* [Python Essentials](https://www.packtpub.com/application-development/python-essentials)
* [Learning Python for Forensics](https://www.packtpub.com/networking-and-servers/learning-python-forensics)


###Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSe5qwunkGf6PUvzPirPDtuy1Du5Rlzew23UBp2S-P3wB-GcwQ/viewform) if you have any feedback or suggestions.
