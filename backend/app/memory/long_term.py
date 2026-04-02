import json

def save_memory(key, data):
    with open("memory.json", "a") as f:
        f.write(json.dumps({key: data}) + "\n")