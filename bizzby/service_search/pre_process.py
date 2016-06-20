import nltk
import regex

stopword_cache = nltk.corpus.stopwords.words("english")

def remove_punctuation(text):
    return regex.sub(ur"\p{P}+", "", text)

def pre_process(query_string):
    # remove punctuation and lowercase query
    clean_string = remove_punctuation(query_string.lower())
    # split on whitespace into words
    clean_tokens = clean_string.split()
    # remove stopwords (a, the, etc.)
    query_words = [word for word in clean_tokens if word not in stopword_cache]
    return query_words

def find_ngrams(input_list, n):
    n_gram_tuples = zip(*[input_list[i:] for i in range(n)])
    n_gram_strings = []
    for n_gram_tuple in n_gram_tuples:
        tuple_string = ''
        for item in n_gram_tuple:
            tuple_string += ' ' + item
        n_gram_strings.append(tuple_string.strip())
    return n_gram_strings

def get_query_grams(query_string, n_gram_length=3):
    clean_words = pre_process(query_string)
    query_n_grams = []
    # get all ngrams up to n_gram_length
    # e.g. if n = 3 get words, bigrams, and trigrams
    for n in range(1, n_gram_length+1):
        n_grams = find_ngrams(clean_words, n)
        query_n_grams.append(n_grams)
    return query_n_grams
