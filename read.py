from nltk.tokenize import word_tokenize
from nltk.metrics import edit_distance
from collections import defaultdict
import json

def create_vocab(file):
    """
    Creates a vocabulary from a file
    :param file: Path to corpus
    :return: dictionary representing the dictionary
    """
    clean_vocab = defaultdict(int)
    text = open(file,"r")
    texts = text.readlines()
    #print(texts)
    for line in texts:
        word_tokens = word_tokenize(line.strip())  # remove urls, tokenize the text
        words = [w.lower() for w in word_tokens]  # lowercase
        for word in words:
            clean_vocab[word] += 1
    text.close()
    return  clean_vocab

def save_vocab(vocab,path):
    """

    :param vocab: vocabulary
    :param path: path to save
    :return:
    """
    with open(path, 'w') as outfile:
        json.dump(vocab, outfile)


def load_vocab(path):
    """

    :param path:path to json file
    :return: vocabulary
    """
    with open(path) as f:
        return json.load(f)

    
class Checker(object):
    """
    A spell checker - looks into the dictioary and retrieves all words that are only one eidt distance from the
    word to be spell checked as candidate words.
    The correct spelling is the word with the highest frequency.
    If there are no candidate words returned, the same word is returned as the correct spelling.
    attributes:

    vocab : a dictionary object representing the vocabulary

    """

    def __init__(self,vocab):
        self.vocab = vocab
    def correct(self, word):
        """

        :param word:word to be corrected
        :return: corrected word
        """
        most = self.find_nearest(word)
        rank = []
        if len(most)>0:
            for w in most:
                rank.append((self.vocab.get(w),w))
            sorted(rank)
            #print(rank)
            return rank[0][1]
        else:
            return word

    def find_nearest(self,word):
        """

        :param word: word to be corrected
        :return: candidate words
        """
        most=[]
        for w in self.vocab:
            if edit_distance(w,word)==1:
                most.append(w)
        return most



