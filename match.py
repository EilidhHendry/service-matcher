from fuzzywuzzy import process as fuzzy_process
import nltk
import regex

stopword_cache = nltk.corpus.stopwords.words("english")

services = {
    'handyman': ['handyman','odd jobs', 'sealing', 'decorating'],
    'cleaner': ['cleaner', 'deep clean', 'ironing', 'carpet cleaning'],
    'plumber': ['plumber', 'unblock drains', 'emergency plumber'],
    'electrician': ['electrician', 'light switches', 'emergency electrician', 'sockets']
}

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

def fuzzy_match(query_string):
    """
    Simple algorithm to match a query with it's corresponding service.
    Uses fuzzywuzzy package which uses Levenshtein edit distance to score potential matches.
    Not a complete algorithm. See README for limitiations.
    """
    # if an empty string is entered
    if not query_string:
        return None, None

    # lowercase the input
    query_string = query_string.lower()

    # create a generator object and pass to fuzzywuzzy process
    generator_object = (service for sublist in services.values() for service in sublist)
    result, _ = fuzzy_process.extractOne(query_string, generator_object) # currently don't care about second return arg (score)

    # if the result matches a broad service category
    if result in services.keys():
        return result, None
    else:
        # find the key of the result in the services dictionary
        # (probably not the best way to do this - rethink data structure)
        # returns None if can't be found
        service = next((service for service, sublist in services.iteritems() for sub_service in sublist if sub_service == result), None)
        # return services key and value
        return service, result


def interactive_match():
    query_string = raw_input("Please enter the service you would like: ")
    service, sub_service = fuzzy_match(query_string)

    # if the sub_service is returned as None
    if service and not sub_service:
        new_query = raw_input("You would like a " + service + ". What would you like this " + service + " to do? ")
        service, sub_service = fuzzy_match(new_query)

    # if both
    if service and sub_service:
        print "You would like a " + service + " to " + sub_service + "."

    # if neither or empty
    else:
        print "Service could not be found."


if __name__ == '__main__':
    interactive_match()
