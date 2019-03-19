Spell cheker
=========
A simple illustration of how a spell cheker works.     

## Requirements
```bash
import nltk 
```
## creating the vocabulary
We create a vocabulary by counting how many times each word in a corpus occurs.
## simple spell checking logic
The spell checker looks into the vocabulary and retrieves as candidates  all words that are at most one edit distance from the word to be spell checked .
 From the list of candidates, the correct word is the word with the highest frequency.
If there are no candidate words returned, the same word is returned as the correct word.
