import os.path
from .save_tree import load_tree, save_tree
from .main import Node, insert_text, find_prefix_root, print_autocomplete
from .cleanup_data import main

TREE_FILENAME = 'data/word_tree.rd'
DATA_FILENAME = 'data/word_list.txt'

suggestions = []


def build_or_load_tree():
    if os.path.exists(TREE_FILENAME):
        print("Loading existing tree...")
    else:
        print("Building new tree...")
        tree = Node()
        if not os.path.exists(DATA_FILENAME):
            main()
        with open(DATA_FILENAME, 'r') as data_file:
            for line in data_file:
                insert_text(tree, line.strip().lower(), 0)
        save_tree(tree, TREE_FILENAME)

    return load_tree(TREE_FILENAME)
        

trie = build_or_load_tree()

def suggest_word(word, tree=trie):
    suggestions.clear()
    root = find_prefix_root(tree, word, 0)
    print_autocomplete(root, suggestions)
    return suggestions