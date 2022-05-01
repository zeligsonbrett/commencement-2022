import csv

with open('2022 names - Sheet1') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
        current = '<div class = "name">' + row[0] + '</div>\n'
        print(current)