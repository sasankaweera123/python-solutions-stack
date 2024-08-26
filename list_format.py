from collections import defaultdict

# Step 1: Calculate the sum of values for each itemid in list2
new_list = defaultdict(int)
for entry in list2:
    new_list[int(entry['itemid'])] += int(entry['value'])

# Step 2: Match itemids in list1 based on the name (excluding the "Bits" part)
matches = {}
for item in list1:
    key = item['name'].split(': Bits')[0]
    if key not in matches:
        matches[key] = {}
    if item['name'].endswith('Bits received'):
        matches[key]['received'] = new_list[int(item['itemid'])]
    elif item['name'].endswith('Bits sent'):
        matches[key]['sent'] = new_list[int(item['itemid'])]

# Step 3: Calculate the ratio for each matched pair
output = []
for key, values in matches.items():
    if 'received' in values and 'sent' in values:
        received = values['received']
        sent = values['sent']
        ratio = received / sent if sent != 0 else 0
        output.append({
            'name': key,
            'received': received,
            'sent': sent,
            'ratio': ratio
        })

# Fully expected output
print(output)
