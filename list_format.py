from collections import defaultdict

list1 = [
    {'itemid': '264', 'name': 'Interface Gi1/17(Port1:TP TPIA-CL03-017-G15-14): Bits sent', 'some_other_keys': 'some_more_values'},
    {'itemid': '215', 'name': 'Interface Te1/50("Port1:CL-PO-G22-23"): Bits received', 'some_other_keys': 'some_more_values'},
    {'itemid': '425', 'name': 'Interface Gi1/46(no description): Bits sent', 'some_other_keys': 'some_more_values'},
    {'itemid': '521', 'name': 'Interface Te1/50("Port1:CL-PO-G22-23"): Bits sent', 'some_other_keys': 'some_more_values'},
    {'itemid': '310', 'name': 'Interface Gi1/46(no description): Bits received', 'some_other_keys': 'some_more_values'},
    {'itemid': '123', 'name': 'Interface Gi1/17(Port1:TP TPIA-CL03-017-G15-14): Bits received', 'some_other_keys': 'some_more_values'},
]
list2 = [
    {'itemid': '264', 'clock': '1724146566', 'value': '6246880', 'ns': '120003316'},
    {'itemid': '264', 'clock': '1724146746', 'value': '6134912', 'ns': '113448784'},
    {'itemid': '215', 'clock': '1724144406', 'value': '5786832', 'ns': '157177073'},
    {'itemid': '215', 'clock': '1724144766', 'value': '5968784', 'ns': '760851309'},
    {'itemid': '425', 'clock': '1724148366', 'value': '6590424', 'ns': '403316048'},
    {'itemid': '425', 'clock': '1724148726', 'value': '6549984', 'ns': '484278803'},
    {'itemid': '521', 'clock': '1724148906', 'value': '6346488', 'ns': '306999249'},
    {'itemid': '521', 'clock': '1724147106', 'value': '6139008', 'ns': '459391602'},
    {'itemid': '310', 'clock': '1724147286', 'value': '6000208', 'ns': '826776455'},
    {'itemid': '310', 'clock': '1724147466', 'value': '6784960', 'ns': '152620809'},
    {'itemid': '123', 'clock': '1724147826', 'value': '6865272', 'ns': '70247389'},
    {'itemid': '123', 'clock': '1724148186', 'value': '6544328', 'ns': '610791670'},
]
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
