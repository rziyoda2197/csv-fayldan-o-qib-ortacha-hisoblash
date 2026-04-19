import csv
import statistics

def otracha_hisoblash(csv_fayl):
    with open(csv_fayl, 'r') as file:
        reader = csv.DictReader(file)
        salaries = [float(row['salary']) for row in reader]
        otracha = statistics.mean(salaries)
        return otracha

print(otracha_hisoblash('salaries.csv'))
