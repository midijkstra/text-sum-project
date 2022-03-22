import re
import math
import numpy as np
import networkx as nx
import nltk

from nltk.cluster.util import cosine_distance
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def sent_tokenize(text):
    REG_STR = '[.!?;।' + '؛؟]'
    result = [s.strip() for s in re.split(REG_STR, text) if s.strip() != '']
    return result

def word_tokenize(x):
    REG_STR = '[0-9\W_]'
    data = []

    for text in x:
        text = [s.strip().lower() for s in re.split(REG_STR, text) if s.strip() != '']
        data.append(text)

    return data

def sim(s1, s2):
    words = list(set(s1 + s2))
    v1 = [0] * len(words)
    v2 = [0] * len(words)

    for w in s1:
        if w in stop_words:
            continue
        v1[words.index(w)] += 1

    for w in s2:
        if w in stop_words:
            continue
        v2[words.index(w)] += 1

    res = 1 - cosine_distance(v1, v2)
    return 1 if math.isnan(res) else res

def build_sim_matrix(text):
    size = len(text)
    sim_matrix = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            sim_matrix[i][j] = sim(text[i], text[j])

    return sim_matrix

# Summary generator
def summarize(original, translation):
    result = []
    original = sent_tokenize(original)
    text = word_tokenize(sent_tokenize(translation))

    sim_matrix = build_sim_matrix(text)
    sim_graph = nx.from_numpy_array(sim_matrix)
    scores = nx.pagerank(sim_graph)

    # Choose best n sentences,
    # Then print them in their original order
    res_size = 5 if len(scores) > 5 else len(scores)
    scores = list(dict(sorted(scores.items(), key=lambda item: item[1])))
    scores = scores[-1:-1-res_size:-1]
    scores.sort()

    for i in scores:
        result.append(original[i])

    return '. '.join(result) + '.'