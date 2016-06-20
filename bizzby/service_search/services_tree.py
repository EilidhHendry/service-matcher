from fuzzywuzzy import process as fuzzy_process
import pre_process

services_tree = {
    'root': ['washing machine', 'clean'],
    'washing machine': ['install', 'fit', 'repair'],
    'install': ['new', 'replace'],
    'fit': ['new', 'replace'],
    'new': 150,
    'replace': 99,
    'repair': 100,
    'clean': ['deep clean', 'ironing'],
    'deep clean': ['1 bedroom', '2 bedroom', '3 bedroom'],
    '1 bedroom': 100,
    '2 bedroom': 200,
    '3 bedroom': 300,
    'ironing': ['1 - 10 items', '10 - 20 items'],
    '1 - 10 items': 10,
    '10 - 20 items': 20,
}

def get_top_match(query_n_grams, candidates):
    matches = []
    # go through all the n-grams and add the top match and score to list
    for n_gram in query_n_grams:
        option = fuzzy_process.extractOne(n_gram, candidates)
        matches.append(option)

    # retrieve the item in the list with the max score
    best_match = max(matches, key=lambda item: item[1])

    return best_match


def search_services_tree(query_n_grams, node='root'):
    path = []
    while not is_price(services_tree[node]):
        children = services_tree[node]
        node, score = get_top_match(query_n_grams, children)
        if score < 65:
            return path, children
        path.append(node)
    return path, services_tree[node]


def is_price(value):
    try:
        value + 1
        return True
    except:
        return False


if __name__ == '__main__':
    query_string = "Install washing machine"
    query_n_grams = pre_process.get_query_grams(query_string)
    path, price = search_services_tree(query_n_grams, 'new')
    print path, price
