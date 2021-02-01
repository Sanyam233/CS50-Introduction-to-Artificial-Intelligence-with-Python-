import nltk
import sys
import os
import math
import string
import re


# FILE_MATCHES = 1
# SENTENCE_MATCHES = 1


# def main():

#     # Check command-line arguments
#     # if len(sys.argv) != 2:
#     #     sys.exit("Usage: python questions.py corpus")

#     # Calculate IDF values across files

#     load_files("corpus")
#     # files = load_files(sys.argv[1])
#     # file_words = {
#     #     filename: tokenize(files[filename])
#     #     for filename in files
#     # }
#     # file_idfs = compute_idfs(file_words)

#     # # Prompt user for query
#     # query = set(tokenize(input("Query: ")))

#     # # Determine top file matches according to TF-IDF
#     # filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

#     # # Extract sentences from top files
#     # sentences = dict()
#     # for filename in filenames:
#     #     for passage in files[filename].split("\n"):
#     #         for sentence in nltk.sent_tokenize(passage):
#     #             tokens = tokenize(sentence)
#     #             if tokens:
#     #                 sentences[sentence] = tokens

#     # # Compute IDF values across sentences
#     # idfs = compute_idfs(sentences)

#     # # Determine top sentence matches
#     # matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
#     # for match in matches:
#     #     print(match)


# def load_files(directory):
#     """
#     Given a directory name, return a dictionary mapping the filename of each
#     `.txt` file inside that directory to the file's contents as a string.
#     """

#     files = [f for f in os.listdir(directory)]

#     corpus = {}

#     for name in files:
#         text = open(os.path.join(directory, name))
#         corpus[name] = text.read()

#     return corpus




# def tokenize(document):
#     """
#     Given a document (represented as a string), return a list of all of the
#     words in that document, in order.

#     Process document by coverting all words to lowercase, and removing any
#     punctuation or English stopwords.
#     """
#     raise NotImplementedError


# def compute_idfs(documents):
#     """
#     Given a dictionary of `documents` that maps names of documents to a list
#     of words, return a dictionary that maps words to their IDF values.

#     Any word that appears in at least one of the documents should be in the
#     resulting dictionary.
#     """
#     raise NotImplementedError


# def top_files(query, files, idfs, n):
#     """
#     Given a `query` (a set of words), `files` (a dictionary mapping names of
#     files to a list of their words), and `idfs` (a dictionary mapping words
#     to their IDF values), return a list of the filenames of the the `n` top
#     files that match the query, ranked according to tf-idf.
#     """
#     raise NotImplementedError


# def top_sentences(query, sentences, idfs, n):
#     """
#     Given a `query` (a set of words), `sentences` (a dictionary mapping
#     sentences to a list of their words), and `idfs` (a dictionary mapping words
#     to their IDF values), return a list of the `n` top sentences that match
#     the query, ranked according to idf. If there are ties, preference should
#     be given to sentences that have a higher query term density.
#     """
#     raise NotImplementedError


# if __name__ == "__main__":
#     main()
import nltk
import sys
import os
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    # if len(sys.argv) != 2:
    #     sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files

    files = load_files("corpus")
    # token = tokenize(files["machine_learning.txt"])
    # print(token)

    # top_files(set(tokenize("the theory of probability is a representation of its concepts")), files, )
    # files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize("the theory of probability is a representation of its concepts"))  #input("Query: ")

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES) 

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


# def load_files(directory):
#   """
#   Given a directory name, return a dictionary mappingthe filename of each
#   `.txt` file inside that directory to the file'scontents as a string.
#   """
#   files = [f for f in os.listdir(directory)]
#   corpus = {}
#   for name in files:
#       text = open(os.path.join(directory, name))
#       corpus[name] = text.read()
#   return corpus




# def tokenize(document):
#   """
#   Given a document (represented as a string), return alist of all of the
#   words in that document, in order.
#   Process document by coverting all words to lowercase,and removing any
#   punctuation or English stopwords.
#   """
#   doc = nltk.word_tokenize(document.lower())
#   stop_words = set(nltk.corpus.stopwords.words("english"))
#   punc = string.punctuation

#   return [word for word in doc if word not in stop_words and word not in punc and word and re.search('[a-zA-Z]+', word)]



# def compute_idfs(documents):
#   """
#   Given a dictionary of `documents` that maps names ofdocuments to a list
#   of words, return a dictionary that maps words totheir IDF values.
#   Any word that appears in at least one of thedocuments should be in the
#   resulting dictionary.
#   """
#   container = {}

