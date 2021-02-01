import os
import random
import re
import sys
import copy

DAMPING = 0.85
SAMPLES = 10000


def main():
    # if len(sys.argv) != 2:
    #     sys.exit("Usage: python pagerank.py corpus")
    dic = "corpus0"
    corpus = crawl(dic)
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    pages = corpus.keys()
    num_of_pages = len(pages)
    links_on_page = corpus[page]
    num_of_links = len(links_on_page)
    distribution = {page : (1 - damping_factor)/num_of_pages for page in pages}

    for page in pages:
        if page in links_on_page:
            distribution[page] += damping_factor/num_of_links
        elif (num_of_links == 0):
            distribution[page] += damping_factor/num_of_pages

    return distribution

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages = corpus.keys()
    pageRank = {page : 0 for page in pages}
    current_page = random.choice(list(pages))

    for i in range(1, n):
        distribution = transition_model(corpus, current_page, damping_factor)
        for page in pageRank:
            pageRank[page] = ((pageRank[page] * (i - 1)  + distribution[page]))/i

        #selects a new page randomly based on weights
        current_page = random.choices(list(pageRank.keys()), list(pageRank.values()), k = 1)[0]

    return pageRank

def iter_sum(corpus, cpy, page):
    total = 0 
    for p in corpus:
        if page in corpus[p]:
            total += cpy[p] / len(corpus[p])
    
    return total


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages = corpus.keys()
    n = len(pages)
    pageRank = {page : 1/n for page in pages}    
    chng = True

    while chng:
        chng = False
        cpy = copy.deepcopy(pageRank)
        for page in corpus:
            pageRank[page] = ((1 - damping_factor)/n) + (damping_factor * iter_sum(corpus, cpy, page))
            chng = chng or abs(cpy[page] - pageRank[page]) > 0.001

    return pageRank

if __name__ == "__main__":
    main()