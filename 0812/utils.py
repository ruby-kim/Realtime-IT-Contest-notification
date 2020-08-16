import os
import json


def save(base_dir, data, filename):
    with open(os.path.join(base_dir, filename), 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent='\t')
    print("===== Finish saving data... =====")


def load(base_dir, filename):
    with open(base_dir + filename, encoding='utf-8', errors='ignore') as data:
        json_file = json.load(data, strict=False)
    return json_file
