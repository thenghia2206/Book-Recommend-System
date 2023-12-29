import pickle
import numpy as np

pt = pickle.load(open('Model/pt.pkl','rb'))
books = pickle.load(open('Model/books.pkl','rb'))
similarity_scores = pickle.load(open('Model/similarity_scores.pkl','rb'))

def predict_model(nameBook : str):
    try:
        index = np.where(pt.index == nameBook)[0][0]
    except IndexError:
        return False
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:6]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    return data