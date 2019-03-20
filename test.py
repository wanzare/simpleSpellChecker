import unittest
import spellChecker.read as read
class Test(unittest.TestCase):
    from urllib import request
    url = "http://www.gutenberg.org/files/2554/2554.txt"
    response = request.urlopen(url)
    raw = response.read().decode('utf8')
    print(raw)
    i2 = ["power", "trusted"]
    FILE = "test_corpus.txt"
    vocab = read.create_vocab(FILE)
    checker = read.Checker(vocab)
    words = ["powr", "trustedd"]

    def test_vocab(self):
        self.assertEqual(len(Test.vocab), 93)

    def test_checker(self):
        self.assertEqual([Test.checker.correct(w) for w in Test.words], Test.i2)


if __name__ == '__main__':


    unittest.main()
