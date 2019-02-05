# built-in package
# some nice additions for doing common operations (see below)
# docs: https://docs.python.org/3/library/collections.html
import collections

# external package
# easy interaction with http(s) servers
import requests

# cache responses to speed up re-fetching URLs
import requests_cache
requests_cache.install_cache()

# convenience function for just getting the content of a URL
# --> as a byte sequence
def get_url_bytes(url):
    """Returns the raw bytes of the body of a server's response to a URL."""
    response = requests.get(url)
    return response.content
# Get some texts to use as a reference for the tests

electrons_book = get_url_bytes('https://www.gutenberg.org/ebooks/36456.txt.utf-8')
kjv_bible = get_url_bytes('https://www.gutenberg.org/ebooks/10.txt.utf-8')

def probabilities(b):
    counts = {} # empty dictionary
    len_of_seq = len(b) # returns num of bytes in the passed sequence
    for byte_b in b: # add each element into the dictionary and inc it's value
            if byte_b in counts.keys(): # if the key does exist, inc the value
                counts[byte_b] += 1
            else: # if the key does not exist, create key:value and init to 0
                counts[byte_b] = 1
    for key in counts:
        counts[key] = counts.get(key) / len_of_seq # divide each element by the byte sequence length

    return counts
from math import log2

def information(probs):
    shann_info = dict(probs) # made a copy of the passed dict
    for key in shann_info:
        shann_info[key] = log2( 1/shann_info[key] ) # Shannon Info Eq
    return shann_info

    def entropy(text):
    probs = probabilities(text)
    h = information(probs)
    e = 0 # init entropy var to 0
    for i in h:
        e += probs[i] * h[i] # entropy eq.
    return e
