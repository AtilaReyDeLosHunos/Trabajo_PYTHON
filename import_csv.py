import csv
with open("address.csv" , 'r') as f:
    csvreader = csv.reader (f)
    print (type (csvreader))
    for row in csvreader:
        print (row[ 0], row[ 4])
        print (row)