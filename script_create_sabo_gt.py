import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--sabo", required=True)
parser.add_argument("--gt", required=True)
parser.add_argument("--sabo_types", required=True)
args = parser.parse_args()


sabo_types = []
with open(args.gt, 'r') as f:
    gt = json.load(f)
with open(args.sabo, 'r') as f:
    sabo = json.load(f)
nodes = sabo['elements']['nodes']

for mapping in gt['mappings']:
    pm = mapping['pm']
    found = False
    for n in nodes:
        sabo_node = n['data']['id']
        if '$' in sabo_node and '$' not in pm:
            sabo_node = sabo_node.replace('$', '.')
        if sabo_node == pm:
            sabo_type = n['data']['labels']
            if len(sabo_type) != 1:
                print('BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', sabo_node)
            else:
                sabo_type = n['data']['labels'][0]
            sabo_types.append({'sabo': n['data']['id'], 'sabo_type': sabo_type, 'pm': pm, 'secdfd': mapping['secdfd'], 'secdfd_type': mapping['secdfd_type']})
            found = True
        if '(' in pm:
            if sabo_node[-1] == ')' and \
                    sabo_node.split('(')[0].replace('#', '.').lower() == pm.split('(')[0].lower():
                sabo_type = n['data']['labels']
                if len(sabo_type) != 1:
                    print('BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', sabo_node)
                else:
                    sabo_type = n['data']['labels'][0]
                sabo_types.append({'sabo': n['data']['id'], 'sabo_type': sabo_type, 'pm': pm, 'secdfd': mapping['secdfd'], 'secdfd_type': mapping['secdfd_type']})
                found = True
    if not found:
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', pm)
        sabo_types.append({'sabo': 'NOT_FOUND', 'sabo_type': 'UNKOWN', 'pm': pm, 'secdfd': mapping['secdfd'], 'secdfd_type': mapping['secdfd_type']})

with open(args.sabo_types, 'w') as f:
    f.write(json.dumps(sabo_types))
