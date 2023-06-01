import json

with open('countries.json', 'r', encoding='utf-8') as input_file:
    data = json.load(input_file)
    religions = dict()
    for entry in data:
        if entry['religion'] not in religions.keys():
            religions[entry['religion']] = [entry['country']]
        else:
            religions[entry['religion']].append(entry['country'])

with open('religion.json', 'w', encoding='utf-8') as output_file:
    json.dump(religions, output_file, indent=3)
