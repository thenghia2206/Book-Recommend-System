import pickle
import numpy as np

pt = pickle.load(open('Model/pt.pkl','rb'))
books = pickle.load(open('Model/books.pkl','rb'))
similarity_scores = pickle.load(open('Model/similarity_scores.pkl','rb'))

def predict_model(bookId : str):
    try:
        index = np.where(pt.index == bookId)[0][0]
    except IndexError:
        return False
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:6]

    data = []
    for i in similar_items:
        temp_df = books[books['_id'] == pt.index[i[0]]]
        data.extend(list(temp_df.drop_duplicates('_id')['_id'].values))

    return data