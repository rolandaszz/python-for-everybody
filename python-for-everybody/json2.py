import json

data = '''
{
  "note":"This file contains the sample data for testing",
  "comments":
[
    {
      "name":"Romina",
      "count":97
    },
    {
      "name":"Laurie",
      "count":97
    },
    {
      "name":"Bayli",
      "count":90
    },
    {
      "name":"Siyona",
      "count":90
    }
]
}'''

info = json.loads(data)
print('User count:', len(info))

for item in info():
    print(item['note'])

