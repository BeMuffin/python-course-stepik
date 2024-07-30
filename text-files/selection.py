import csv
from datetime import datetime

criminals = {
}

with open ('crimes.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        date = datetime.strptime(row['Date'], '%m/%d/%Y %I:%M:%S %p')
        search_date = '2015'
        if (date.year == datetime.strptime(search_date,'%Y').year):
            if(row['Primary Type'] in criminals):
                criminals[row['Primary Type']] +=1
            else:
                criminals[row['Primary Type']] = 1

print (criminals)

sorted_crimes = sorted(criminals.items(),key=lambda x:x[1],reverse=True)
print(sorted_crimes[0][0])


#https://docs.python.org/3/library/collections.html#collections.Counter - useful link