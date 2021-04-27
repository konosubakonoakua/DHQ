import json
def get_imagenet_label_mapping() -> dict:
    with open("./mapping.json", 'r') as f:
        mapping = json.loads(f)
    return mapping