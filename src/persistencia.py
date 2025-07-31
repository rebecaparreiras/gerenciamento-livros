import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'livros.json')

def carregar_livros():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_livros(lista_livro):
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(lista_livro, f, ensure_ascii=False, indent=4)
