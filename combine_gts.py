import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--gts", required=True, type=str)
parser.add_argument("--output", required=True, type=str)
args = parser.parse_args()

gt_paths = args.gts.split(';')
gts = []

for gt in gt_paths:
    with open(gt, 'r') as f:
        gts.append(json.load(f))

output = {'mappings': []}

for gt in gts:
    for entry in gt['mappings']:
        found = False
        for o in output['mappings']:
            if o['secdfd'] == entry['secdfd'] and o['pm'] == entry['pm']:
                found = True
                break
        if not found:
            output['mappings'].append(entry)

with open(args.output, 'w') as f:
    f.write(json.dumps(output))
