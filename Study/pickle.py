import pickle

name = 'bright mind'
age = 27
address = '성북구 석관동'
score = {'math':100, 'english':100}

with open('bright_mind.p', 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(score, file)

with open('bright_mind.p', 'rb') as file:
    name2 = pickle.load(file)
    age2 = pickle.load(file)
    address2 = pickle.load(file)
    score2 = pickle.load(file)
    print(name2)
    print(age2)
    print(address2)
    print(score2)
