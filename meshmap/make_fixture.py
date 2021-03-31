"""
Basic script for reading a CSV listing of contacts from `contacts.csv` and
creating a Django fixture in `contacts.json`. Fixtures can be loaded into
the DB with the `manage.py loaddata` command.
"""
import csv
import json

with open('contacts.csv', newline='') as csvfile:
    pk = 1
    contacts = []
    next(csvfile) # skip the header row
    for row in csv.reader(csvfile):
        contact = {
            'model': 'main.contact',
            'pk': pk,
            'fields': {
                'time': row[0],
                'source_name': row[1],
                # NOTE: this decimal to float conversion will lose precision, a
                # better solution would be a custom serializer and the Decimal
                # type: https://stackoverflow.com/questions/1960516/python-json-serialize-a-decimal-object
                'source_lat': float(row[2]),
                'source_lon': float(row[3]),
                'contact_name': row[4],
                'contact_lat': float(row[5]),
                'contact_lon': float(row[6]),
            }
        }
        contacts.append(contact)
        pk += 1
    with open('contacts.json', 'w') as jsonfile:
        jsonfile.write(json.dumps(contacts, sort_keys=True, indent=4))
