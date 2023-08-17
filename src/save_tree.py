import pickle 

# serialize and save the prefix tree 
def save_tree(root, filename):
    with open(filename, 'wb') as file:
        pickle.dump(root, file)

# deserialize and load the prefix tree 
def load_tree(filename):
    with open(filename, 'rb') as file:
        return  pickle.load(file)

