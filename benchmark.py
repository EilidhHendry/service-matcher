import timeit
from fuzzywuzzy import process
from match import services

def match(query_string):
    # find the minimum word length of the list of services
    min_service_length = min(len(word) for word in services.keys())

    # split the input string on whitespace
    # keep if length is greater than the min_service length
    candidate_words = [word for word in query_string.split() if len(word) >= min_service_length]

    for word in candidate_words:
        if word in services.keys():
            return word

    return None


def basic_match(query_string):
    query_words = query_string.split()
    for word in query_words:
        if word in services.keys():
            return word
    return None


def fuzzy_match(query_string):
    result, _ = process.extractOne(query_string, services.keys())
    return result

if __name__=="__main__":
    setup = 'import benchmark'
    input = '\'I need a plumber\''

    print 'match: ', min(timeit.Timer('benchmark.match(' + input + ')', setup=setup).repeat(3, 3))
    print 'basic match: ', min(timeit.Timer('benchmark.basic_match(' + input + ')', setup=setup).repeat(3, 3))
    print 'fuzzy match: ', min(timeit.Timer('benchmark.fuzzy_match(' + input + ')', setup=setup).repeat(3, 3))
