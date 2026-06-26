import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--gts", required=True, type=str)
parser.add_argument("--output", required=True, type=str)
args = parser.parse_args()

gt_paths = args.gts.split(';')
print('gt_paths:', gt_paths)
mappings = []

for gt in gt_paths:
    print('opening', gt)
    with open(gt, 'r') as f:
        loaded_json = json.load(f)
        print('loading', len(loaded_json), 'mappings')
        mappings.extend(loaded_json)

output = {
    'asset': {},
    'process': {},
    'data_store': {},
    'external_entity': {}
}

for m in mappings:
    sabo_type = m['sabo_type']
    secdfd_type = m['secdfd_type']
    if output[secdfd_type].get(sabo_type) is None:
        output[secdfd_type][sabo_type] = 1
    else:
        output[secdfd_type][sabo_type] += 1

with open(args.output, 'w') as f:
    f.write(json.dumps(output))
