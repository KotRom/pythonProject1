import json
import csv

json_string = '''{
  "people": [
    {
      "name": "Jack Sumers",
      "phone": "555-555-555",
      "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
      "has_licence": false,
      "salary": 1500
    },
    {
      "name": "Mary Smith",
      "phone": "777-777-777",
      "emails": null,
      "has_licence": true,
      "salary": 1700
    },
    {
      "name": "Steven Cooke",
      "phone": null,
      "emails": "stevencooke@example.com",
      "has_licence": true,
      "salary": 2500
    }
  ]
}'''

csv_string = ''
data = json.loads(json_string)
for key in data['people'][0].keys():
    csv_string += key + ','
csv_string += '\n'
for person in data['people']:
    for x in person.values():
        csv_string += str(x) + ','
    csv_string += '\n'
print(csv_string)