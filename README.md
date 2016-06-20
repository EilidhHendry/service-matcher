This repo contains one potential solution to the problem of matching an input query to a service and sub-service.

## Set up:

```
git clone git@github.com:EilidhHendry/service-matcher.git
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python scripts/nltk.py
```

## Running django app locally
```
cd bizzby
python manage.py runserver
```
Then visit 'localhost:8000' in your browser.

## Running interactive algorithm

Running `python match.py` from the command line will start an interactive version of the algorithm.

It will prompt:
```
>>Please enter the service you would like:
```
Then type in a service, e.g. 'plumber'
```
>>>You would like a plumber. What would you like this plumber to do?
```
Type in the service you require, e.g. 'unblock drains'
```
>>>You would like a plumber to unblock drains.
```

## Algorithm (fuzzy matching django version)
First we extract keywords form the query.
Then compute bigrams, and trigrams from the query.
We then search through a tree of services and tasks. We use the fuzzy matching described below to find the most similar node in the tree and then move down the tree and either return the price, or a list of options.

# Limitiations
- Currently is looking to provide services related to washing machine install/repair so only takes queries related to this
- Query has to be quite similar to task stored in tree. (future work could perhaps use WordNet to find synonyms)
- Currently can't look further ahead in the tree. I.e. if you search 'install new washing machine' it will still ask whether it's new or replace.

## Algorithm (fuzzy matching command line version)
The current algorithm for matching query to category is a fairly simple one. It uses the fuzzywuzzy package to compute a score for the similarity between the query and each of the services and sub-services. The fuzzywuzzy package uses the Levenshtein edit distance to calculate the score.

I settled on the fuzzywuzzy package after performing some simple benchmarking and observing that it was faster than the other potential approaches

Improvements in the future would address the limitations described below. Rather than only looking at the top scoring match I would look at a number of high scoring results which scored above a threshold.

Other potential improvements include providing suggestions to users, and parsing the sentence to find keywords.

## Limitations (of command-line version)

- Currently takes either broad service category (e.g. handyman, plumber, cleaner) OR sub service (e.g. odd jobs, decorating, deep clean), but not both at once.
- If your query contains a word which identically matches a broad category then it will return the broad category and not match the sub category, e.g. "carpet cleaner" would match "cleaner" then give a follow up query for the sub category rather than returning "cleaner for carpet cleaning".
- Currently only excepts inputs from the following dictionary:
```
services = {
    'handyman': ['handyman','odd jobs', 'sealing', 'decorating'],
    'cleaner': ['cleaner', 'deep clean', 'ironing', 'carpet cleaning'],
    'plumber': ['plumber', 'unblock drains', 'emergency plumber'],
    'electrician': ['electrician', 'light switches', 'emergency electrician', 'sockets']
}
```