#   for doc in documents:
#     string = documents[doc]
#     for word in string:
#       if word in container:
#         if doc in container[word]:
#           continue
#         else:
#           container[word].append(doc)
#       else:
#         container[word] = [doc]
  
#   total_docs = len(documents)
  
#   return {word : math.log(total_docs / len(container[word])) for word in container}

# def top_files(query, files, idfs, n):
#     """
#     Given a `query` (a set of words), `files` (a dictionary mapping names of
#     files to a list of their words), and `idfs` (a dictionary mapping words
#     to their IDF values), return a list of the filenames of the the `n` top
#     files that match the query, ranked according to tf-idf.
#     """

#     file_freq = dict()

#     for fi in files:
#         freq = {}
#         for word in query:
#             for w in files[fi]:
#                 if word == w and word in freq:
#                     freq[word] += 1
#                 elif word == w and word not in freq:
#                     freq[word] = 1
        
#         tf_idf = {word : idfs[word] * freq[word] for word in freq}
        
#         file_freq[fi] = sum(round(tf_idf[f],2) for f in tf_idf)

#     sorted_file_freq = {k : v for k, v in sorted(file_freq.items(), key = lambda  item : -item[1])}

#     return list(sorted_file_freq.keys())[:n]



def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    sentence_idf = dict()   
    for sen in sentences:
        sentence_idf[sen] = [0, 0] 
        for word in query:
            if word in sentences[sen]:
                sentence_idf[sen][0] += idfs[word]
                sentence_idf[sen][1] += 1
        
        sentence_idf[sen][1] = round(sentence_idf[sen][1] / len(sentences[sen]))

    sorted_sentence_idf = {k : v for k , v in sorted(sentence_idf.items(), key = lambda x : (-x[1][0], -x[1][-1]))}  
    return list(sorted_sentence_idf)[:n]    

# def top_sentences(query, sentences, idfs, n):
#     """
#     Given a `query` (a set of words), `sentences` (a dictionary mapping
#     sentences to a list of their words), and `idfs` (a dictionary mapping words
#     to their IDF values), return a list of the `n` top sentences that match
#     the query, ranked according to idf. If there are ties, preference should
#     be given to sentences that have a higher query term density.
#     """
#     result = []
#     for sentence in sentences:
#         idf = 0
#         total_words_found = 0
#         for word in query:
#             if word in sentences[sentence]:
#                 total_words_found += 1
#                 idf += idfs[word]
#         density = float(total_words_found) / len(sentences[sentence])
#         result.append((sentence, idf, density))
#     result.sort(key=lambda x: (x[1], x[2]), reverse=True)
#     return [x[0] for x in result[:n]]
    

def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    files_mapping = {}
    for file_name in os.listdir(directory):
        with open(os.path.join(directory, file_name)) as f:
            files_mapping[file_name] = f.read()
    return files_mapping


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.
    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    words = nltk.word_tokenize(document.lower())
    processed_doc = []
    for word in words:
        if word not in nltk.corpus.stopwords.words("english") and word not in string.punctuation:
            processed_doc.append(word)
    return processed_doc


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.
    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    idfs = dict()
    words = set()
    total_docs = len(documents)
    for _file in documents:
        words.update(set(documents[_file]))

    for word in words:
        f = sum(word in documents[filename] for filename in documents)
        idf = math.log(total_docs / f)
        idfs[word] = idf
    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    tfidfs = []
    for filename in files:
        tfidf = 0
        for q in query:
            tfidf += idfs[q] * files[filename].count(q)
        tfidfs.append((filename, tfidf))
    tfidfs.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in tfidfs[:n]]


# def top_sentences(query, sentences, idfs, n):
#     """
#     Given a `query` (a set of words), `sentences` (a dictionary mapping
#     sentences to a list of their words), and `idfs` (a dictionary mapping words
#     to their IDF values), return a list of the `n` top sentences that match
#     the query, ranked according to idf. If there are ties, preference should
#     be given to sentences that have a higher query term density.
#     """
#     result = []
#     for sentence in sentences:
#         idf = 0
#         total_words_found = 0
#         for word in query:
#             if word in sentences[sentence]:
#                 total_words_found += 1
#                 idf += idfs[word]
#         density = float(total_words_found) / len(sentences[sentence])
#         result.append((sentence, idf, density))
#     result.sort(key=lambda x: (x[1], x[2]), reverse=True)
#     return [x[0] for x in result[:n]]

if __name__ == "__main__":
    main()
