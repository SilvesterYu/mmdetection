import pickle

with open('scratch1.pkl', 'rb') as f:
    x = pickle.load(f)
    for i in x:
        print("-"*100)
        print(list(i)[0])
    
