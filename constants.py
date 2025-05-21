import json

json_name = 'vocab.json'


def load_vocab():
    with open(json_name, 'r', encoding= 'utf-8') as f:
        return json.load(f)
    
def save_vocab(data):
    with open(json_name, 'w', encoding= 'utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False) 


times_for_word_review = 7
