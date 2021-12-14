import csv
import json

# some JSON:
x = '{"devices":[{ "name":"John", "age":30, "city":"New York"},{ "name":"John", "age":30, "city":"New York"}]}'

devices = '{"devices":[{"name":"device_a","ip_address":"10.0.0.1","model":"3650","level":1,"interfaces":[{"gig1/0/1":"device_b","remote_port":"Gig0/0/15","remote_device_model":"1001X"},{"Ten0/0/0/4":"device_c","remote_port":"Fa1/15","remote_device_model":"4321"}]},{"name":"device_b","ip_address":"10.0.0.1","model":"3650","level":2,"interfaces":[{"Gig0/0/15":"device_a","remote_port":"gig1/0/1","remote_device_model":"3650"},{"Ten0/0/0/4":"device_c","remote_port":"Fa1/15","remote_device_model":"4321"}]}]}'

# parse x:
y = json.loads(devices)

# the result is a Python dictionary:
print(y["devices"][1]["interfaces"][0])

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
