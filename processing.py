import pickle
import numpy as np
import spacy
from sklearn.metrics.pairwise import cosine_similarity
nlp = spacy.load('en_core_web_md')

final_df = pickle.load(open('final_df.pkl', 'rb'))

def preprocess_user_input(text):
    doc = nlp(text)
    no_stop_words = [token for token in doc if not token.is_stop and not token.is_punct]
    final_doc = nlp(str(no_stop_words))
    return final_doc.vector

def calculate_similarity(user_vector, df_column):
    similarities = []
    for vector in df_column:
        similarity = cosine_similarity([user_vector], [vector])
        similarities.append(similarity[0][0])
    return similarities

def result_eng(user_input, top_k=3):
    user_input_vector = preprocess_user_input(user_input)
    similarities = calculate_similarity(user_input_vector, final_df['exp_english_vec'])
    
    top_indices = np.argsort(similarities)[::-1][:top_k]
    top_k_rows = final_df.iloc[top_indices]
    
    results = []
    for index, row in top_k_rows.iterrows():
        result_dict = {
            'chapter': row.iloc[0],
            'verse': row.iloc[1],
            'shlokha': row.iloc[2],
            'eng_translation': row.iloc[3],
            'eng_meaning': row.iloc[4],
            'lang': 'eng'
        }
        results.append(result_dict)
    
    return results

def result_hin(user_input, top_k=3):
    user_input_vector = preprocess_user_input(user_input)
    similarities = calculate_similarity(user_input_vector, final_df['exp_english_vec'])
    
    top_indices = np.argsort(similarities)[::-1][:top_k]
    top_k_rows = final_df.iloc[top_indices]
    
    results = []
    for index, row in top_k_rows.iterrows():
        result_dict = {
            'chapter': row.iloc[0],
            'verse': row.iloc[1],
            'shlokha': row.iloc[2],
            'hin_translation': row.iloc[5],
            'hin_meaning': row.iloc[6],
            'lang': 'hin'
        }
        results.append(result_dict)
    
    return results

def recommend(user_input, top_k=3, output_lang='eng'):
    results = []
    if output_lang == 'eng':
        results = result_eng(user_input, top_k)
    elif output_lang == 'hin':
        results = result_hin(user_input, top_k)
    else:
        results = ['Something went wrong']
    return results
