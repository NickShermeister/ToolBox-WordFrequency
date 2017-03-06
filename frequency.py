""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    fulltext = open(file_name, 'r')
    lines = fulltext.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    fin_line = curr_line
    while lines[fin_line].find('End of the Project Gutenberg EBook') == -1:
        fin_line += 1
    lines = lines[curr_line+1:fin_line]
    newstring = ''
    compstring = ''
    for y in lines:
        compstring += y
    for x in compstring: #get rid of symbols that I don't want in my speech
        if x not in (string.punctuation):
            newstring += (x)
    finstring = newstring.lower()
    listowords = finstring.split()
    return listowords


def get_top_n_words(listowords, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    #NOTE: Yes, you gave an easy way to do this. I thought of a way and started doing it so I decided to finish it my way. I failed and it is now commented out.
    num = 0
    entiredict = dict()
    for y in listowords:    #run through all of the words and create a dictionary with them
        if y not in entiredict:
            entiredict[y] = 1
        else:
            entiredict[y] += 1
    WordandFreqs = []
    ordered_by_frequency = sorted(entiredict, key=entiredict.get, reverse=True)
    # reverse = dict()
    # for v, k in entiredict.items():
    #     if k not in reverse:
    #         reverse[k] = [v]
    #     else:
    #         reverse[k].append(v)
    # #allwords = []
    # tempdict = reverse
    # while num < n:
    #     temp = max(k for k, v in reverse.items())
    #     tempwords = reverse[temp]
    #     for x in tempwords:
    #         WordandFreqs.append(x)
    #         num += 1
    #     some_dict = {key: value for key, value in reverse.items() if value != temp}
    #     reverse = some_dict
    return ordered_by_frequency[0:n-1]

if __name__ == "__main__":
    #print("Running WordFrequency Toolbox")
    #print(string.punctuation)
    hi = get_word_list('twenty.txt')
    print(get_top_n_words(hi, 100))
