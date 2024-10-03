import requests
import csv

url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'
response = requests.get(url)

dataset= "C:/Users/hp/Desktop/mthree/C400Python/taxi_dataset.csv"
with open(dataset, 'wb') as file:
    file.write(response.content)

with open(dataset, newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    taxi = list(csvreader)


total_records = len(taxi)

print(total_records)

boroughs = set(row['Borough'] for row in taxi)
print(boroughs)

brooklyn_records = sum(1 for row in taxi if row['Borough'] == 'Brooklyn')
print(brooklyn_records)

output_file_path = 'C:/Users/hp/Desktop/mthree/C400Python/root/taxi_zone_output.txt'
with open(output_file_path,'w') as output_file:
    output_file.write(f"Total number of records: {total_records}\n")
    output_file.write(f"Unique boroughs: {', '.join(boroughs)}\n")
    output_file.write(f"Number of records for Brooklyn borough: {brooklyn_records}\n")