# PrettyPrint setup https://docs.python.org/3/library/pprint.html
import pprint
pp = pprint.PrettyPrinter(indent=4)

# A list of service dictionaries
services = [
    {"name": "Current site survey", "cost": 100},
    {"name": "Needs Assessment", "cost": 200},
    {"name": "New site development", "cost": 300}
]

# Calculate the TOTAL cost
total = 0
for service in services:
    total += service["cost"]

# Create the invoice dictionary
invoice = {"services": services, "total": total}

pp.pprint(invoice)
