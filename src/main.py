class Node:
    instance_count = 0 
    def __init__(self):
        Node.instance_count += 1
        self.id = Node.instance_count
        self.x = ''
        self.children ={}


def insert_text(root, text, idx):
    if idx == len(text):
        root.x = text 
        return 
    
    if text[idx] not in root.children:
        root.children[text[idx]] = Node()
    
    insert_text(root.children[text[idx]], text, idx+1)

def print_tree(root):
    print(f'    Node_{root.id}')
    for i in root.children:
        print(f'    Node_{root.id} -> Node_{root.children[i].id} [label="{i}"]')
        print_tree(root.children[i])


def find_prefix_root(root, prefix, idx):
    if idx == len(prefix):
        return root 
    if root == None:
        return None 
    if prefix[idx] not in root.children:
        return None 
    return find_prefix_root(root.children[prefix[idx]], prefix, idx+1)

def print_autocomplete(root, suggestions, prefix=''):
    if root:
        if root.x:
            suggestions.append(root.x)
            
        for char, child in root.children.items():
            print_autocomplete(child, suggestions, prefix + char,)


def dump_tree_dot(root):
    print('digraph True{')
    print_tree(root)
    print('}')

def remove_text(root, text, idx):
    if root is None:
        return
    
    if idx == len(text):
        root.x = ''  # Clear the word associated with the node
        return
    
    if text[idx] in root.children:
        remove_text(root.children[text[idx]], text, idx+1)
        
        # Clean up: If the child node has no children and no associated word, remove it
        if not root.children[text[idx]].children and not root.children[text[idx]].x:
            del root.children[text[idx]]
    else:
        print(f"Word '{text}' not found in the trie.")


if __name__=="__main__":
    main()